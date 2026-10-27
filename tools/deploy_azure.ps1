# Build and deploy the Copilot Multi-Industry Demo Hub to Azure App Service.
# Reads Azure details from ~/.scout/copilot-demo-hub/local-config.json (kept out of the repo).
# Every az call passes --subscription, so the default Azure CLI context is never changed.
# Uploads use a Microsoft Entra token (password-based deploy logins stay disabled) and the
# site is sent in parts of about 40 MB, because one large upload gets cut off.
#
# Usage:  pwsh tools/deploy_azure.ps1              # rebuild data.js + hub.html, package, deploy
#         pwsh tools/deploy_azure.ps1 -SkipBuild   # package and deploy the current build
#         pwsh tools/deploy_azure.ps1 -Redirects   # also refresh the forwarding page on the old addresses
#         pwsh tools/deploy_azure.ps1 -NoClean     # overlay the files so the live site stays up while uploading (files removed from the build are left behind)
param([switch]$SkipBuild, [switch]$Redirects, [switch]$NoClean)
$ErrorActionPreference = 'Stop'
$repo = Split-Path -Parent $PSScriptRoot
$cfgPath = Join-Path $HOME '.scout\copilot-demo-hub\local-config.json'
if (-not (Test-Path $cfgPath)) { throw "Local config not found: $cfgPath" }
$cfg = (Get-Content $cfgPath -Raw | ConvertFrom-Json).appservice
Set-Location $repo
$env:PYTHONIOENCODING = 'utf-8'

if (-not $SkipBuild) {
    python build_master.py; if ($LASTEXITCODE) { throw 'build_master.py failed' }
    python gen_hub.py; if ($LASTEXITCODE) { throw 'gen_hub.py failed' }
}
python tools\build_azure_dist.py; if ($LASTEXITCODE) { throw 'build_azure_dist.py failed' }

$scm = "https://$($cfg.app).scm.azurewebsites.net/api/publish"
$parts = @(Get-ChildItem dist\chunks\part-*.zip | Sort-Object Name)
for ($i = 0; $i -lt $parts.Count; $i++) {
    $clean = if ($i -eq 0 -and -not $NoClean) { 'true' } else { 'false' }
    $restart = if ($i -eq $parts.Count - 1) { 'true' } else { 'false' }
    $ok = $false
    for ($try = 1; $try -le 3 -and -not $ok; $try++) {
        $hdr = Join-Path $env:TEMP ('kudu-' + [guid]::NewGuid().ToString('N') + '.txt')
        try {
            $token = az account get-access-token --subscription $cfg.subscription --query accessToken -o tsv
            if (-not $token) { throw 'No Azure token. Sign in to the Caldova tenant with az login first.' }
            Set-Content -Path $hdr -Value ('Authorization: Bearer ' + $token) -NoNewline -Encoding ascii
            $token = $null
            $code = curl.exe -s -o NUL -w '%{http_code}' -X POST "$($scm)?type=zip&clean=$clean&restart=$restart" `
                -H "@$hdr" -H 'Content-Type: application/octet-stream' --data-binary "@$($parts[$i].FullName)" --max-time 1200
            $ok = ($code -eq '200' -or $code -eq '202')
            Write-Host ("{0}: HTTP {1} (try {2})" -f $parts[$i].Name, $code, $try)
        }
        finally { Remove-Item $hdr -Force -ErrorAction SilentlyContinue }
        if (-not $ok) { Start-Sleep 15 }
    }
    if (-not $ok) { throw "Upload failed: $($parts[$i].Name)" }
}

if ($Redirects) {
    foreach ($swa in $cfg.old_swa) {
        $token = az staticwebapp secrets list --name $swa --resource-group $cfg.resource_group `
            --subscription $cfg.subscription --query properties.apiKey -o tsv 2>$null
        if (-not $token) { throw "No deployment token for $swa" }
        $env:SWA_CLI_DEPLOYMENT_TOKEN = $token
        try {
            npx -y @azure/static-web-apps-cli@2 deploy dist\redirect --env production --no-use-keychain
            if ($LASTEXITCODE) { throw "Redirect deploy failed: $swa" }
        }
        finally {
            Remove-Item Env:SWA_CLI_DEPLOYMENT_TOKEN -ErrorAction SilentlyContinue
            $token = $null
        }
    }
}
Write-Host "Deployed: $($cfg.host)"
