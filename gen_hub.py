
# gen_hub.py — Generate hub.html with departments tab + sector grouping
HTML = r"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>IDMY Copilot Industry Hub</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap" rel="stylesheet">
<style>
*{margin:0;padding:0;box-sizing:border-box}
:root{
  --navy:#1F2D55;--blue:#0078D4;--teal:#00A8A8;--accent:#FF6B35;
  --bg:#F0F4F8;--white:#FFFFFF;--text:#1A1A2E;--muted:#6B7280;
  --card:#FFFFFF;--border:#E2E8F0;--sidebar:290px;
}
body{font-family:'Inter',system-ui,sans-serif;background:var(--bg);color:var(--text);min-height:100vh}
/* TOP BAR */
.topbar{
  background:linear-gradient(135deg,#0F1C3F,#1F2D55);
  padding:0 28px;height:56px;display:flex;align-items:center;justify-content:space-between;
  position:sticky;top:0;z-index:100;box-shadow:0 2px 16px rgba(0,0,0,0.3);
}
.topbar-left{display:flex;align-items:center;gap:12px}
.topbar-logo{width:28px;height:28px;background:linear-gradient(135deg,#0078D4,#00A8A8);border-radius:6px;display:flex;align-items:center;justify-content:center;font-size:14px}
.topbar-title{color:#FFFFFF;font-size:15px;font-weight:700;letter-spacing:0.3px}
.topbar-badge{background:rgba(0,168,168,0.2);border:1px solid rgba(0,168,168,0.4);border-radius:20px;padding:3px 10px;color:#00A8A8;font-size:11px;font-weight:600}
.topbar-right{display:flex;align-items:center;gap:8px}
.btn-sm{padding:7px 14px;border-radius:8px;border:1px solid rgba(255,255,255,0.2);background:rgba(255,255,255,0.08);color:rgba(255,255,255,0.8);font-size:12px;font-weight:600;cursor:pointer;transition:all 0.2s;font-family:inherit}
.btn-sm:hover{background:rgba(255,255,255,0.15);color:#FFFFFF}
/* LAYOUT */
.layout{display:flex;min-height:calc(100vh - 56px)}
/* SIDEBAR */
.sidebar{
  width:var(--sidebar);background:#FFFFFF;border-right:1px solid var(--border);
  position:sticky;top:56px;height:calc(100vh - 56px);overflow-y:auto;flex-shrink:0;display:flex;flex-direction:column;
}
.sidebar-tabs{display:flex;border-bottom:2px solid var(--border);flex-shrink:0}
.sidebar-tab{flex:1;padding:12px 0;text-align:center;font-size:12px;font-weight:700;cursor:pointer;color:var(--muted);border-bottom:2px solid transparent;margin-bottom:-2px;transition:all 0.2s}
.sidebar-tab.active{color:var(--blue);border-bottom-color:var(--blue)}
.sidebar-panel{display:none;flex:1;overflow-y:auto}
.sidebar-panel.active{display:block}
.sidebar-section{padding:12px 0 6px}
.sidebar-label{padding:0 14px 5px;font-size:9px;font-weight:700;text-transform:uppercase;letter-spacing:1.2px;color:var(--muted)}
.sector-label{padding:6px 14px 4px;font-size:9px;font-weight:800;text-transform:uppercase;letter-spacing:1.2px;color:#94A3B8;margin-top:4px}
.sidebar-item{
  display:flex;align-items:center;gap:9px;padding:9px 14px;cursor:pointer;
  transition:all 0.15s;border-left:3px solid transparent;font-size:12px;font-weight:500;color:var(--text);
}
.sidebar-item:hover{background:#F8FAFC;color:var(--blue)}
.sidebar-item.active{background:#EEF4FF;border-left-color:var(--blue);color:var(--blue);font-weight:600}
.sidebar-item .ind-icon{font-size:15px;width:22px;text-align:center}
.sidebar-item .ind-name{flex:1;line-height:1.3}
.sidebar-item .ind-count{background:#F1F5F9;border-radius:10px;padding:1px 6px;font-size:10px;color:var(--muted);font-weight:600}
.sidebar-divider{height:1px;background:var(--border);margin:6px 14px}
/* MAIN */
.main{flex:1;overflow:hidden;padding:28px;max-width:calc(100vw - var(--sidebar))}
/* WHATS NEW */
.whats-new{
  background:linear-gradient(135deg,#0F1C3F,#1F2D55 60%,#0078D4);
  border-radius:16px;padding:20px 24px;margin-bottom:24px;
  display:flex;align-items:center;gap:16px;overflow:hidden;position:relative;
}
.whats-new::before{content:'';position:absolute;right:-40px;top:-40px;width:200px;height:200px;border-radius:50%;background:rgba(0,168,168,0.15)}
.wn-icon{font-size:28px;flex-shrink:0}
.wn-content{flex:1;min-width:0}
.wn-tag{display:inline-block;background:rgba(0,168,168,0.2);border:1px solid rgba(0,168,168,0.4);border-radius:20px;padding:2px 10px;color:#00A8A8;font-size:10px;font-weight:700;text-transform:uppercase;letter-spacing:0.8px;margin-bottom:6px}
.wn-title{color:#FFFFFF;font-size:15px;font-weight:700;margin-bottom:3px}
.wn-desc{color:rgba(255,255,255,0.65);font-size:12px;line-height:1.5}
.wn-nav{display:flex;gap:6px;flex-shrink:0}
.wn-btn{background:rgba(255,255,255,0.1);border:1px solid rgba(255,255,255,0.2);border-radius:8px;padding:6px 10px;color:rgba(255,255,255,0.7);cursor:pointer;font-size:14px;transition:all 0.2s}
.wn-btn:hover{background:rgba(255,255,255,0.2);color:#FFFFFF}
.wn-dots{display:flex;gap:5px;align-items:center;margin-top:8px}
.wn-dot{width:6px;height:6px;border-radius:50%;background:rgba(255,255,255,0.3);cursor:pointer;transition:all 0.2s}
.wn-dot.active{background:#00A8A8;width:16px;border-radius:3px}
/* HOME GRID */
.home-header{margin-bottom:20px}
.home-title{font-size:22px;font-weight:800;color:var(--navy);margin-bottom:4px}
.home-subtitle{color:var(--muted);font-size:13px}
.home-stats{display:flex;gap:10px;margin-top:14px;flex-wrap:wrap}
.stat-chip{background:#FFFFFF;border:1px solid var(--border);border-radius:10px;padding:7px 14px;display:flex;align-items:center;gap:7px;font-size:12px}
.stat-chip .val{font-weight:700;color:var(--navy)}
.stat-chip .lbl{color:var(--muted)}
/* Tab toggle above grid */
.grid-tabs{display:flex;gap:8px;margin-bottom:20px}
.grid-tab{padding:8px 20px;border-radius:20px;border:2px solid var(--border);background:#FFFFFF;color:var(--muted);font-size:13px;font-weight:700;cursor:pointer;transition:all 0.2s;font-family:inherit}
.grid-tab.active{background:var(--navy);border-color:var(--navy);color:#FFFFFF}
/* Sector group in grid */
.sector-header{font-size:11px;font-weight:800;text-transform:uppercase;letter-spacing:1.2px;color:var(--muted);padding:16px 0 8px;border-bottom:1px solid var(--border);margin-bottom:12px;grid-column:1/-1}
.ind-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(210px,1fr));gap:14px}
.ind-card{
  background:#FFFFFF;border:1px solid var(--border);border-radius:14px;padding:18px;
  cursor:pointer;transition:all 0.2s;position:relative;overflow:hidden;
}
.ind-card::before{content:'';position:absolute;top:0;left:0;right:0;height:3px;background:var(--ind-color,var(--blue))}
.ind-card:hover{transform:translateY(-2px);box-shadow:0 10px 28px rgba(0,0,0,0.1);border-color:var(--ind-color,var(--blue))}
.ind-card-icon{font-size:28px;margin-bottom:10px}
.ind-card-name{font-size:13px;font-weight:700;color:var(--navy);margin-bottom:3px}
.ind-card-company{font-size:11px;color:var(--muted);margin-bottom:8px;line-height:1.4}
.ind-card-pills{display:flex;gap:5px;flex-wrap:wrap;margin-top:6px}
.pill{background:#F1F5F9;border-radius:16px;padding:2px 7px;font-size:10px;color:var(--muted);font-weight:600}
.pill.premium{background:#EEF4FF;color:var(--blue)}
.pill.basic{background:#F0FDF4;color:#16A34A}
.pill.dept{background:#FFF3E0;color:#C2410C}
.ind-card-prompts{font-size:11px;color:var(--muted);margin-top:8px;display:flex;align-items:center;gap:4px}
/* DETAIL */
.prompt-fileref{
  display:inline-flex;align-items:center;gap:6px;
  background:#EEF4FF;border:1px solid #C7DEFF;border-radius:6px;
  padding:5px 10px;font-size:11px;color:#0078D4;font-weight:600;
  margin-bottom:8px;
}
.prompt-fileref::before{content:"📁 Open first: ";font-weight:400;color:#555}
.tool-account-bar{
  padding:8px 16px;font-size:11px;background:#F8FAFC;
  border-bottom:1px solid #E2E8F0;display:flex;align-items:center;gap:6px;
  color:#6B7280;
}
.tool-account-bar strong{color:#1F2D55}
.detail-view{display:none}
.detail-view.active{display:block}
.detail-hero{
  background:linear-gradient(135deg,var(--ind-color,var(--navy)),var(--ind-accent,var(--blue)));
  border-radius:16px;padding:28px;margin-bottom:24px;position:relative;overflow:hidden;
}
.detail-hero::after{content:var(--ind-icon,'🏢');position:absolute;right:24px;top:50%;transform:translateY(-50%);font-size:80px;opacity:0.15}
.detail-hero-back{display:inline-flex;align-items:center;gap:6px;color:rgba(255,255,255,0.7);font-size:12px;font-weight:600;cursor:pointer;margin-bottom:12px;transition:color 0.2s;background:none;border:none;font-family:inherit;padding:0}
.detail-hero-back:hover{color:#FFFFFF}
.detail-hero-badge{background:rgba(255,255,255,0.15);border:1px solid rgba(255,255,255,0.25);border-radius:20px;padding:4px 12px;color:rgba(255,255,255,0.9);font-size:11px;font-weight:600;display:inline-block;margin-bottom:12px}
.detail-hero-title{color:#FFFFFF;font-size:24px;font-weight:800;margin-bottom:6px}
.detail-hero-company{color:rgba(255,255,255,0.85);font-size:14px;font-weight:600;margin-bottom:6px}
.detail-hero-tagline{color:rgba(255,255,255,0.65);font-size:13px;line-height:1.5}
.detail-body{display:grid;grid-template-columns:1fr 310px;gap:22px;align-items:start}
.detail-scenario{background:#FFFFFF;border:1px solid var(--border);border-radius:14px;padding:18px;margin-bottom:18px}
.detail-scenario-title{font-size:13px;font-weight:700;color:var(--navy);margin-bottom:8px;display:flex;align-items:center;gap:6px}
.detail-scenario-text{font-size:13px;color:var(--muted);line-height:1.6}
.tool-section{margin-bottom:16px}
.tool-header{
  display:flex;align-items:center;gap:10px;padding:11px 14px;
  background:#F8FAFC;border:1px solid var(--border);border-radius:10px;
  cursor:pointer;transition:all 0.2s;user-select:none;
}
.tool-header:hover{background:#EEF4FF;border-color:var(--blue)}
.tool-header.open{background:#EEF4FF;border-color:var(--blue);border-bottom-left-radius:0;border-bottom-right-radius:0}
.tool-name{font-size:13px;font-weight:700;color:var(--navy);flex:1}
.tool-license{font-size:10px;font-weight:700;padding:3px 7px;border-radius:10px}
.tool-license.premium{background:#EEF4FF;color:var(--blue)}
.tool-license.basic{background:#F0FDF4;color:#16A34A}
.tool-chevron{color:var(--muted);transition:transform 0.2s;font-size:12px}
.tool-header.open .tool-chevron{transform:rotate(180deg)}
.tool-prompts{display:none;border:1px solid var(--blue);border-top:none;border-bottom-left-radius:10px;border-bottom-right-radius:10px;overflow:hidden}
.tool-prompts.open{display:block}
.prompt-item{padding:13px 15px;border-bottom:1px solid #F1F5F9;cursor:pointer;transition:background 0.15s;position:relative}
.prompt-item:last-child{border-bottom:none}
.prompt-item:hover{background:#F8FAFC}
.prompt-item:hover .copy-btn{opacity:1}
.prompt-title{font-size:12px;font-weight:700;color:var(--navy);margin-bottom:4px}
.prompt-text{font-size:12px;color:#2D3748;line-height:1.7;white-space:pre-wrap;background:#F8FAFC;border-left:3px solid #0078D4;padding:11px 13px;border-radius:0 8px 8px 0;margin:6px 0 10px}
.copy-btn{
  position:absolute;right:12px;top:50%;transform:translateY(-50%);
  background:var(--blue);color:#FFFFFF;border:none;border-radius:6px;
  padding:4px 9px;font-size:10px;font-weight:700;cursor:pointer;
  opacity:0;transition:opacity 0.2s;font-family:inherit;
}
.copy-btn:hover{background:#005EA6}
.detail-sidebar{}
.files-card{background:#FFFFFF;border:1px solid var(--border);border-radius:14px;padding:18px;margin-bottom:14px}
.files-title{font-size:13px;font-weight:700;color:var(--navy);margin-bottom:10px;display:flex;align-items:center;gap:6px}
.file-item{display:flex;align-items:center;gap:9px;padding:7px 9px;border:1px solid var(--border);border-radius:7px;margin-bottom:5px;font-size:12px;background:#FAFBFC;text-decoration:none;color:var(--text);transition:all 0.15s;cursor:pointer}
.file-item:hover{background:#EEF4FF;border-color:var(--blue)}
.file-item:last-child{margin-bottom:0}
.file-ext{font-weight:700;padding:2px 5px;border-radius:4px;font-size:10px;flex-shrink:0}
.file-ext.xlsx{background:#E8F5E9;color:#2E7D32}
.file-ext.docx{background:#E3F2FD;color:#1565C0}
.file-ext.msg{background:#FFF3E0;color:#E65100}
.file-name{flex:1;color:var(--text);font-weight:500;word-break:break-word;line-height:1.3}
.tips-card{background:linear-gradient(135deg,#0F1C3F,#1F2D55);border-radius:14px;padding:18px}
.tips-title{color:#FFFFFF;font-size:13px;font-weight:700;margin-bottom:10px;display:flex;align-items:center;gap:6px}
.tip-item{display:flex;gap:7px;margin-bottom:9px;font-size:12px;color:rgba(255,255,255,0.75);line-height:1.5}
.tip-item:last-child{margin-bottom:0}
.tip-num{background:rgba(0,168,168,0.2);border:1px solid rgba(0,168,168,0.4);color:#00A8A8;border-radius:50%;width:17px;height:17px;display:flex;align-items:center;justify-content:center;font-weight:700;font-size:10px;flex-shrink:0;margin-top:1px}
/* Toast */
.toast{position:fixed;bottom:24px;right:24px;background:#1F2D55;color:#FFFFFF;padding:12px 20px;border-radius:10px;font-size:13px;font-weight:600;box-shadow:0 8px 24px rgba(0,0,0,0.3);transform:translateY(100px);opacity:0;transition:all 0.3s;z-index:1000;display:flex;align-items:center;gap:8px}
.toast.show{transform:translateY(0);opacity:1}
/* MY/ID context toggle */
.ctx-toggle{display:flex;background:rgba(255,255,255,0.08);border:1px solid rgba(255,255,255,0.15);border-radius:8px;overflow:hidden;flex-shrink:0}
.ctx-btn{padding:5px 12px;border:none;background:transparent;color:rgba(255,255,255,0.6);font-size:12px;font-weight:700;cursor:pointer;transition:all 0.2s;font-family:inherit}
.ctx-btn.active{background:rgba(255,255,255,0.18);color:#FFFFFF}
.ctx-btn:hover:not(.active){color:rgba(255,255,255,0.85)}
/* Dept pills row inside scenario */
.dept-pills{display:flex;flex-wrap:wrap;gap:6px;margin-top:14px;padding-top:14px;border-top:1px dashed var(--border)}
.dept-pills-label{font-size:10px;font-weight:700;text-transform:uppercase;letter-spacing:1px;color:var(--muted);width:100%;margin-bottom:2px}
.dept-pill{padding:5px 11px;background:#FFF3E0;border:1px solid #FED7AA;border-radius:14px;font-size:11px;color:#C2410C;font-weight:700;cursor:pointer;transition:all 0.15s;display:inline-flex;align-items:center;gap:4px}
.dept-pill:hover{background:#FED7AA;color:#9A3412;transform:translateY(-1px)}
/* Storyboard card */
.storyboard-card{background:#FFFFFF;border:1px solid var(--border);border-radius:14px;padding:18px;margin-bottom:18px}
.storyboard-title{font-size:13px;font-weight:700;color:var(--navy);margin-bottom:4px;display:flex;align-items:center;gap:6px}
.storyboard-sub{font-size:11px;color:var(--muted);margin-bottom:14px}
.sb-exercises{display:flex;flex-direction:column;gap:12px}
.sb-ex{border-left:3px solid var(--blue);padding:10px 14px;background:#F8FAFC;border-radius:0 8px 8px 0}
.sb-ex-head{display:flex;align-items:center;gap:8px;margin-bottom:6px;flex-wrap:wrap}
.sb-ex-num{font-size:10px;font-weight:800;color:#FFFFFF;background:var(--blue);padding:3px 9px;border-radius:10px;text-transform:uppercase;letter-spacing:0.5px}
.sb-ex-title{font-size:13px;font-weight:700;color:var(--navy);flex:1;min-width:0}
.sb-ex-meta{font-size:10px;color:var(--muted);font-weight:600;background:#FFFFFF;border:1px solid var(--border);padding:2px 8px;border-radius:10px}
.sb-ex-summary{font-size:11px;color:#475569;margin-bottom:8px;line-height:1.5;font-style:italic}
.sb-tasks{display:flex;flex-wrap:wrap;gap:6px}
.sb-task{display:inline-flex;align-items:center;gap:6px;padding:5px 10px;background:#FFFFFF;border:1px solid var(--border);border-radius:14px;font-size:10px;color:var(--text);font-weight:600;cursor:pointer;transition:all 0.15s}
.sb-task:hover{border-color:var(--blue);background:#EEF4FF;transform:translateY(-1px)}
.sb-task-n{font-weight:800;color:var(--blue);font-size:10px}
.sb-task-verb{font-weight:600}
.sb-task-mode{font-size:9px;text-transform:uppercase;padding:1px 6px;border-radius:8px;font-weight:800;letter-spacing:0.4px}
.sb-task-mode.show{background:#FFF3E0;color:#C2410C}
.sb-task-mode.hands{background:#F0FDF4;color:#16A34A}
/* Personas card (right sidebar) */
.personas-card{background:#FFFFFF;border:1px solid var(--border);border-radius:14px;padding:18px;margin-bottom:14px}
.personas-title{font-size:13px;font-weight:700;color:var(--navy);margin-bottom:10px;display:flex;align-items:center;gap:6px}
.persona-item{display:flex;align-items:flex-start;gap:10px;padding:9px 0;border-bottom:1px solid #F1F5F9}
.persona-item:last-child{border-bottom:none}
.persona-avatar{width:34px;height:34px;border-radius:50%;display:flex;align-items:center;justify-content:center;color:#FFFFFF;font-weight:700;font-size:11px;flex-shrink:0}
.persona-info{flex:1;min-width:0}
.persona-name{font-size:12px;font-weight:700;color:var(--navy);line-height:1.3}
.persona-role{font-size:10.5px;color:var(--muted);margin-top:1px;line-height:1.3}
.persona-lic{font-size:9px;font-weight:700;color:#0078D4;background:#EEF4FF;padding:2px 7px;border-radius:8px;display:inline-block;margin-top:3px}
.persona-lic.free{color:#16A34A;background:#F0FDF4}
/* Researcher callout + mode label */
.researcher-callout{padding:12px 14px;background:linear-gradient(135deg,#FEF3C7,#FDE68A);border:1px solid #F6CB6F;border-radius:8px;margin:0 0 12px 0;font-size:11.5px;color:#7C5400;line-height:1.65}
.researcher-callout strong{color:#5C3F00}
.researcher-callout-row{display:block;margin-top:4px}
.prompt-mode{display:inline-block;background:#FEF3C7;color:#92400E;font-size:10px;font-weight:800;padding:3px 9px;border-radius:10px;margin-right:8px;letter-spacing:0.3px;text-transform:uppercase;border:1px solid #FCD34D}
/* Detail tabs (Tools vs Chat) */
.detail-tabs{display:flex;gap:6px;margin-bottom:16px;border-bottom:2px solid var(--border);padding-bottom:0}
.detail-tab{padding:9px 16px;background:transparent;border:none;border-bottom:2px solid transparent;margin-bottom:-2px;color:var(--muted);font-size:13px;font-weight:700;cursor:pointer;transition:all 0.2s;font-family:inherit}
.detail-tab.active{color:var(--blue);border-bottom-color:var(--blue)}
.detail-tab:hover:not(.active){color:var(--navy)}
/* Frontier license badge */
.tool-license.frontier{background:#FFF3E0;color:#C2410C;border:1px solid #FED7AA}
/* Persona chip on prompt */
.prompt-persona{display:inline-block;font-size:10px;font-weight:800;padding:3px 9px;border-radius:10px;margin-right:8px;letter-spacing:0.3px;border:1px solid currentColor;background:#FFFFFF}
/* Responsive */
@media(max-width:768px){
  .sidebar{display:none}
  .main{padding:16px;max-width:100vw}
  .detail-body{grid-template-columns:1fr}
  .detail-sidebar{order:-1}
  .ind-grid{grid-template-columns:repeat(auto-fill,minmax(150px,1fr))}
}
::-webkit-scrollbar{width:5px}
::-webkit-scrollbar-track{background:#F1F5F9}
::-webkit-scrollbar-thumb{background:#CBD5E1;border-radius:3px}
::-webkit-scrollbar-thumb:hover{background:#94A3B8}
</style>
</head>
<body>

<!-- TOP BAR -->
<nav class="topbar">
  <div class="topbar-left">
    <div class="topbar-logo">🤖</div>
    <span class="topbar-title">IDMY Copilot Industry Hub</span>
    <span class="topbar-badge">29 Industries · 10 Departments</span>
  </div>
  <div class="topbar-right">
    <div class="ctx-toggle">
      <button class="ctx-btn active" id="ctx-my" onclick="setCtx('MY')">&#127474;&#127486; Malaysia</button>
      <button class="ctx-btn" id="ctx-id" onclick="setCtx('ID')">&#127470;&#127465; Indonesia</button>
    </div>
    <button class="btn-sm" onclick="goHome()">&#x1F3E0; Home</button>
    <button class="btn-sm" onclick="logout()">&#x1F512; Lock</button>
  </div>
</nav>

<!-- LAYOUT -->
<div class="layout">

  <!-- SIDEBAR -->
  <aside class="sidebar" id="sidebar">
    <div class="sidebar-tabs">
      <div class="sidebar-tab active" id="stab-ind" onclick="setSidebarTab('ind')">🏭 Industries</div>
      <div class="sidebar-tab" id="stab-dept" onclick="setSidebarTab('dept')">🏢 Departments</div>
    </div>
    <!-- Industries panel -->
    <div class="sidebar-panel active" id="spanel-ind">
      <div class="sidebar-section">
        <a class="sidebar-item active" id="nav-all-ind" onclick="showGridTab('ind')">
          <span class="ind-icon">🏠</span>
          <span class="ind-name">All Industries</span>
          <span class="ind-count" id="total-ind-count">29</span>
        </a>
      </div>
      <div class="sidebar-divider"></div>
      <div id="sidebar-industries"></div>
    </div>
    <!-- Departments panel -->
    <div class="sidebar-panel" id="spanel-dept">
      <div class="sidebar-section">
        <a class="sidebar-item active" id="nav-all-dept" onclick="showGridTab('dept')">
          <span class="ind-icon">🏠</span>
          <span class="ind-name">All Departments</span>
          <span class="ind-count" id="total-dept-count">10</span>
        </a>
      </div>
      <div class="sidebar-divider"></div>
      <div id="sidebar-departments"></div>
    </div>
  </aside>

  <!-- MAIN -->
  <main class="main" id="main">

    <!-- WHATS NEW -->
    <div class="whats-new" id="whats-new-banner">
      <div class="wn-icon">✨</div>
      <div class="wn-content">
        <div class="wn-tag" id="wn-tag">Loading...</div>
        <div class="wn-title" id="wn-title">Loading...</div>
        <div class="wn-desc" id="wn-desc">Loading...</div>
        <div class="wn-dots" id="wn-dots"></div>
      </div>
      <div class="wn-nav">
        <button class="wn-btn" onclick="wnNav(-1)">&#8249;</button>
        <button class="wn-btn" onclick="wnNav(1)">&#8250;</button>
      </div>
    </div>

    <!-- HOME VIEW -->
    <div id="home-view">
      <div class="home-header">
        <div class="home-title">&#127474;&#127486; &#127470;&#127465; IDMY Industry Hub</div>
        <div class="home-subtitle">Select an industry or department to explore M365 Copilot demo scenarios, prompts, and reference files</div>
        <div class="home-stats">
          <div class="stat-chip"><span class="val">29</span><span class="lbl">Industries</span></div>
          <div class="stat-chip"><span class="val">10</span><span class="lbl">Departments</span></div>
          <div class="stat-chip"><span class="val" id="prompt-count">--</span><span class="lbl">Total Prompts</span></div>
          <div class="stat-chip"><span class="val">14</span><span class="lbl">Copilot Tools</span></div>
        </div>
      </div>
      <!-- Grid tab toggle -->
      <div class="grid-tabs">
        <button class="grid-tab active" id="gtab-ind" onclick="showGridTab('ind')">&#127981; Industries (29)</button>
        <button class="grid-tab" id="gtab-dept" onclick="showGridTab('dept')">&#127970; Departments (10)</button>
      </div>
      <!-- Industry grid (sector grouped) -->
      <div id="ind-grid-wrap">
        <div class="ind-grid" id="ind-grid"></div>
      </div>
      <!-- Department grid -->
      <div id="dept-grid-wrap" style="display:none">
        <div class="ind-grid" id="dept-grid"></div>
      </div>
    </div>

    <!-- DETAIL VIEW -->
    <div id="detail-view" class="detail-view">
      <div class="detail-hero" id="detail-hero">
        <button class="detail-hero-back" id="detail-back-btn" onclick="goHome()">&#8592; Back</button>
        <div class="detail-hero-badge" id="detail-badge">Industry</div>
        <div class="detail-hero-title" id="detail-title">Title</div>
        <div class="detail-hero-company" id="detail-company">Company</div>
        <div class="detail-hero-tagline" id="detail-tagline">Tagline</div>
      </div>
      <div class="detail-body">
        <div class="detail-main-col" id="detail-main-col">
          <div class="detail-scenario" id="detail-scenario"></div>
          <div id="detail-storyboard" class="storyboard-card" style="display:none"></div>
          <div class="detail-tabs" id="detail-tabs" style="display:none"></div>
          <div id="detail-prompts"></div>
        </div>
        <div class="detail-sidebar">
          <div class="files-card" id="detail-files"></div>
          <div class="personas-card" id="detail-personas" style="display:none"></div>
          <div class="tips-card" id="detail-tips"></div>
        </div>
      </div>
    </div>

  </main>
</div>

<!-- TOAST -->
<div class="toast" id="toast">&#10003; Prompt copied to clipboard!</div>

<!-- SCRIPTS -->
<script src="data.js"></script>
<script>
if(sessionStorage.getItem('hub_auth')!=='ok') window.location.href='index.html';

let wnIdx=0;
let currentGridTab='ind';
let currentSidebarTab='ind';
let _ctx='MY'; // 'MY' or 'ID'
let _detailTab='tools'; // 'tools' or 'chat'
let _currentTab='ind'; // 'ind' or 'dept' (which type was last shown)
const data=window.HUB_DATA;

function setCtx(c){
  _ctx=c;
  document.getElementById('ctx-my').classList.toggle('active',c==='MY');
  document.getElementById('ctx-id').classList.toggle('active',c==='ID');
  // Rebuild grids and sidebar with new context
  buildGrid(); buildDeptGrid(); buildSidebar(); buildDeptSidebar();
  // If detail view open, fully re-render with new context
  if(_currentItem && document.getElementById('detail-view').style.display!=='none'){
    showItem(_currentItem,_currentTab);
  }
}
function _getCompany(item){return _ctx==='ID'&&item.companyID?item.companyID:item.company;}
function _getTagline(item){return _ctx==='ID'&&item.taglineID?item.taglineID:item.tagline;}
function _getScenario(item){return _ctx==='ID'&&item.scenarioID?item.scenarioID:item.scenario;}
function _getPrompts(t){return _ctx==='ID'&&t.promptsID&&t.promptsID.length?t.promptsID:t.prompts;}
function _getPersona(t,pi){
  const arr=_ctx==='ID'&&t.personaID&&t.personaID.length?t.personaID:(t.persona||[]);
  return arr[pi]||'';
}
function _isResearcher(name){return /Researcher/i.test(name||'')}
function _isCowork(name){return /Cowork/i.test(name||'')}
function _isChat(name){return /Copilot Chat/i.test(name||'')&&!/Notebook/i.test(name||'')}
function _isFrontier(lic){return /Frontier/i.test(lic||'')}
function _personaColor(name){
  if(!name) return '#6B7280';
  if(/Hadar/i.test(name)) return '#1E40AF';
  if(/Sasha/i.test(name)) return '#7C3AED';
  if(/Mod/i.test(name)) return '#059669';
  if(/Daichi/i.test(name)) return '#DC2626';
  // Departmental fallback by hash
  let h=0; for(let i=0;i<name.length;i++) h=(h*31+name.charCodeAt(i))|0;
  const palette=['#1E40AF','#7C3AED','#059669','#DC2626','#0891B2','#CA8A04','#9333EA','#0D9488'];
  return palette[Math.abs(h)%palette.length];
}
let _currentItem=null;

// ── Sidebar tab toggle ──
function setSidebarTab(tab){
  currentSidebarTab=tab;
  ['ind','dept'].forEach(t=>{
    document.getElementById('stab-'+t).classList.toggle('active',t===tab);
    document.getElementById('spanel-'+t).classList.toggle('active',t===tab);
  });
}

// ── Grid tab toggle ──
function showGridTab(tab){
  currentGridTab=tab;
  setSidebarTab(tab);
  // Always restore the home (gallery) view — clicking "All Industries" or "All
  // Departments" from a detail page must take the user back to the grid.
  document.getElementById('home-view').style.display='block';
  const dv=document.getElementById('detail-view');
  dv.classList.remove('active'); dv.style.display='none';
  _currentItem=null;
  document.getElementById('gtab-ind').classList.toggle('active',tab==='ind');
  document.getElementById('gtab-dept').classList.toggle('active',tab==='dept');
  document.getElementById('ind-grid-wrap').style.display=tab==='ind'?'block':'none';
  document.getElementById('dept-grid-wrap').style.display=tab==='dept'?'block':'none';
  // Reset sidebar nav highlights to "All"
  document.querySelectorAll('.sidebar-item').forEach(el=>el.classList.remove('active'));
  if(tab==='ind') document.getElementById('nav-all-ind').classList.add('active');
  else document.getElementById('nav-all-dept').classList.add('active');
  window.scrollTo({top:0,behavior:'smooth'});
}

// ── Build sidebar industries (sector-grouped) ──
function buildSidebar(){
  const el=document.getElementById('sidebar-industries');
  el.innerHTML='';
  let totalPrompts=0;
  // Group by sector
  data.sectors.forEach(sec=>{
    const inds=sec.industries.map(id=>data.industries.find(i=>i.id===id)).filter(Boolean);
    if(!inds.length) return;
    const lbl=document.createElement('div');
    lbl.className='sector-label';
    lbl.textContent=sec.label;
    el.appendChild(lbl);
    inds.forEach(ind=>{
      const count=ind.prompts.reduce((a,t)=>a+t.prompts.length,0);
      totalPrompts+=count;
      const a=document.createElement('a');
      a.className='sidebar-item'; a.id='nav-'+ind.id;
      a.onclick=()=>showItem(ind,'ind');
      a.innerHTML='<span class="ind-icon">'+ind.icon+'</span><span class="ind-name">'+ind.name+'</span><span class="ind-count">'+count+'</span>';
      el.appendChild(a);
    });
  });
  document.getElementById('prompt-count').textContent=totalPrompts+data.departments.reduce((a,d)=>a+d.prompts.reduce((b,t)=>b+t.prompts.length,0),0);
}

// ── Build sidebar departments ──
function buildDeptSidebar(){
  const el=document.getElementById('sidebar-departments');
  el.innerHTML='';
  data.departments.forEach(dept=>{
    const count=dept.prompts.reduce((a,t)=>a+t.prompts.length,0);
    const a=document.createElement('a');
    a.className='sidebar-item'; a.id='nav-'+dept.id;
    a.onclick=()=>showItem(dept,'dept');
    a.innerHTML='<span class="ind-icon">'+dept.icon+'</span><span class="ind-name">'+dept.name+'</span><span class="ind-count">'+count+'</span>';
    el.appendChild(a);
  });
}

// ── Build industry grid (sector-grouped) ──
function buildGrid(){
  const el=document.getElementById('ind-grid');
  el.innerHTML='';
  data.sectors.forEach(sec=>{
    const inds=sec.industries.map(id=>data.industries.find(i=>i.id===id)).filter(Boolean);
    if(!inds.length) return;
    const hdr=document.createElement('div');
    hdr.className='sector-header';
    hdr.textContent=sec.label.toUpperCase();
    el.appendChild(hdr);
    inds.forEach(ind=>el.appendChild(makeCard(ind,'ind')));
  });
}

// ── Build department grid ──
function buildDeptGrid(){
  const el=document.getElementById('dept-grid');
  el.innerHTML='';
  data.departments.forEach(dept=>el.appendChild(makeCard(dept,'dept')));
}

function makeCard(item,tab){
  const count=item.prompts.reduce((a,t)=>a+t.prompts.length,0);
  const tools=[...new Set(item.prompts.map(t=>t.tool.replace(/^[^\s]+ /,'')))].slice(0,3);
  const div=document.createElement('div');
  div.className='ind-card';
  div.style.setProperty('--ind-color',item.color);
  div.onclick=()=>showItem(item,tab);
  const isDept=tab==='dept';
  div.innerHTML=
    '<div class="ind-card-icon">'+item.icon+'</div>'+
    '<div class="ind-card-name">'+item.name+'</div>'+
    '<div class="ind-card-company">'+_getCompany(item)+'</div>'+
    '<div class="ind-card-pills">'+
      tools.map(t=>'<span class="pill">'+t+'</span>').join('')+
      (isDept?'<span class="pill dept">Department</span>':'')+
    '</div>'+
    '<div class="ind-card-prompts">&#x1F4AC; '+count+' prompts &middot; '+item.files.length+' files</div>';
  return div;
}

// ── What's New ──
function buildWhatsNew(){
  const items=data.whatsNew;
  const dots=document.getElementById('wn-dots');
  dots.innerHTML=items.map((_,i)=>'<div class="wn-dot'+(i===0?' active':'')+'" onclick="setWn('+i+')"></div>').join('');
  setWn(0);
}
function setWn(i){
  wnIdx=i; const item=data.whatsNew[i];
  document.getElementById('wn-tag').textContent=item.badge||item.tag||'';
  document.getElementById('wn-title').textContent=item.title||'';
  document.getElementById('wn-desc').textContent=item.summary||item.desc||item.tip||'';
  document.querySelectorAll('.wn-dot').forEach((d,j)=>{d.classList.toggle('active',j===i)});
}
function wnNav(dir){setWn((wnIdx+dir+data.whatsNew.length)%data.whatsNew.length)}
setInterval(()=>wnNav(1),6000);

// ── Show item detail (works for both industries and departments) ──
function showItem(item,tab){
  _currentItem=item;
  _currentTab=tab||'ind';
  const id=item.id;
  // Hero
  const hero=document.getElementById('detail-hero');
  hero.style.background='linear-gradient(135deg,'+item.color+','+(item.accent||item.color)+')';
  hero.style.setProperty('--ind-icon','"'+item.icon+'"');
  const isDept=tab==='dept';
  document.getElementById('detail-back-btn').textContent=isDept?'← Back to all departments':'← Back to all industries';
  document.getElementById('detail-back-btn').onclick=()=>{ goHome(); showGridTab(tab); };
  document.getElementById('detail-badge').textContent=isDept?'Department':item.name;
  document.getElementById('detail-title').textContent=_getCompany(item);
  document.getElementById('detail-company').textContent=item.name;
  document.getElementById('detail-tagline').textContent=_getTagline(item);
  // Scenario + dept pills
  const scenarioText=_getScenario(item);
  let pillsHtml='';
  if(item.relevantDepts && item.relevantDepts.length){
    const pills=item.relevantDepts.map(did=>{
      const d=data.departments.find(x=>x.id===did);
      if(!d) return '';
      return '<span class="dept-pill" data-did="'+escapeAttr(d.id)+'">'+d.icon+' '+escapeHTML(d.name)+'</span>';
    }).filter(Boolean).join('');
    if(pills){
      pillsHtml='<div class="dept-pills"><div class="dept-pills-label">🏢 Departments most affected — click to drill down</div>'+pills+'</div>';
    }
  }
  document.getElementById('detail-scenario').innerHTML=
    '<div class="detail-scenario-title">📋 Demo Scenario</div>'+
    '<div class="detail-scenario-text">'+escapeHTML(scenarioText)+'</div>'+pillsHtml;
  // Wire dept pills
  document.querySelectorAll('#detail-scenario .dept-pill').forEach(el=>{
    el.onclick=()=>{
      const did=el.getAttribute('data-did');
      const d=data.departments.find(x=>x.id===did);
      if(d) showItem(d,'dept');
    };
  });
  // Storyboard
  const sbWrap=document.getElementById('detail-storyboard');
  if(item.storyboard && item.storyboard.length){
    sbWrap.style.display='block';
    sbWrap.innerHTML=
      '<div class="storyboard-title">🎬 Storyboard <span style="font-size:11px;font-weight:500;color:var(--muted)">— '+item.storyboard.length+' exercises across one morning</span></div>'+
      '<div class="storyboard-sub">Run these tools in sequence to deliver an end-to-end demo flow. Click a tool below the storyboard to copy its prompts.</div>'+
      '<div class="sb-exercises">'+
      item.storyboard.map(ex=>{
        const exTitle=_ctx==='ID'&&ex.titleID?ex.titleID:ex.title;
        const exSummary=_ctx==='ID'&&ex.summaryID?ex.summaryID:(ex.summary||'');
        const tasks=(ex.tasks||[]).map(t=>{
          const verb=_ctx==='ID'&&t.verbID?t.verbID:t.verb;
          const mode=t.mode==='hands'?'hands':'show';
          const modeLabel=mode==='hands'?'Hands-on':'Show & Tell';
          return '<span class="sb-task" data-tool="'+escapeAttr(t.tool||'')+'">'+
            '<span class="sb-task-n">'+escapeHTML(t.n||'')+'</span>'+
            '<span class="sb-task-verb">'+escapeHTML(verb||'')+'</span>'+
            '<span class="sb-task-mode '+mode+'">'+modeLabel+'</span>'+
            '</span>';
        }).join('');
        return '<div class="sb-ex">'+
          '<div class="sb-ex-head">'+
            '<span class="sb-ex-num">EX '+(ex.ex||'')+'</span>'+
            '<span class="sb-ex-title">'+escapeHTML(exTitle||'')+'</span>'+
            '<span class="sb-ex-meta">⏱ '+(ex.minutes||15)+' min · '+escapeHTML(ex.mode||'')+'</span>'+
          '</div>'+
          (exSummary?'<div class="sb-ex-summary">'+escapeHTML(exSummary)+'</div>':'')+
          '<div class="sb-tasks">'+tasks+'</div>'+
          '</div>';
      }).join('')+
      '</div>';
  } else {
    sbWrap.style.display='none';
    sbWrap.innerHTML='';
  }
  // Tab toggle (Tools vs Chat) — only show if tool list contains both T_CHAT and other tools
  const hasChat=item.prompts.some(t=>_isChat(t.tool));
  const hasOther=item.prompts.some(t=>!_isChat(t.tool));
  const tabsWrap=document.getElementById('detail-tabs');
  if(hasChat && hasOther){
    tabsWrap.style.display='flex';
    tabsWrap.innerHTML=
      '<button class="detail-tab '+( _detailTab==='tools'?'active':'')+'" id="dtab-tools" onclick="setDetailTab(\'tools\')">🛠️ M365 Copilot Tools</button>'+
      '<button class="detail-tab '+( _detailTab==='chat'?'active':'')+'" id="dtab-chat" onclick="setDetailTab(\'chat\')">💬 Copilot Chat Prompts</button>';
  } else {
    tabsWrap.style.display='none';
    tabsWrap.innerHTML='';
    _detailTab='tools';
  }
  // Filter prompts by tab
  const visibleTools=item.prompts.filter(t=>{
    if(!hasChat||!hasOther) return true;
    if(_detailTab==='chat') return _isChat(t.tool);
    return !_isChat(t.tool);
  });
  // Prompts
  const pEl=document.getElementById('detail-prompts');
  pEl.innerHTML='';
  visibleTools.forEach((tool)=>{
    const ti=item.prompts.indexOf(tool);
    const isBasic=tool.license&&(tool.license.toLowerCase().includes('basic')||tool.license.toLowerCase().includes('free'));
    const isFront=_isFrontier(tool.license);
    const isResearcher=_isResearcher(tool.tool);
    const sec=document.createElement('div'); sec.className='tool-section';
    const promptArr=_getPrompts(tool);
    const promHtml=promptArr.map((p,pi)=>{
      const key=_pmKey(id,ti,pi);
      const txt=typeof p==='string'?p:(p.prompt||'');
      _PM[key]=txt;
      const persona=_getPersona(tool,pi);
      const pColor=_personaColor(persona);
      let modeLbl='';
      if(isResearcher){
        modeLbl=pi===0
          ?'<span class="prompt-mode">🔍 Critique Mode</span>'
          :'<span class="prompt-mode">⚖️ Model Council</span>';
      }
      const personaChip=persona
        ?'<span class="prompt-persona" style="color:'+pColor+'">👤 '+escapeHTML(persona)+'</span>'
        :'';
      return '<div class="prompt-item">'+
        '<div class="prompt-title">'+modeLbl+personaChip+'💬 Prompt '+(pi+1)+'</div>'+
        '<div class="prompt-text">'+escapeHTML(txt)+'</div>'+
        '<button class="copy-btn" onclick="copyById(\''+key+'\')">Copy prompt</button>'+
        '</div>';
    }).join('');
    let licClass='premium', licLabel='✨ M365 Copilot';
    if(isBasic){ licClass='basic'; licLabel='🆓 No License Required'; }
    if(isFront){ licClass='frontier'; licLabel='🔥 M365 + Frontier'; }
    let researcherCallout='';
    if(isResearcher){
      researcherCallout='<div class="researcher-callout">'+
        '<strong>🔍 Critique Mode</strong> — Researcher self-critiques every source, verifying claims against the originals before including them in the report. Best for getting trustworthy, citation-grounded answers fast.'+
        '<span class="researcher-callout-row"></span>'+
        '<strong>⚖️ Model Council</strong> — Researcher orchestrates multiple frontier reasoning models (GPT-5, Claude, Gemini, etc.) to debate the brief, surface dissent, and synthesise a balanced view. Best for high-stakes decisions where you want diverse expert input.'+
        '</div>';
    }
    sec.innerHTML=
      '<div class="tool-header" id="tool-hdr-'+id+'-'+ti+'" onclick="toggleTool(\''+id+'-'+ti+'\')">'+
        '<span class="tool-name">'+escapeHTML(tool.tool)+'</span>'+
        '<span class="tool-license '+licClass+'">'+licLabel+'</span>'+
        '<span class="tool-chevron">▼</span>'+
      '</div>'+
      '<div class="tool-prompts" id="tool-prm-'+id+'-'+ti+'">'+
        (tool.account?'<div class="tool-account-bar">👤 Demo account: <strong>'+escapeHTML(tool.account)+'</strong></div>':'')+
        researcherCallout+
        promHtml+
      '</div>';
    pEl.appendChild(sec);
  });
  if(visibleTools.length){ toggleTool(id+'-'+item.prompts.indexOf(visibleTools[0])); }
  // Files
  const fEl=document.getElementById('detail-files');
  fEl.innerHTML='<div class="files-title">📁 Reference Files <span style="font-size:11px;font-weight:400;color:var(--muted)">— click to download</span></div>'+
    item.files.map(f=>{
      const ext=f.split('.').pop().toLowerCase();
      return '<a class="file-item" href="files/'+encodeURIComponent(f)+'" download="'+f+'" target="_blank">'+
        '<span class="file-ext '+ext+'">'+ext.toUpperCase()+'</span>'+
        '<span class="file-name">'+escapeHTML(f)+'</span>'+
        '<span style="margin-left:auto;font-size:11px;color:var(--blue);font-weight:600">⬇ Download</span>'+
        '</a>';
    }).join('');
  // Personas card (between files and tips)
  const personasEl=document.getElementById('detail-personas');
  if(item.personas && item.personas.length){
    personasEl.style.display='block';
    personasEl.innerHTML=
      '<div class="personas-title">🎭 Personas in this demo</div>'+
      item.personas.map(p=>{
        const role=_ctx==='ID'&&p.roleID?p.roleID:p.role;
        const initials=(p.name||'').split(' ').map(s=>s[0]).join('').slice(0,2).toUpperCase();
        const isFree=/free/i.test(p.lic||'');
        return '<div class="persona-item">'+
          '<div class="persona-avatar" style="background:'+(p.color||_personaColor(p.name))+'">'+initials+'</div>'+
          '<div class="persona-info">'+
            '<div class="persona-name">'+escapeHTML(p.name||'')+'</div>'+
            '<div class="persona-role">'+escapeHTML(role||'')+'</div>'+
            '<div class="persona-lic '+(isFree?'free':'')+'">'+escapeHTML(p.lic||'')+'</div>'+
          '</div>'+
        '</div>';
      }).join('');
  } else {
    personasEl.style.display='none';
    personasEl.innerHTML='';
  }
  // Tips
  const tips=[
    'Use <strong>admin@ABSx62256373.onmicrosoft.com</strong> for all M365 Copilot premium demos',
    'Use <strong>SashaO@ABSx62256373.onmicrosoft.com</strong> for Copilot Chat Free demos',
    'Have the reference Excel/Word files open in the browser before demoing Copilot in that app',
    'For Notebook demos, use the <code>/file</code> syntax to reference each source file',
    'For Teams demos, use the demo tenant\'s recorded meetings (New Software Implementation, Potential Merger, Negotiating Marketing Contract)'
  ];
  document.getElementById('detail-tips').innerHTML=
    '<div class="tips-title" style="color:#FFFFFF">⚡ Demo Tips</div>'+
    tips.map((t,i)=>'<div class="tip-item"><div class="tip-num">'+(i+1)+'</div><div>'+t+'</div></div>').join('');
  // Sidebar highlight
  document.querySelectorAll('.sidebar-item').forEach(el=>el.classList.remove('active'));
  const navEl=document.getElementById('nav-'+id);
  if(navEl)navEl.classList.add('active');
  setSidebarTab(tab);
  // Show detail
  document.getElementById('home-view').style.display='none';
  const dv=document.getElementById('detail-view');
  dv.classList.add('active'); dv.style.display='block';
  window.scrollTo({top:0,behavior:'smooth'});
}

function setDetailTab(t){
  _detailTab=t;
  if(_currentItem) showItem(_currentItem,_currentTab);
}

function escapeAttr(s){return String(s||'').replace(/"/g,'&quot;').replace(/'/g,'&#39;')}

function toggleTool(key){
  const hdr=document.getElementById('tool-hdr-'+key);
  const prm=document.getElementById('tool-prm-'+key);
  if(!hdr||!prm)return;
  const isOpen=hdr.classList.contains('open');
  hdr.classList.toggle('open',!isOpen);
  prm.classList.toggle('open',!isOpen);
}

function goHome(){
  document.getElementById('home-view').style.display='block';
  const dv=document.getElementById('detail-view');
  dv.classList.remove('active'); dv.style.display='none';
  // Restore grid tab state
  document.querySelectorAll('.sidebar-item').forEach(el=>el.classList.remove('active'));
  if(currentGridTab==='dept'){
    document.getElementById('nav-all-dept').classList.add('active');
    setSidebarTab('dept');
  } else {
    document.getElementById('nav-all-ind').classList.add('active');
    setSidebarTab('ind');
  }
  window.scrollTo({top:0,behavior:'smooth'});
}

const _PM={};
function _pmKey(indId,ti,pi){return indId+'_'+ti+'_'+pi;}
function copyById(key){
  const text=_PM[key]||'';
  navigator.clipboard.writeText(text).then(()=>{
    const t=document.getElementById('toast');
    t.classList.add('show');
    setTimeout(()=>t.classList.remove('show'),2500);
  });
}
function escapeHTML(s){
  if(!s)return '';
  return String(s).replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;').replace(/"/g,'&quot;');
}
function logout(){
  sessionStorage.removeItem('hub_auth');
  window.location.href='index.html';
}

// ── Init ──
buildSidebar();
buildDeptSidebar();
buildGrid();
buildDeptGrid();
buildWhatsNew();
</script>
</body>
</html>"""

with open('hub.html','w',encoding='utf-8') as f:
    f.write(HTML)

import os
sz=os.path.getsize('hub.html')
print(f"hub.html written: {sz:,} bytes")
