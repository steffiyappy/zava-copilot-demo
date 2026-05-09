
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
  width:var(--sidebar);background:rgba(255,255,255,0.92);backdrop-filter:saturate(140%) blur(8px);-webkit-backdrop-filter:saturate(140%) blur(8px);border-right:1px solid var(--border);
  position:sticky;top:56px;height:calc(100vh - 56px);overflow-y:auto;flex-shrink:0;display:flex;flex-direction:column;
}
.sidebar-tabs{display:flex;border-bottom:2px solid var(--border);flex-shrink:0}
.sidebar-tab{flex:1;padding:12px 0;text-align:center;font-size:12px;font-weight:700;cursor:pointer;color:var(--muted);border-bottom:2px solid transparent;margin-bottom:-2px;transition:all 0.2s}
.sidebar-tab.active{color:var(--blue);border-bottom-color:var(--blue);position:relative}
.sidebar-tab.active::after{content:'';position:absolute;left:20%;right:20%;bottom:-2px;height:2px;background:linear-gradient(90deg,transparent,var(--blue),transparent);animation:slideUnderline 0.3s ease}
@keyframes slideUnderline{from{transform:scaleX(0);opacity:0}to{transform:scaleX(1);opacity:1}}
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
/* WHATS NEW — fixed-height carousel so content below never shifts */
.whats-new{
  background:linear-gradient(135deg,#0F1C3F,#1F2D55 60%,#0078D4);
  border-radius:16px;padding:20px 24px;margin-bottom:24px;
  display:flex;align-items:center;gap:16px;overflow:hidden;position:relative;
  height:140px;min-height:140px;max-height:140px;
}
.whats-new::before{content:'';position:absolute;right:-40px;top:-40px;width:200px;height:200px;border-radius:50%;background:rgba(0,168,168,0.15);pointer-events:none;z-index:0}
.wn-icon{font-size:28px;flex-shrink:0;position:relative;z-index:2}
.wn-content{flex:1;min-width:0;position:relative;z-index:2;display:flex;flex-direction:column;justify-content:center;height:100%;overflow:hidden}
.wn-tag{display:inline-block;background:rgba(0,168,168,0.2);border:1px solid rgba(0,168,168,0.4);border-radius:20px;padding:2px 10px;color:#00A8A8;font-size:10px;font-weight:700;text-transform:uppercase;letter-spacing:0.8px;margin-bottom:6px;align-self:flex-start;flex-shrink:0}
.wn-title{color:#FFFFFF;font-size:15px;font-weight:700;margin-bottom:3px;flex-shrink:0;display:-webkit-box;-webkit-line-clamp:1;-webkit-box-orient:vertical;overflow:hidden}
.wn-desc{color:rgba(255,255,255,0.7);font-size:12px;line-height:1.45;display:-webkit-box;-webkit-line-clamp:2;-webkit-box-orient:vertical;overflow:hidden;flex:1;min-height:0}
.wn-meta{display:flex;align-items:center;gap:10px;margin-top:6px;flex-shrink:0}
.wn-link{color:#7DD3FC;font-size:11px;font-weight:600;text-decoration:none;display:inline-flex;align-items:center;gap:4px}
.wn-link:hover{color:#FFFFFF;text-decoration:underline}
.wn-nav{display:flex;gap:6px;flex-shrink:0;position:relative;z-index:5}
.wn-btn{background:rgba(255,255,255,0.12);border:1px solid rgba(255,255,255,0.25);border-radius:8px;padding:6px 12px;color:rgba(255,255,255,0.85);cursor:pointer;font-size:16px;line-height:1;transition:all 0.2s;font-family:inherit;position:relative;z-index:5}
.wn-btn:hover{background:rgba(255,255,255,0.25);color:#FFFFFF;transform:scale(1.05)}
.wn-btn:active{transform:scale(0.95)}
.wn-dots{display:flex;gap:5px;align-items:center;margin-top:0;position:relative;z-index:2}
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
.tool-prompts{display:none;border:1px solid var(--blue);border-top:none;border-bottom-left-radius:10px;border-bottom-right-radius:10px;overflow:hidden;background:#FFFFFF}
.tool-prompts.open{display:block}
.prompt-item{padding:14px 16px 12px;border-bottom:1px solid #F1F5F9;transition:background 0.15s;position:relative}
.prompt-item:last-child{border-bottom:none}
.prompt-item:hover{background:#F8FAFC}
.prompt-title{font-size:12px;font-weight:700;color:var(--navy);margin-bottom:8px;display:flex;align-items:center;gap:8px;flex-wrap:wrap}
/* INSTR panel — sits ABOVE the copyable prompt; not copyable */
.prompt-instr{font-size:11.5px;color:#475569;line-height:1.6;background:#F8FAFC;border:1px solid #E2E8F0;border-left:3px solid #94A3B8;padding:9px 12px;border-radius:0 6px 6px 0;margin:4px 0 8px;white-space:pre-wrap}
.prompt-instr-label{font-size:9.5px;font-weight:800;color:#475569;text-transform:uppercase;letter-spacing:1px;margin-bottom:4px;display:flex;align-items:center;gap:5px}
.prompt-text{font-size:12px;color:#1A1A2E;line-height:1.7;white-space:pre-wrap;background:#EEF4FF;border-left:3px solid #0078D4;padding:11px 13px;border-radius:0 8px 8px 0;margin:6px 0 8px;font-weight:500}
.prompt-text-label{font-size:9.5px;font-weight:800;color:#0078D4;text-transform:uppercase;letter-spacing:1px;margin-bottom:4px;display:flex;align-items:center;gap:5px}
/* Copy button — flow-positioned BELOW the prompt (no longer overlapping text) */
.prompt-actions{display:flex;justify-content:flex-end;align-items:center;gap:8px;margin-top:6px}
.copy-btn{
  background:var(--blue);color:#FFFFFF;border:none;border-radius:6px;
  padding:6px 14px;font-size:11px;font-weight:700;cursor:pointer;
  transition:all 0.2s;font-family:inherit;display:inline-flex;align-items:center;gap:5px;
}
.copy-btn:hover{background:#005EA6;transform:translateY(-1px);box-shadow:0 3px 8px rgba(0,120,212,0.3)}
.copy-btn:active{transform:translateY(0)}
.copy-btn:focus-visible{outline:3px solid rgba(0,120,212,0.4);outline-offset:2px}
/* Cowork actions list (5 numbered parallel sub-tasks on separate lines) */
.cowork-actions{background:linear-gradient(135deg,#FFF7ED,#FFEDD5);border:1px solid #FED7AA;border-radius:8px;padding:10px 14px;margin:0 0 10px}
.cowork-actions-label{font-size:9.5px;font-weight:800;color:#9A3412;text-transform:uppercase;letter-spacing:1px;margin-bottom:6px;display:flex;align-items:center;gap:5px}
.cowork-action-line{display:flex;align-items:flex-start;gap:9px;padding:6px 0;border-top:1px dashed rgba(154,52,18,0.18);font-size:12px;color:#451A03;line-height:1.55}
.cowork-action-line:first-of-type{border-top:none;padding-top:2px}
.cowork-action-num{font-weight:800;color:#9A3412;flex-shrink:0;min-width:18px}
.cowork-action-icon{font-size:14px;flex-shrink:0;line-height:1.4}
.cowork-action-text{flex:1;min-width:0}
/* Notebook special block (sources + Instructions field) */
.notebook-meta{background:linear-gradient(135deg,#F0F9FF,#E0F2FE);border:1px solid #BAE6FD;border-radius:8px;padding:11px 14px;margin:0 0 10px}
.notebook-meta-label{font-size:9.5px;font-weight:800;color:#075985;text-transform:uppercase;letter-spacing:1px;margin-bottom:6px;display:flex;align-items:center;gap:5px}
.notebook-sources{display:flex;flex-wrap:wrap;gap:5px;margin-bottom:8px}
.notebook-source-pill{background:#FFFFFF;border:1px solid #BAE6FD;border-radius:14px;padding:3px 10px;font-size:10.5px;color:#075985;font-weight:600;display:inline-flex;align-items:center;gap:4px}
.notebook-instr-row{font-size:11.5px;color:#0C4A6E;line-height:1.55;background:rgba(255,255,255,0.6);border-radius:6px;padding:8px 10px;margin-top:4px;border-left:2px solid #0EA5E9}
.notebook-instr-row strong{color:#075985}
/* Fluent polish — focus rings, hover lift, smooth motion */
.ind-card,.dept-pill,.sb-task,.sb-ex,.tool-header,.tool-prompts,.copy-btn{transition:all 0.18s cubic-bezier(.2,.8,.2,1)}
.ind-card:focus-visible,.dept-pill:focus-visible,.sb-task:focus-visible,.tool-header:focus-visible{outline:3px solid rgba(0,120,212,0.45);outline-offset:2px;border-color:var(--blue)}
.tool-header:active{transform:scale(0.995)}
.sb-ex{transition:transform 0.2s ease,box-shadow 0.2s ease}
.sb-ex:hover{transform:translateX(2px);box-shadow:-3px 0 0 var(--blue)}
/* Persona avatar gradient by name */
.persona-avatar{background:linear-gradient(135deg,#3B82F6,#1E40AF)}
/* Section header above tools (groups Agent Builder under M365 Copilot Tools) */
.tool-group-header{font-size:11px;font-weight:800;text-transform:uppercase;letter-spacing:1.2px;color:var(--muted);margin:18px 0 8px;padding:0 4px;display:flex;align-items:center;gap:8px}
.tool-group-header::after{content:'';flex:1;height:1px;background:var(--border)}
.tool-group-header:first-child{margin-top:0}
/* Language toggle (replaces MY/ID toggle) */
.lang-toggle{display:flex;background:rgba(255,255,255,0.08);border:1px solid rgba(255,255,255,0.15);border-radius:8px;overflow:hidden;flex-shrink:0}
.lang-btn{padding:5px 12px;border:none;background:transparent;color:rgba(255,255,255,0.6);font-size:12px;font-weight:700;cursor:pointer;transition:all 0.2s;font-family:inherit}
.lang-btn.active{background:rgba(255,255,255,0.18);color:#FFFFFF}
.lang-btn:hover:not(.active){color:rgba(255,255,255,0.85)}
.lang-btn:disabled{opacity:0.35;cursor:not-allowed}
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
    <span class="topbar-badge" id="topbar-badge">Loading…</span>
  </div>
  <div class="topbar-right">
    <div class="lang-toggle" id="lang-toggle">
      <button class="lang-btn active" id="lang-en" onclick="setLang('EN')" title="English (Malaysia &amp; Indonesia)">&#127474;&#127486;&#127470;&#127465; EN</button>
      <button class="lang-btn" id="lang-id" onclick="setLang('ID')" title="Bahasa Indonesia">&#127470;&#127465; BI</button>
      <button class="lang-btn" id="lang-bm" onclick="setLang('BM')" title="Bahasa Malaysia">&#127474;&#127486; BM</button>
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
let _lang='EN'; // 'EN' | 'ID' | 'BM'
let _detailTab='tools'; // 'tools' or 'chat'
let _currentTab='ind'; // 'ind' or 'dept' (which type was last shown)
const data=window.HUB_DATA;

function setLang(L){
  // Disable BM pill if current entry is geo='ID' (BM doesn't apply to Indonesia entries)
  // Disable ID pill if current entry is geo='MY' AND has no promptsID anywhere (rare).
  // For now we let the user pick freely; renderer falls back to EN if no translation.
  _lang=L;
  ['EN','ID','BM'].forEach(x=>{
    const el=document.getElementById('lang-'+x.toLowerCase());
    if(el) el.classList.toggle('active',x===L);
  });
  buildGrid(); buildDeptGrid(); buildSidebar(); buildDeptSidebar();
  if(_currentItem && document.getElementById('detail-view').style.display!=='none'){
    showItem(_currentItem,_currentTab);
  }
}
// Backward-compat alias (in case old onclick="setCtx('ID')" inline handlers leaked into data)
function setCtx(c){ setLang(c==='ID'?'ID':'EN'); }

function _pickLangField(item, base){
  // base = 'company' | 'tagline' | 'scenario' (without language suffix)
  const id=item[base+'ID'];
  const bm=item[base+'BM'];
  if(_lang==='ID' && id) return id;
  if(_lang==='BM' && bm) return bm;
  return item[base];
}
function _getCompany(item){return _pickLangField(item,'company');}
function _getTagline(item){return _pickLangField(item,'tagline');}
function _getScenario(item){return _pickLangField(item,'scenario');}
function _getPrompts(t){
  if(_lang==='ID' && t.promptsID && t.promptsID.length) return t.promptsID;
  if(_lang==='BM' && t.promptsBM && t.promptsBM.length) return t.promptsBM;
  return t.prompts||[];
}
function _getPersona(t,pi){
  const arr=_lang==='ID'&&t.personaID&&t.personaID.length?t.personaID:(t.persona||[]);
  return arr[pi]||'';
}
function _isResearcher(name){return /Researcher/i.test(name||'')}
function _isCowork(name){return /Cowork/i.test(name||'')}
function _isNotebook(name){return /Notebook/i.test(name||'')}
function _isChat(name){return /Copilot Chat/i.test(name||'')&&!/Notebook/i.test(name||'')}
function _isWordAgt(name){return /Word\s*Agent/i.test(name||'')}
function _isPptAgt(name){return /(PowerPoint|PPT)\s*Agent/i.test(name||'')}
function _isXlAgt(name){return /Excel\s*Agent/i.test(name||'')}
function _isBuilder(name){return /Agent\s*Builder/i.test(name||'')}
// Tools that live in the Copilot Chat tab (chat-based continuous-motion flow per IHH HR ref)
function _isChatTab(name){return _isChat(name)||_isWordAgt(name)||_isPptAgt(name)||_isXlAgt(name)||_isBuilder(name);}
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

// Strip leading emoji + whitespace from a display name (#9/#10 — defence in depth)
const _EMOJI_PREFIX_RE=/^[\p{Extended_Pictographic}\u{1F1E6}-\u{1F1FF}\u{2600}-\u{27BF}\u{2300}-\u{23FF}\u{2B00}-\u{2BFF}]+\s*/u;
function _stripLeadingEmoji(s){return String(s||'').replace(_EMOJI_PREFIX_RE,'').trim();}

// Default instructions per tool when the prompt object's `instr` field is empty.
// These match the per-tool contract committed in the v3 plan.
function _defaultInstr(tool, pi, item){
  const name=String(tool.tool||'');
  const acct=tool.account?(' Sign in with '+tool.account+'.'):'';
  if(_isResearcher(name)){
    const mode=pi===0?'**Critique Mode**':'**Model Council**';
    return 'Open `m365.cloud.microsoft/chat`.'+acct+' Click the **Agents** tab in the left rail → choose **Researcher**. Switch the mode pill to '+mode+'. Paste the prompt below.';
  }
  if(/Analyst/i.test(name)){
    return 'Open `m365.cloud.microsoft/chat`.'+acct+' Click the **Agents** tab → choose **Analyst**. **Upload** the reference file(s) listed in this entry from the right-hand sidebar. Then paste the prompt below — Analyst writes Python, runs it, and returns charts + tables.';
  }
  if(/Copilot in Excel/i.test(name)){
    return 'Open the relevant `.xlsx` file from the right-hand sidebar in **Excel for the Web**.'+acct+' Open the **Copilot pane** (top-right Copilot icon). Paste the prompt below.';
  }
  if(/Copilot in Word/i.test(name)){
    return 'Open the relevant `.docx` file from the right-hand sidebar in **Word for the Web**.'+acct+' Open the **Copilot pane** (top-right Copilot icon). Paste the prompt below.';
  }
  if(/Copilot in PowerPoint/i.test(name)){
    return 'Open the relevant `.pptx` file from the right-hand sidebar in **PowerPoint for the Web**.'+acct+' Open the **Copilot pane** (top-right Copilot icon). Paste the prompt below.';
  }
  if(/Outlook/i.test(name)){
    return 'Open **Outlook on the web**.'+acct+' Open the relevant email/thread referenced in the prompt. Click **Copilot** in the ribbon → choose **Summarise / Draft / Coach**. Paste the prompt below.';
  }
  if(/Teams/i.test(name)){
    return 'In **Teams calendar**, open the past meeting referenced in the prompt. The **Recap** page opens. Click the **Copilot icon** (top-right). Paste the prompt below. Copy the answer into a new Word doc when done.';
  }
  if(_isNotebook(name)){
    return 'Open `m365.cloud.microsoft/chat` → **Notebook** tab → **+ New Notebook**.'+acct+' Add ALL files listed in the Notebook setup block above as sources at creation time. Paste the **Instructions field** (system prompt) shown above. Then run this prompt.';
  }
  if(_isCowork(name)){
    return 'Open `m365.cloud.microsoft` → left-rail **Agents** → **Cowork**. (Frontier Program required.) Paste the prompt — Cowork delegates the 5 numbered actions in parallel and reports back when each is done.';
  }
  if(_isWordAgt(name)){
    return 'Open `m365.cloud.microsoft/chat`.'+acct+' Type the prompt below directly into chat — Copilot returns a fully drafted **`.docx`** saved to OneDrive. **Do NOT open Word first.**';
  }
  if(_isPptAgt(name)){
    return 'Open `m365.cloud.microsoft/chat`.'+acct+' Type the prompt below directly into chat — Copilot returns a fully drafted **`.pptx`** saved to OneDrive. **Do NOT open PowerPoint first.**';
  }
  if(_isXlAgt(name)){
    return 'Open `m365.cloud.microsoft/chat`.'+acct+' Type the prompt below directly into chat — Copilot returns a fully built **`.xlsx`** saved to OneDrive. **Do NOT open Excel first.**';
  }
  if(_isBuilder(name)){
    if(pi===0) return 'Open `m365.cloud.microsoft/chat` → **Agents** → **+ Create an agent**.'+acct+' Step 1 (**Describe**): paste this prompt into the description field — Copilot drafts the agent\'s name, instructions, and starter prompts.';
    if(pi===1) return 'Step 2 (**Configure**): paste this prompt as the **Instructions** field. Then click **Knowledge** → **Add** → upload the reference files listed in the right sidebar. Click **Capabilities** → enable **Web search** + **Code interpreter**.';
    if(pi===2) return 'Step 3 (**Test**): paste this prompt into the right-hand test pane. Verify the agent grounds its answer in the uploaded files and cites them.';
    return 'Step 4 (**Create + Share**): click **Create**, then **Share** → add Group ExCo distribution list with **Use** access. Done.';
  }
  if(_isChat(name)){
    return 'Open `m365.cloud.microsoft/chat`.'+acct+' Type the prompt below directly into chat.';
  }
  return 'Open the tool listed above in M365.'+acct+' Paste the prompt below.';
}

// Parse a Cowork prompt body for numbered action markers and return {n, icon, text} per line.
// Supports both line-separated ("1. Draft …\n2. Send …") and inline ("(1) draft …; (2) send …") formats.
function _parseCoworkActions(text){
  const T=String(text||'');
  // Marker = optional "(", digits, then ")" or ".", followed by whitespace.
  // Anchored to start-of-string OR preceded by whitespace/semicolon/comma to avoid false hits inside words.
  const RE=/(?:^|[\s;,])\(?(\d+)[\.\)]\s+/g;
  const positions=[];
  let m;
  while((m=RE.exec(T))!==null){
    positions.push({n:m[1], start: m.index + m[0].length, markerStart: m.index});
  }
  if(positions.length<2) return [];
  const out=[];
  for(let i=0;i<positions.length;i++){
    const start=positions[i].start;
    const end=i+1<positions.length?positions[i+1].markerStart:T.length;
    let body=T.slice(start,end).trim();
    body=body.replace(/[;,]\s*$/,'').trim();
    if(!body) continue;
    let icon='⚡';
    if(/draft.+(word|doc|brief|memo|paper|note)/i.test(body)||/word\s+doc/i.test(body)) icon='📝';
    else if(/(send|draft).+(email|mail)/i.test(body)||/email\s+to/i.test(body)) icon='✉️';
    else if(/(schedule|book|set\s+up|create).+(meeting|cal|calendar)/i.test(body)||/calendar\s+invite/i.test(body)) icon='📅';
    else if(/(post|message).+(teams|chat|channel)/i.test(body)||/teams\s+(message|post|channel)/i.test(body)) icon='💬';
    else if(/(deck|slide|powerpoint|pptx|presentation)/i.test(body)) icon='🖼';
    else if(/(spreadsheet|excel|xlsx|workbook|model)/i.test(body)) icon='📊';
    else if(/(plan|task|todo|to-do)/i.test(body)) icon='✅';
    out.push({n:positions[i].n, icon, text:body});
  }
  return out;
}

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
      a.innerHTML='<span class="ind-icon">'+ind.icon+'</span><span class="ind-name">'+_stripLeadingEmoji(ind.name)+'</span><span class="ind-count">'+count+'</span>';
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
    a.innerHTML='<span class="ind-icon">'+dept.icon+'</span><span class="ind-name">'+_stripLeadingEmoji(dept.name)+'</span><span class="ind-count">'+count+'</span>';
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
    '<div class="ind-card-name">'+_stripLeadingEmoji(item.name)+'</div>'+
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
  document.getElementById('detail-badge').textContent=isDept?'Department':_stripLeadingEmoji(item.name);
  document.getElementById('detail-title').textContent=_getCompany(item);
  document.getElementById('detail-company').textContent=_stripLeadingEmoji(item.name);
  document.getElementById('detail-tagline').textContent=_getTagline(item);
  // Scenario + dept pills
  const scenarioText=_getScenario(item);
  let pillsHtml='';
  if(item.relevantDepts && item.relevantDepts.length){
    const pills=item.relevantDepts.map(did=>{
      const d=data.departments.find(x=>x.id===did);
      if(!d) return '';
      return '<span class="dept-pill" data-did="'+escapeAttr(d.id)+'">'+d.icon+' '+escapeHTML(_stripLeadingEmoji(d.name))+'</span>';
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
  const _phaseLabels=['🌅 MORNING','☀️ MIDDAY','🌤️ AFTERNOON','🌆 END OF DAY'];
  const _phaseLabelsID=['🌅 PAGI','☀️ SIANG','🌤️ SORE','🌆 AKHIR HARI'];
  const _phaseLabelsBM=['🌅 PAGI','☀️ TENGAH HARI','🌤️ PETANG','🌆 AKHIR HARI'];
  if(item.storyboard && item.storyboard.length){
    sbWrap.style.display='block';
    const phases=_lang==='ID'?_phaseLabelsID:(_lang==='BM'?_phaseLabelsBM:_phaseLabels);
    const heroTitle=_lang==='ID'?'📖 Sehari Bersama Persona':(_lang==='BM'?'📖 Sehari Bersama Persona':'📖 A Day in the Life');
    const heroSub=_lang==='ID'
      ?'Ikuti alur end-to-end ini seolah Anda menemani persona sepanjang hari. Klik tool di bawah untuk menyalin promptnya.'
      :(_lang==='BM'
        ?'Ikuti aliran hujung-ke-hujung ini seolah-olah anda menemani persona sepanjang hari. Klik alat di bawah untuk menyalin prompt.'
        :'Follow this end-to-end flow as if you are shadowing the persona through the day. Click a tool below to copy its prompts.');
    sbWrap.innerHTML=
      '<div class="storyboard-title">'+heroTitle+'</div>'+
      '<div class="storyboard-sub">'+heroSub+'</div>'+
      '<div class="sb-exercises">'+
      item.storyboard.map((ex,i)=>{
        const exTitle=_lang==='ID'&&ex.titleID?ex.titleID:(_lang==='BM'&&ex.titleBM?ex.titleBM:ex.title);
        const exSummary=_lang==='ID'&&ex.summaryID?ex.summaryID:(_lang==='BM'&&ex.summaryBM?ex.summaryBM:(ex.summary||''));
        const phase=phases[i] || phases[phases.length-1];
        const tasks=(ex.tasks||[]).map(t=>{
          const verb=_lang==='ID'&&t.verbID?t.verbID:(_lang==='BM'&&t.verbBM?t.verbBM:t.verb);
          return '<span class="sb-task" data-tool="'+escapeAttr(t.tool||'')+'">'+
            '<span class="sb-task-n">'+escapeHTML(t.n||'')+'</span>'+
            '<span class="sb-task-verb">'+escapeHTML(verb||'')+'</span>'+
            '</span>';
        }).join('');
        return '<div class="sb-ex">'+
          '<div class="sb-ex-head">'+
            '<span class="sb-ex-num">'+phase+'</span>'+
            '<span class="sb-ex-title">'+escapeHTML(exTitle||'')+'</span>'+
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
  // Tab toggle (Tools vs Chat).
  // Chat tab = T_CHAT + Word/PPT/Excel Agents + Agent Builder (continuous-motion chat-based flow per IHH HR ref).
  // Tools tab = everything else (Researcher, Analyst, Excel/Word/PPT in-app, Outlook, Teams, Notebook, Cowork).
  const hasChat=item.prompts.some(t=>_isChatTab(t.tool));
  const hasOther=item.prompts.some(t=>!_isChatTab(t.tool));
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
    if(_detailTab==='chat') return _isChatTab(t.tool);
    return !_isChatTab(t.tool);
  });
  // Prompts
  const pEl=document.getElementById('detail-prompts');
  pEl.innerHTML='';
  let _lastGroup=null;
  visibleTools.forEach((tool)=>{
    const ti=item.prompts.indexOf(tool);
    const isBasic=tool.license&&(tool.license.toLowerCase().includes('basic')||tool.license.toLowerCase().includes('free'));
    const isFront=_isFrontier(tool.license);
    const isResearcher=_isResearcher(tool.tool);
    const isCowork=_isCowork(tool.tool);
    const isNotebook=_isNotebook(tool.tool);
    // Optional group header — only inside the Chat tab to delineate "Free Chat" vs "M365 Copilot — chat-based agents"
    if(_detailTab==='chat'){
      const grp=_isChat(tool.tool)?'free':'agents';
      if(grp!==_lastGroup){
        const hdr=document.createElement('div');
        hdr.className='tool-group-header';
        hdr.innerHTML=grp==='free'
          ?'🆓 Copilot Chat — broader use cases (no license required)'
          :'✨ M365 Copilot — chat-based continuous-motion flow (Word Agent → PPT Agent → Excel Agent → Agent Builder)';
        pEl.appendChild(hdr);
        _lastGroup=grp;
      }
    }
    const sec=document.createElement('div'); sec.className='tool-section';
    const promptArr=_getPrompts(tool);
    const promHtml=promptArr.map((p,pi)=>{
      const key=_pmKey(id,ti,pi);
      const txt=typeof p==='string'?p:(p.prompt||'');
      const instrTxt=(typeof p==='object'&&p&&p.instr)?p.instr:_defaultInstr(tool,pi,item);
      _PM[key]=txt;
      let modeLbl='';
      if(isResearcher){
        modeLbl=pi===0
          ?'<span class="prompt-mode">🔍 Critique Mode</span>'
          :'<span class="prompt-mode">⚖️ Model Council</span>';
      }
      // Cowork special render: parse the prompt body for "1. " / "2. " etc. action lines and split each onto its own line.
      let coworkHtml='';
      if(isCowork){
        const lines=_parseCoworkActions(txt);
        if(lines.length>=2){
          coworkHtml=
            '<div class="cowork-actions">'+
            '<div class="cowork-actions-label">⚡ Cowork delegates these in parallel</div>'+
            lines.map(L=>{
              return '<div class="cowork-action-line">'+
                '<span class="cowork-action-num">'+escapeHTML(L.n)+'.</span>'+
                '<span class="cowork-action-icon">'+L.icon+'</span>'+
                '<span class="cowork-action-text">'+escapeHTML(L.text)+'</span>'+
              '</div>';
            }).join('')+
            '</div>';
        }
      }
      // Notebook special render: surface sources + Instructions field above the numbered prompts.
      // We only add this once, on prompt 0 (so it doesn't repeat per prompt).
      let notebookHtml='';
      if(isNotebook && pi===0 && tool.notebookMeta){
        const nm=tool.notebookMeta;
        const srcs=(nm.sources||[]).map(s=>'<span class="notebook-source-pill">'+escapeHTML(s)+'</span>').join('');
        const instr=_lang==='ID'&&nm.instructionsID?nm.instructionsID:(_lang==='BM'&&nm.instructionsBM?nm.instructionsBM:(nm.instructions||''));
        notebookHtml=
          '<div class="notebook-meta">'+
          '<div class="notebook-meta-label">📓 Notebook setup — add ALL sources at creation time, then set the Instructions field</div>'+
          (srcs?'<div class="notebook-sources">'+srcs+'</div>':'')+
          (instr?'<div class="notebook-instr-row"><strong>Instructions field (system prompt):</strong> '+escapeHTML(instr)+'</div>':'')+
          '</div>';
      }
      // The instr block above the prompt body is suppressed for Cowork (the actions block IS the instr context)
      const showInstr=instrTxt && !isCowork;
      return '<div class="prompt-item">'+
        '<div class="prompt-title">'+modeLbl+'💬 Prompt '+(pi+1)+'</div>'+
        (notebookHtml)+
        (showInstr
          ? '<div class="prompt-instr-label">📋 Instructions</div>'+
            '<div class="prompt-instr">'+escapeHTML(instrTxt)+'</div>'
          : '')+
        coworkHtml+
        '<div class="prompt-text-label">💬 Prompt — copy this</div>'+
        '<div class="prompt-text">'+escapeHTML(txt)+'</div>'+
        '<div class="prompt-actions">'+
          '<button class="copy-btn" onclick="copyById(\''+key+'\')">📋 Copy prompt</button>'+
        '</div>'+
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
        '<strong>⚖️ Model Council</strong> — Researcher runs GPT-5.5 Thinking and Claude Opus 4.7 in parallel against the brief and returns both reports plus a synthesis cover letter highlighting agreements, disagreements and unique findings. Best for high-stakes decisions where you want diverse expert input.'+
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
        const role=_lang==='ID'&&p.roleID?p.roleID:(_lang==='BM'&&p.roleBM?p.roleBM:p.role);
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
    'For Notebook demos, click <strong>+ Sources</strong> in the right rail and upload each file from OneDrive — the notebook grounds answers on those sources automatically (no <code>/file</code> tag needed in the prompt body)',
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
(function(){
  const tb=document.getElementById('topbar-badge');
  if(tb) tb.textContent=data.industries.length+' Industries · '+data.departments.length+' Departments';
  const stIndCount=document.getElementById('total-ind-count');
  if(stIndCount) stIndCount.textContent=data.industries.length;
  const stDeptCount=document.getElementById('total-dept-count');
  if(stDeptCount) stDeptCount.textContent=data.departments.length;
  // Update home-page stat chips
  document.querySelectorAll('.stat-chip').forEach(c=>{
    const lbl=c.querySelector('.lbl'); const val=c.querySelector('.val');
    if(!lbl||!val) return;
    if(/Industries/i.test(lbl.textContent)) val.textContent=data.industries.length;
    if(/Departments/i.test(lbl.textContent)) val.textContent=data.departments.length;
  });
  // Update home-page grid-tab labels
  const gtI=document.getElementById('gtab-ind'); if(gtI) gtI.innerHTML='&#127981; Industries ('+data.industries.length+')';
  const gtD=document.getElementById('gtab-dept'); if(gtD) gtD.innerHTML='&#127970; Departments ('+data.departments.length+')';
})();
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
