# Build and deploy the Copilot Multi-Industry Demo Hub to Azure Static Web Apps.
# Reads Azure details from ~/.scout/copilot-demo-hub/local-config.json (kept out of the repo).
# Every az call passes --subscription, so the default Azure CLI context is never changed.
#
# Usage:  pwsh tools/deploy_azure.ps1            # rebuild data.js + hub.html, package, deploy
#         pwsh tools/deploy_azure.ps1 -SkipBuild # package and deploy the current build
param([switch]$SkipBuild)
$ErrorActionPreference = 'Stop'
$repo = Split-Path -Parent $PSScriptRoot
$cfgPath = Join-Path $HOME '.scout\copilot-demo-hub\local-config.json'
if (-not (Test-Path $cfgPath)) { throw "Local config not found: $cfgPath" }
$cfg = Get-Content $cfgPath -Raw | ConvertFrom-Json
Set-Location $repo
$env:PYTHONIOENCODING = 'utf-8'

if (-not $SkipBuild) {
    python build_master.py; if ($LASTEXITCODE) { throw 'build_master.py failed' }
    python gen_hub.py; if ($LASTEXITCODE) { throw 'gen_hub.py failed' }
}
python tools\build_azure_dist.py; if ($LASTEXITCODE) { throw 'build_azure_dist.py failed' }

foreach ($app in @(@($cfg.azure.media_app, 'dist\media'), @($cfg.azure.main_app, 'dist\main'))) {
    $token = az staticwebapp secrets list --name $app[0] --resource-group $cfg.azure.resource_group `
        --subscription $cfg.azure.subscription --query properties.apiKey -o tsv 2>$null
    if (-not $token) { throw "No deployment token for $($app[0]). Sign in to the Caldova tenant with az login first." }
    $env:SWA_CLI_DEPLOYMENT_TOKEN = $token
    try {
        npx -y @azure/static-web-apps-cli@2 deploy $app[1] --env production --no-use-keychain
        if ($LASTEXITCODE) { throw "Deploy failed: $($app[0])" }
    }
    finally {
        Remove-Item Env:SWA_CLI_DEPLOYMENT_TOKEN -ErrorAction SilentlyContinue
        $token = $null
    }
}
Write-Host "Deployed: $($cfg.azure.main_host)"
