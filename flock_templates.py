# flock_templates.py - COMPLETE REVISION v3
##############################################################################
# FlockIQ Poultry Farm Management System — Templates
##############################################################################

_BASE_STYLE = """
<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.0/css/all.min.css">
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap" rel="stylesheet">
<script src="https://cdn.jsdelivr.net/npm/chart.js@4.4.4/dist/chart.umd.min.js"></script>
<style>
:root {
  --bg: #fdfcfb; --sidebar-bg: #ffffff; --card-bg: #ffffff; --text: #1c1917;
  --muted: #78716c; --border: rgba(120, 113, 108, 0.12); --sidebar-hover: #f5f5f4;
  --sidebar-active-bg: #f0fdf4; --sidebar-active-text: #166534;
  --accent: #166534; --accent2: #854d0e; --green: #15803d; --blue: #1e40af;
  --red: #991b1b; --yellow: #a16207;
  --shadow: 0 1px 3px rgba(0,0,0,0.05), 0 4px 12px rgba(22, 101, 52, 0.04);
  --shadow-lg: 0 10px 25px rgba(22, 101, 52, 0.08);
}
html.dark {
  --bg: #0c0a09; --sidebar-bg: #1c1917; --card-bg: #292524; --text: #f5f5f4;
  --muted: #a8a29e; --border: rgba(255,255,255,0.08); --sidebar-hover: #292524;
  --sidebar-active-bg: #14532d; --sidebar-active-text: #bbf7d0;
  --shadow: 0 4px 20px rgba(0,0,0,0.4);
}
*, *::before, *::after { box-sizing: border-box; }
body { background: var(--bg); color: var(--text); font-family: 'Inter', sans-serif; margin: 0; min-height: 100vh; transition: background 0.25s, color 0.25s; }
.app-shell { display: flex; min-height: 100vh; }
.sidebar { width: 268px; flex-shrink: 0; background: var(--sidebar-bg); border-right: 1px solid var(--border); display: flex; flex-direction: column; position: sticky; top: 0; height: 100vh; overflow-y: auto; z-index: 100; transition: transform 0.3s cubic-bezier(.4,0,.2,1); }
.sidebar-brand { padding: 24px 20px 16px; border-bottom: 1px solid var(--border); display: flex; align-items: center; gap: 12px; }
.brand-icon { width: 40px; height: 40px; border-radius: 10px; background: linear-gradient(135deg, #166534, #15803d); display: flex; align-items: center; justify-content: center; color: #fff; font-size: 18px; flex-shrink: 0; }
.brand-text { font-family: 'Inter', sans-serif; font-size: 15px; font-weight: 800; line-height: 1.2; }
.brand-sub { font-size: 11px; color: var(--muted); font-weight: 500; }
.sidebar-nav { padding: 16px 12px; flex: 1; }
.nav-section-label { font-size: 10px; font-weight: 700; text-transform: uppercase; letter-spacing: 1.2px; color: var(--muted); padding: 12px 8px 6px; }
.nav-link { display: flex; align-items: center; gap: 10px; padding: 10px 12px; border-radius: 9px; margin-bottom: 2px; color: var(--text); font-size: 14px; font-weight: 500; text-decoration: none; transition: all 0.15s; cursor: pointer; }
.nav-link:hover { background: var(--sidebar-hover); color: var(--accent); }
.nav-link.active { background: var(--sidebar-active-bg); color: var(--sidebar-active-text); font-weight: 700; }
.nav-link i { width: 20px; text-align: center; font-size: 14px; }
.badge-count { margin-left: auto; background: #dc2626; color: #fff; font-size: 11px; font-weight: 700; padding: 1px 7px; border-radius: 999px; line-height: 1.6; }
.sidebar-footer { padding: 16px 12px; border-top: 1px solid var(--border); }
.logout-btn { display: flex; align-items: center; gap: 10px; padding: 10px 12px; border-radius: 9px; color: #991b1b; font-size: 14px; font-weight: 600; text-decoration: none; transition: all 0.15s; width: 100%; background: none; border: none; cursor: pointer; }
.logout-btn:hover { background: rgba(153, 27, 27, 0.08); color: #991b1b; }
.main-content { flex: 1; overflow-x: hidden; }
.topbar { background: var(--sidebar-bg); border-bottom: 1px solid var(--border); padding: 14px 28px; display: flex; justify-content: space-between; align-items: center; position: sticky; top: 0; z-index: 50; }
.topbar-title { font-family: 'Inter', sans-serif; font-size: 18px; font-weight: 800; color: var(--accent); }
.topbar-actions { display: flex; align-items: center; gap: 10px; }
.page-body { padding: 28px; }
.tab-content { display: none; }
.tab-content.active { display: block; animation: fadeIn 0.3s ease; }
@keyframes fadeIn { from { opacity: 0; transform: translateY(10px); } to { opacity: 1; transform: translateY(0); } }
.card { background: var(--card-bg); border: 1px solid var(--border); border-radius: 14px; box-shadow: var(--shadow); }
.card-header-custom { padding: 18px 22px 0; font-size: 15px; font-weight: 700; display: flex; align-items: center; justify-content: space-between; flex-wrap: wrap; gap: 10px; }
.card-body-custom { padding: 18px 22px; }
.stat-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 16px; }
.stat-card { border-radius: 14px; padding: 22px; color: #fff; position: relative; overflow: hidden; box-shadow: var(--shadow-lg); }
.stat-card .sc-label { font-size: 12px; font-weight: 600; text-transform: uppercase; letter-spacing: 0.8px; opacity: 0.9; }
.stat-card .sc-value { font-size: 32px; font-weight: 800; font-family: 'Inter', sans-serif; line-height: 1.1; margin-top: 6px; }
.stat-card .sc-icon { position: absolute; right: 18px; top: 18px; width: 48px; height: 48px; border-radius: 50%; background: rgba(255,255,255,0.2); display: flex; align-items: center; justify-content: center; font-size: 20px; }
.sc-farm-green { background: linear-gradient(135deg, #166534, #15803d); }
.sc-farm-earth { background: linear-gradient(135deg, #854d0e, #a16207); }
.sc-farm-olive { background: linear-gradient(135deg, #3f6212, #4d7c0f); }
.sc-farm-forest { background: linear-gradient(135deg, #064e3b, #065f46); }
.sc-farm-blue { background: linear-gradient(135deg, #1e3a8a, #1d4ed8); }
.sc-farm-red { background: linear-gradient(135deg, #7c2d12, #c2410c); }
.sc-farm-teal { background: linear-gradient(135deg, #0f766e, #14b8a6); }
.sc-farm-purple { background: linear-gradient(135deg, #5b21b6, #7c3aed); }
.table { --bs-table-bg: transparent; --bs-table-color: var(--text); }
.table > :not(caption) > * > * { background-color: transparent !important; color: var(--text) !important; border-color: var(--border) !important; }
.table thead th { font-size: 11px; text-transform: uppercase; letter-spacing: 0.8px; font-weight: 700; color: var(--muted); }
html.dark .table { border-color: var(--border); }
.badge-active { background: rgba(21, 128, 61, 0.12); color: #166534; border-radius: 20px; padding: 3px 10px; font-weight: 600; font-size: 12px; }
.badge-harvested { background: rgba(120, 113, 108, 0.12); color: #78716c; border-radius: 20px; padding: 3px 10px; font-weight: 600; font-size: 12px; }
.badge-success { background: rgba(21, 128, 61, 0.12); color: #166534; border-radius: 20px; padding: 3px 10px; font-weight: 600; font-size: 12px; }
.badge-warning { background: rgba(161, 98, 7, 0.12); color: #a16207; border-radius: 20px; padding: 3px 10px; font-weight: 600; font-size: 12px; }
.badge-danger { background: rgba(220, 38, 38, 0.12); color: #dc2626; border-radius: 20px; padding: 3px 10px; font-weight: 600; font-size: 12px; }
.badge-info { background: rgba(37, 99, 235, 0.12); color: #2563eb; border-radius: 20px; padding: 3px 10px; font-weight: 600; font-size: 12px; }
.status-pill { border-radius: 20px; padding: 3px 10px; font-weight: 700; font-size: 11px; text-transform: uppercase; letter-spacing: 0.4px; display: inline-flex; align-items: center; gap: 5px; }
.status-scheduled { background: rgba(161, 98, 7, 0.12); color: #a16207; }
.status-administered { background: rgba(21, 128, 61, 0.12); color: #166534; }
.status-missed, .status-skipped { background: rgba(220, 38, 38, 0.1); color: #dc2626; }
.status-paid { background: rgba(21, 128, 61, 0.12); color: #166534; }
.status-pending { background: rgba(161, 98, 7, 0.12); color: #a16207; }
.status-overdue { background: rgba(220, 38, 38, 0.12); color: #dc2626; }
.form-control, .form-select { background: var(--bg) !important; border: 1.5px solid var(--border) !important; color: var(--text) !important; border-radius: 9px !important; padding: 9px 13px !important; font-size: 14px !important; transition: border-color 0.15s; }
.form-control:focus, .form-select:focus { border-color: var(--accent) !important; box-shadow: 0 0 0 3px rgba(22, 101, 52, 0.1) !important; }
.form-label { font-size: 12px; font-weight: 700; text-transform: uppercase; letter-spacing: 0.6px; color: var(--muted); margin-bottom: 5px; }
.btn-farm { background: linear-gradient(135deg, #166534, #15803d); color: #fff; border: none; border-radius: 9px; font-weight: 700; font-size: 14px; padding: 9px 20px; transition: opacity 0.15s; }
.btn-farm:hover { opacity: 0.88; color: #fff; }
.btn-ghost { background: var(--sidebar-hover); color: var(--text); border: none; border-radius: 9px; font-weight: 600; font-size: 13px; padding: 8px 16px; }
.btn-ghost:hover { color: var(--text); opacity: 0.8; }
.btn-danger-custom { background: #dc2626; color: #fff; border: none; border-radius: 9px; font-weight: 600; font-size: 13px; padding: 8px 16px; }
.btn-danger-custom:hover { opacity: 0.85; color: #fff; }
.alert-flash { border-radius: 10px; font-size: 14px; font-weight: 500; border: none; }
.theme-toggle { width: 36px; height: 36px; border-radius: 9px; background: var(--sidebar-hover); border: none; color: var(--text); cursor: pointer; display: flex; align-items: center; justify-content: center; transition: all 0.15s; font-size: 14px; }
.theme-toggle:hover { background: var(--border); }
.role-badge { font-size: 10px; font-weight: 800; text-transform: uppercase; letter-spacing: 1px; padding: 3px 9px; border-radius: 20px; }
.role-owner { background: rgba(22, 101, 52, 0.1); color: #166534; }
.role-manager { background: rgba(37,99,235,0.12); color: #2563eb; }
.role-worker { background: rgba(22,163,74,0.12); color: #16a34a; }
.mobile-topbar { display: none; background: var(--sidebar-bg); border-bottom: 1px solid var(--border); padding: 14px 20px; align-items: center; justify-content: space-between; position: sticky; top: 0; z-index: 200; }
.mobile-overlay { display: none; position: fixed; inset: 0; background: rgba(0,0,0,0.5); z-index: 150; backdrop-filter: blur(2px); }
.mobile-overlay.show { display: block; }
@media (max-width: 991px) {
  .sidebar { position: fixed; left: 0; top: 0; height: 100%; transform: translateX(-100%); }
  .sidebar.show { transform: translateX(0); box-shadow: 4px 0 20px rgba(0,0,0,0.15); }
  .mobile-topbar { display: flex; }
  .topbar { display: none; }
  .page-body { padding: 18px; }
}
@media (max-width: 576px) {
  .stat-grid { grid-template-columns: 1fr 1fr; }
  .sc-value { font-size: 24px; }
}
.section-header { display: flex; align-items: center; gap: 10px; margin-bottom: 16px; }
.section-header h5 { font-family: 'Inter', sans-serif; font-size: 16px; font-weight: 800; margin: 0; }
.section-divider { width: 4px; height: 22px; border-radius: 3px; background: linear-gradient(to bottom, #166534, #15803d); }
.hero-banner { border-radius: 18px; background: linear-gradient(135deg, #166534 0%, #3f6212 100%); color: #fff; padding: 28px 32px; display: flex; justify-content: space-between; align-items: center; margin-bottom: 28px; position: relative; overflow: hidden; }
.hero-banner::after { content:''; position:absolute; right:-30px; top:-30px; width:180px; height:180px; border-radius:50%; background:rgba(255,255,255,0.08); }
.hero-banner::before { content:''; position:absolute; right:60px; bottom:-40px; width:120px; height:120px; border-radius:50%; background:rgba(255,255,255,0.06); }
.metric-pill { display:inline-flex; align-items:center; gap:6px; background:rgba(255,255,255,0.15); border-radius:20px; padding:4px 12px; font-size:13px; font-weight:600; }
.tbl-actions { display:flex; gap:6px; }
.btn-sm-icon { width:30px;height:30px;border-radius:7px;border:none;display:flex;align-items:center;justify-content:center;font-size:12px;cursor:pointer;transition:all 0.15s; }
.btn-edit { background:rgba(37,99,235,0.12); color:#2563eb; }
.btn-edit:hover { background:#2563eb; color:#fff; }
.btn-del { background:rgba(220,38,38,0.1); color:#dc2626; }
.btn-del:hover { background:#dc2626; color:#fff; }
.btn-ok { background:rgba(21,128,61,0.12); color:#166534; }
.btn-ok:hover { background:#166534; color:#fff; }
.btn-warn { background:rgba(161,98,7,0.12); color:#a16207; }
.btn-warn:hover { background:#a16207; color:#fff; }
.analytics-grid { display:grid; grid-template-columns:1fr 1fr; gap:16px; }
@media(max-width:768px){ .analytics-grid{grid-template-columns:1fr;} .hero-banner{flex-direction:column;gap:16px;text-align:center;} }
.input-table-section { overflow-x:auto; }
.schedule-list { display: flex; flex-direction: column; gap: 8px; }
.schedule-item { display: flex; align-items: center; gap: 12px; padding: 10px 14px; border-radius: 10px; background: var(--bg); border: 1px solid var(--border); }
.schedule-item .si-icon { width: 34px; height: 34px; border-radius: 9px; flex-shrink: 0; display: flex; align-items: center; justify-content: center; font-size: 13px; background: rgba(22,101,52,0.1); color: var(--accent); }
.schedule-item.overdue .si-icon { background: rgba(220,38,38,0.12); color: #dc2626; }
.si-body { flex: 1; min-width: 0; }
.si-title { font-size: 13px; font-weight: 700; }
.si-sub { font-size: 12px; color: var(--muted); }
.si-date { font-size: 12px; font-weight: 600; color: var(--muted); white-space: nowrap; }
.confirm-row { display: flex; justify-content: space-between; padding: 8px 0; border-bottom: 1px solid var(--border); font-size: 13px; }
.confirm-row:last-child { border-bottom: none; }
.confirm-row .label { color: var(--muted); font-weight: 600; }
.confirm-row .value { font-weight: 700; }
.chart-container { position: relative; height: 350px; width: 100%; }
.chart-container-sm { position: relative; height: 250px; width: 100%; }
.report-field-list { display: grid; grid-template-columns: repeat(auto-fill, minmax(200px, 1fr)); gap: 8px; }
.report-field-item { display: flex; align-items: center; gap: 8px; padding: 8px 12px; border-radius: 8px; background: var(--bg); border: 1px solid var(--border); font-size: 13px; cursor: pointer; }
.report-field-item:hover { background: var(--sidebar-hover); }
.report-field-item input[type="checkbox"] { cursor: pointer; }
.detail-panel { background: var(--bg); border-radius: 10px; padding: 16px; border: 1px solid var(--border); margin-top: 16px; }
.detail-grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(200px, 1fr)); gap: 12px; }
.detail-item { font-size: 13px; }
.detail-item .label { color: var(--muted); font-weight: 600; font-size: 11px; text-transform: uppercase; letter-spacing: 0.5px; }
.detail-item .value { font-weight: 700; }
.expense-card-icon { width: 40px; height: 40px; border-radius: 10px; display:flex; align-items:center; justify-content:center; font-size:16px; color:#fff; flex-shrink:0; }
</style>
"""

def logo_svg(size=40, opacity=1):
    return f'''<svg viewBox="0 0 100 100" xmlns="http://www.w3.org/2000/svg" width="{size}" height="{size}" style="opacity:{opacity};display:block;">
  <ellipse cx="50" cy="66" rx="34" ry="28" fill="#FFCF3F"/>
  <circle cx="50" cy="34" r="23" fill="#FFDD5C"/>
  <path d="M50 34 L74 39 L50 46 Z" fill="#FF8A3D"/>
  <circle cx="43" cy="29" r="4" fill="#2B2118"/>
  <circle cx="57" cy="29" r="4" fill="#2B2118"/>
  <path d="M18 16 Q28 6 37 18 Q27 20 18 16 Z" fill="#FFB03F"/>
  <path d="M63 18 Q72 6 82 16 Q73 20 63 18 Z" fill="#FFB03F"/>
  <path d="M22 62 Q10 66 14 78 Q24 74 26 64 Z" fill="#FFDD5C"/>
</svg>'''

_BASE_SCRIPT = """
<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
<script>
(function(){
  const t = localStorage.getItem("theme");
  if(t === "dark") document.documentElement.classList.add("dark");
})();
function toggleDark(){
  document.documentElement.classList.toggle("dark");
  localStorage.setItem("theme", document.documentElement.classList.contains("dark") ? "dark" : "light");
  const el = document.getElementById("themeIcon");
  if (el) el.className = document.documentElement.classList.contains("dark") ? "fas fa-sun" : "fas fa-moon";
}
function toggleSidebar(){
  document.getElementById("sidebar").classList.toggle("show");
  document.getElementById("mobileOverlay").classList.toggle("show");
}
function showTab(tabId, element) {
    document.querySelectorAll('.tab-content').forEach(tab => { tab.classList.remove('active'); });
    document.querySelectorAll('.nav-link').forEach(link => { link.classList.remove('active'); });
    var activeTab = document.getElementById(tabId);
    activeTab.classList.add('active');
    element.classList.add('active');
    if (window.innerWidth < 992) { toggleSidebar(); }
    if (window.Chart) {
        activeTab.querySelectorAll('canvas').forEach(function(canvas) {
            var chart = Chart.getChart(canvas);
            if (chart) { chart.resize(); }
        });
    }
}
setTimeout(()=>{ document.querySelectorAll(".alert-flash").forEach(a=>{ let b=bootstrap.Alert.getOrCreateInstance(a); b.close(); }); }, 4000);
</script>
"""

# ─────────────────────────────────────────────────────────────────────────────
# LOGIN (unchanged)
# ─────────────────────────────────────────────────────────────────────────────
TEMPLATE_LOGIN = """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Login — FlockIQ</title>
""" + _BASE_STYLE + """
<style>
body { display: flex; align-items: center; justify-content: center; min-height: 100vh;
  background: #fdfcfb; background-image: radial-gradient(circle at 2px 2px, rgba(22,101,52,0.05) 1px, transparent 0); background-size: 40px 40px; }
.auth-card { background: var(--card-bg); border-radius: 20px; box-shadow: var(--shadow-lg); padding: 40px 36px; width: 100%; max-width: 420px; border: 1px solid var(--border); }
.auth-logo { width: 56px; height: 56px; border-radius: 16px; background: linear-gradient(135deg,#166534,#15803d); display: flex; align-items: center; justify-content: center; color: #fff; font-size: 24px; margin: 0 auto 20px; }
.auth-title { font-family: 'Inter', sans-serif; font-size: 26px; font-weight: 800; text-align: center; margin-bottom: 4px; color: var(--accent); }
.auth-sub { text-align: center; color: var(--muted); font-size: 14px; margin-bottom: 28px; }
.input-group-custom { position: relative; margin-bottom: 14px; }
.input-group-custom .icon { position: absolute; left: 13px; top: 50%; transform: translateY(-50%); color: var(--muted); font-size: 14px; z-index: 1; }
.input-group-custom input { padding-left: 38px !important; }
.password-toggle { position: absolute; right: 14px; top: 50%; transform: translateY(-50%); cursor: pointer; color: var(--muted); z-index: 1; }
.password-toggle:hover { color: var(--text); }
</style>
</head>
<body>
<div class="auth-card">
  <div class="auth-logo">""" + logo_svg(30) + """</div>
  <div class="auth-title">FlockIQ</div>
  <div class="auth-sub">Poultry Farm Management System</div>

  {% with msgs = get_flashed_messages() %}{% if msgs %}
    {% for m in msgs %}
    <div class="alert alert-warning alert-dismissible fade show alert-flash" role="alert" style="font-size:13px;border-radius:9px;">
      <i class="fas fa-exclamation-circle me-2"></i>{{ m }}
      <button type="button" class="btn-close" data-bs-dismiss="alert"></button>
    </div>
    {% endfor %}
  {% endif %}{% endwith %}

  <form method="post">
    <div class="input-group-custom">
      <i class="icon fas fa-user"></i>
      <input type="text" name="username" class="form-control" placeholder="Username" required>
    </div>
    <div class="input-group-custom">
      <i class="icon fas fa-lock"></i>
      <input type="password" name="password" id="loginPw" class="form-control" placeholder="Password" required style="padding-right:40px;">
      <i class="fas fa-eye password-toggle" id="loginPwToggle" onclick="togglePassword()"></i>
    </div>
    <button type="submit" class="btn-farm w-100 mt-2" style="padding:12px;">Sign In</button>
  </form>

  <div class="text-center mt-4" style="font-size:13px; color: var(--muted);">
    Accounts are created by the Farm Owner. Contact your Owner if you need access.
  </div>
</div>
""" + _BASE_SCRIPT + """
<script>
function togglePassword() {
  const f = document.getElementById('loginPw');
  const toggle = document.getElementById('loginPwToggle');
  const show = f.type === 'password';
  f.type = show ? 'text' : 'password';
  toggle.className = show ? 'fas fa-eye-slash password-toggle' : 'fas fa-eye password-toggle';
}
</script>
</body></html>
"""

# ─────────────────────────────────────────────────────────────────────────────
# OWNER DASHBOARD — REVISED
# ─────────────────────────────────────────────────────────────────────────────
TEMPLATE_OWNER = """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Owner Dashboard — FlockIQ</title>
""" + _BASE_STYLE + """
</head>
<body>
<script>(function(){const t=localStorage.getItem("theme");if(t==="dark")document.documentElement.classList.add("dark");})()</script>
<div id="mobileOverlay" class="mobile-overlay" onclick="toggleSidebar()"></div>
<div class="mobile-topbar">
  <button onclick="toggleSidebar()" style="background:none;border:none;color:var(--text);font-size:20px;"><i class="fas fa-bars"></i></button>
  <span style="font-family:'Inter',sans-serif;font-weight:800;font-size:16px;">FlockIQ</span>
  <button class="theme-toggle" onclick="toggleDark()"><i class="fas fa-moon"></i></button>
</div>
<div class="app-shell">

<nav id="sidebar" class="sidebar">
  <div class="sidebar-brand">
    <div class="brand-icon">""" + logo_svg(22) + """</div>
    <div><div class="brand-text">FlockIQ</div><div class="brand-sub">Farm Management</div></div>
  </div>
  <div class="sidebar-nav">
    <div class="nav-section-label">Owner Panel</div>
    <a onclick="showTab('overview', this)" class="nav-link active"><i class="fas fa-gauge"></i> Overview</a>
    <a onclick="showTab('account-mgmt', this)" class="nav-link"><i class="fas fa-users-cog"></i> Account Management</a>
    <a onclick="showTab('market-price', this)" class="nav-link"><i class="fas fa-chart-line"></i> Market Prices</a>
    <a onclick="showTab('flock-mgmt', this)" class="nav-link"><i class="fas fa-layer-group"></i> Flock Management</a>
    <a onclick="showTab('harvest-history', this)" class="nav-link"><i class="fas fa-history"></i> Harvest History</a>
    <a onclick="showTab('summary-reports', this)" class="nav-link"><i class="fas fa-file-alt"></i> Summary Reports</a>
  </div>
  <div class="sidebar-footer">
    <div style="display:flex;align-items:center;gap:10px;padding:8px 12px;margin-bottom:8px;">
      <div style="width:34px;height:34px;border-radius:50%;background:linear-gradient(135deg,#166534,#15803d);display:flex;align-items:center;justify-content:center;color:#fff;font-size:13px;"><i class="fas fa-crown"></i></div>
      <div><div style="font-size:13px;font-weight:700;">{{ full_name }}</div><span class="role-badge role-owner">Owner</span></div>
    </div>
    <a href="/logout" class="logout-btn"><i class="fas fa-sign-out-alt"></i> Logout</a>
  </div>
</nav>

<div class="main-content">
  <div class="topbar">
    <span class="topbar-title">Owner Dashboard</span>
    <div class="topbar-actions">
      <button class="theme-toggle" onclick="toggleDark()"><i class="fas fa-moon"></i></button>
    </div>
  </div>
  <div class="page-body">

    {% with msgs = get_flashed_messages() %}{% if msgs %}
    {% for m in msgs %}
    <div class="alert alert-success alert-dismissible fade show alert-flash mb-3" role="alert">
      <i class="fas fa-check-circle me-2"></i>{{ m }}
      <button type="button" class="btn-close" data-bs-dismiss="alert"></button>
    </div>
    {% endfor %}{% endif %}{% endwith %}

    <!-- ==================== OVERVIEW ==================== -->
    <div id="overview" class="tab-content active">
        <div class="hero-banner">
          <div style="position:relative;z-index:1;">
            <div style="font-size:13px;font-weight:600;opacity:0.85;margin-bottom:6px;">Welcome back,</div>
            <h2 style="font-family:'Inter',sans-serif;font-weight:800;font-size:26px;margin:0 0 14px;">{{ full_name }} <i class="fas fa-crown" style="font-size:16px;opacity:0.8;"></i></h2>
            <div style="display:flex;flex-wrap:wrap;gap:8px;">
              <div class="metric-pill"><i class="fas fa-layer-group"></i> {{ active_flocks|length }} Active Flocks</div>
              <div class="metric-pill"><i class="fas fa-feather-pointed"></i> {{ "{:,}".format(total_birds) }} Total Remaining Birds</div>
              <div class="metric-pill"><i class="fas fa-users"></i> {{ users|length }} System Users</div>
            </div>
          </div>
          <div style="position:relative;z-index:1;">""" + logo_svg(90, 0.25) + """</div>
        </div>

        {% if active_flocks %}
        {% for f in active_flocks %}
        <div class="card mb-4">
          <div class="card-header-custom">
            <div class="section-header" style="margin:0;">
              <div class="section-divider"></div>
              <h5><i class="fas fa-feather-pointed me-2" style="color:var(--accent);"></i>Active Flock: {{ f.batch_name }}</h5>
            </div>
            <div style="display:flex;gap:8px;align-items:center;">
              {% if f.season %}<span class="badge-info">{{ f.season }} Season</span>{% endif %}
              <span class="badge-active">Active</span>
            </div>
          </div>
          <div class="card-body-custom">
            <div class="stat-grid">
              <div class="stat-card sc-farm-green">
                <div class="sc-icon"><i class="fas fa-feather-pointed"></i></div>
                <div class="sc-label">Current Total Number</div>
                <div class="sc-value">{{ "{:,}".format(f.current_bird_count) }}</div>
              </div>
              <div class="stat-card sc-farm-earth">
                <div class="sc-icon"><i class="fas fa-calendar-day"></i></div>
                <div class="sc-label">Age</div>
                <div class="sc-value">Day {{ f.age_days }} <span style="font-size:16px;">of 35</span></div>
              </div>
              <div class="stat-card sc-farm-red">
                <div class="sc-icon"><i class="fas fa-skull-crossbones"></i></div>
                <div class="sc-label">Mortality</div>
                <div class="sc-value">{{ f.mortality_count }} <span style="font-size:16px;">({{ f.mortality_percentage }}%)</span></div>
              </div>
              <div class="stat-card sc-farm-blue">
                <div class="sc-icon"><i class="fas fa-calendar-check"></i></div>
                <div class="sc-label">Target Harvest</div>
                <div class="sc-value" style="font-size:20px;">{{ f.target_harvest_date.strftime('%b %d') if f.target_harvest_date else '—' }}</div>
              </div>
            </div>
          </div>
        </div>
        {% endfor %}
        {% else %}
        <div class="card mb-4">
          <div class="card-body-custom text-center py-5" style="color:var(--muted);">
            <i class="fas fa-layer-group fa-3x mb-3 d-block"></i>
            <h5 style="font-weight:700;">No Active Flock</h5>
            <p>Go to Flock Management to create a new batch.</p>
          </div>
        </div>
        {% endif %}

        <div class="row g-4">
        <div class="col-lg-6 d-flex">
        <div class="card w-100">
          <div class="card-header-custom">
            <div class="section-header" style="margin:0;">
              <div class="section-divider"></div>
              <h5><i class="fas fa-chart-pie me-2" style="color:var(--accent);"></i>Expense Breakdown</h5>
            </div>
          </div>
          <div class="card-body-custom">
            {% if expense_summary.total > 0 %}
            <div style="display:flex;flex-wrap:wrap;align-items:center;gap:28px;">
              <div class="chart-container-sm" style="max-width:280px;flex:1 1 240px;">
                <canvas id="ownerExpensePieChart"></canvas>
              </div>
              <div style="flex:1 1 200px;display:flex;flex-direction:column;gap:10px;">
                <div style="display:flex;align-items:center;gap:8px;font-size:13px;"><span style="width:12px;height:12px;border-radius:3px;background:#0ea5e9;display:inline-block;"></span> Water — ₱{{ "{:,.0f}".format(expense_summary.water) }}</div>
                <div style="display:flex;align-items:center;gap:8px;font-size:13px;"><span style="width:12px;height:12px;border-radius:3px;background:#facc15;display:inline-block;"></span> Electricity — ₱{{ "{:,.0f}".format(expense_summary.electricity) }}</div>
                <div style="display:flex;align-items:center;gap:8px;font-size:13px;"><span style="width:12px;height:12px;border-radius:3px;background:#d97706;display:inline-block;"></span> LPG — ₱{{ "{:,.0f}".format(expense_summary.lpg) }}</div>
                <div style="display:flex;align-items:center;gap:8px;font-size:13px;"><span style="width:12px;height:12px;border-radius:3px;background:#7c3aed;display:inline-block;"></span> Labor — ₱{{ "{:,.0f}".format(expense_summary.labor) }}</div>
                <div style="display:flex;align-items:center;gap:8px;font-size:13px;"><span style="width:12px;height:12px;border-radius:3px;background:#0f766e;display:inline-block;"></span> Vaccine — ₱{{ "{:,.0f}".format(expense_summary.vaccine) }}</div>
                <div style="display:flex;align-items:center;gap:8px;font-size:13px;"><span style="width:12px;height:12px;border-radius:3px;background:#be123c;display:inline-block;"></span> Feed — ₱{{ "{:,.0f}".format(expense_summary.feed) }}</div>
                <div style="display:flex;align-items:center;gap:8px;font-size:13px;"><span style="width:12px;height:12px;border-radius:3px;background:#c2410c;display:inline-block;"></span> Other — ₱{{ "{:,.0f}".format(expense_summary.other) }}</div>
                <div style="display:flex;align-items:center;gap:8px;font-size:13px;font-weight:700;border-top:1px solid var(--border);padding-top:10px;margin-top:2px;">Total — ₱{{ "{:,.0f}".format(expense_summary.total) }}</div>
              </div>
            </div>
            <script>
            (function(){
              var el = document.getElementById('ownerExpensePieChart');
              if (el && window.Chart) {
                new Chart(el, {
                  type: 'pie',
                  data: {
                    labels: ['Water', 'Electricity', 'LPG', 'Labor', 'Vaccine', 'Feed', 'Other'],
                    datasets: [{
                      data: [{{ expense_summary.water }}, {{ expense_summary.electricity }}, {{ expense_summary.lpg }}, {{ expense_summary.labor }}, {{ expense_summary.vaccine }}, {{ expense_summary.feed }}, {{ expense_summary.other }}],
                      backgroundColor: ['#0ea5e9', '#facc15', '#d97706', '#7c3aed', '#0f766e', '#be123c', '#c2410c'],
                      borderWidth: 0
                    }]
                  },
                  options: {
                    responsive: true,
                    maintainAspectRatio: false,
                    plugins: {
                      legend: { display: false },
                      tooltip: {
                        callbacks: {
                          label: function(ctx) {
                            var val = ctx.parsed || 0;
                            var total = ctx.dataset.data.reduce(function(a,b){ return a+b; }, 0);
                            var pct = total > 0 ? ((val/total)*100).toFixed(1) : '0.0';
                            return ctx.label + ': ₱' + val.toLocaleString(undefined,{minimumFractionDigits:0,maximumFractionDigits:0}) + ' (' + pct + '%)';
                          }
                        }
                      }
                    }
                  }
                });
              }
            })();
            </script>
            {% else %}
            <div class="text-center py-4" style="color:var(--muted);">
              <i class="fas fa-chart-pie fa-2x mb-2 d-block"></i>
              No expenses logged yet.
            </div>
            {% endif %}
          </div>
        </div>
        </div>

        <div class="col-lg-6 d-flex">
        <div class="card w-100">
          <div class="card-header-custom">
            <div class="section-header" style="margin:0;">
              <div class="section-divider"></div>
              <h5><i class="fas fa-chart-column me-2" style="color:var(--accent);"></i>Flock Performance — ADG, FCR &amp; LW</h5>
            </div>
          </div>
          <div class="card-body-custom">
            {% if flock_analytics %}
            <div style="font-size:12px;color:var(--muted);margin-bottom:14px;">
              Average Daily Gain, Feed Conversion Ratio, and Live Weight per active flock.
            </div>
            <div style="display:flex;flex-direction:column;gap:12px;max-height:280px;overflow-y:auto;">
              {% for item in flock_analytics %}
              <div style="border:1px solid var(--border);border-radius:10px;padding:12px 14px;">
                <div style="font-weight:700;font-size:13px;margin-bottom:10px;">
                  {{ item.flock.batch_name }}
                  <span style="font-weight:400;color:var(--muted);">— Day {{ item.analytics.age_days }} out of 35</span>
                </div>
                <div style="display:flex;flex-wrap:wrap;gap:20px;">
                  <div>
                    <div style="font-size:11px;color:var(--muted);text-transform:uppercase;letter-spacing:.03em;">ADG</div>
                    <div style="font-size:16px;font-weight:800;color:#15803d;">{{ item.analytics.adg }} <span style="font-size:11px;font-weight:500;color:var(--muted);">g/day</span></div>
                  </div>
                  <div>
                    <div style="font-size:11px;color:var(--muted);text-transform:uppercase;letter-spacing:.03em;">FCR</div>
                    <div style="font-size:16px;font-weight:800;color:#d97706;">{{ item.analytics.fcr }}</div>
                  </div>
                  <div>
                    <div style="font-size:11px;color:var(--muted);text-transform:uppercase;letter-spacing:.03em;">LW</div>
                    <div style="font-size:16px;font-weight:800;color:#0ea5e9;">{{ "{:,.0f}".format(item.analytics.latest_weight) }} <span style="font-size:11px;font-weight:500;color:var(--muted);">g/bird</span></div>
                  </div>
                </div>
              </div>
              {% endfor %}
            </div>
            {% else %}
            <div class="text-center py-4" style="color:var(--muted);">
              <i class="fas fa-chart-column fa-2x mb-2 d-block"></i>
              No flock data yet.
            </div>
            {% endif %}
          </div>
        </div>
        </div>
        </div>
    </div>

    <!-- ==================== ACCOUNT MANAGEMENT ==================== -->
    <div id="account-mgmt" class="tab-content">
      <div class="card mb-4">
        <div class="card-header-custom">
          <div class="section-header" style="margin:0;">
            <div class="section-divider"></div>
            <h5><i class="fas fa-users-cog me-2" style="color:var(--accent);"></i>Account Management</h5>
          </div>
          <button class="btn-farm" data-bs-toggle="modal" data-bs-target="#addUserModal" style="font-size:13px;padding:7px 14px;">
            <i class="fas fa-plus me-1"></i> Add User
          </button>
        </div>
        <div class="card-body-custom">
          <div style="font-size:12px;color:var(--muted);margin-bottom:14px;">
            <i class="fas fa-lock me-1"></i> Only the Owner can create, edit, or remove accounts.
          </div>
          <div class="table-responsive">
            <table class="table table-hover align-middle">
              <thead><tr>
                <th>#</th><th>Full Name</th><th>Username</th><th>Phone Number</th><th>Role</th><th>Status</th><th>Actions</th>
              </tr></thead>
              <tbody>
              {% for u in users %}
              <tr>
                <td style="color:var(--muted);font-size:13px;">{{ u.user_id }}</td>
                <td style="font-weight:600;">{{ u.full_name }}</td>
                <td><code style="font-size:13px;">{{ u.username }}</code></td>
                <td style="font-size:13px;color:var(--muted);">{{ u.phone_num or '—' }}</td>
                <td>
                  {% if u.role == 'Owner' %}<span class="role-badge role-owner">Owner</span>
                  {% elif u.role == 'Manager' %}<span class="role-badge role-manager">Manager</span>
                  {% else %}<span class="role-badge role-worker">Worker</span>{% endif %}
                </td>
                <td>
                  {% if u.is_active %}
                  <span class="status-pill status-paid">Active</span>
                  {% else %}
                  <span class="status-pill status-missed">Inactive</span>
                  {% endif %}
                </td>
                <td>
                  <div class="tbl-actions">
                    <button class="btn-sm-icon btn-edit" type="button" data-bs-toggle="modal" data-bs-target="#editUserModal{{ u.user_id }}" title="Edit"><i class="fas fa-pen"></i></button>
                    <form method="post" action="/owner/user/deactivate/{{ u.user_id }}" style="display:inline;">
                      <button class="btn-sm-icon {{ 'btn-del' if u.is_active else 'btn-ok' }}" type="submit" title="{{ 'Deactivate' if u.is_active else 'Activate' }}" {% if u.username == 'owner' %}disabled{% endif %}>
                        <i class="fas {{ 'fa-user-slash' if u.is_active else 'fa-user-check' }}"></i>
                      </button>
                    </form>
                    <button class="btn-sm-icon btn-warn" type="button" data-bs-toggle="modal" data-bs-target="#resetPasswordModal{{ u.user_id }}" title="Reset Password"><i class="fas fa-key"></i></button>
                    <form method="post" action="/owner/user/delete/{{ u.user_id }}" onsubmit="return confirm('Delete user {{ u.username }}? This cannot be undone.')">
                      <button class="btn-sm-icon btn-del" type="submit" {% if u.username == 'owner' %}disabled title="Cannot delete the default owner account"{% endif %}><i class="fas fa-trash"></i></button>
                    </form>
                  </div>
                </td>
              </tr>

              <div class="modal fade" id="editUserModal{{ u.user_id }}" tabindex="-1">
                <div class="modal-dialog modal-dialog-centered">
                  <div class="modal-content" style="background:var(--card-bg);border:1px solid var(--border);border-radius:16px;">
                    <div class="modal-header" style="border-color:var(--border);">
                      <h5 class="modal-title" style="font-weight:800;"><i class="fas fa-user-pen me-2" style="color:var(--accent);"></i>Edit {{ u.full_name }}</h5>
                      <button type="button" class="btn-close" data-bs-dismiss="modal"></button>
                    </div>
                    <form method="post" action="/owner/user/edit/{{ u.user_id }}">
                      <div class="modal-body">
                        <div class="row g-2 mb-3">
                          <div class="col-4"><label class="form-label">First Name</label><input name="first_name" class="form-control" value="{{ u.first_name }}" required></div>
                          <div class="col-4"><label class="form-label">Middle Name</label><input name="middle_name" class="form-control" value="{{ u.middle_name or '' }}"></div>
                          <div class="col-4"><label class="form-label">Last Name</label><input name="last_name" class="form-control" value="{{ u.last_name }}" required></div>
                        </div>
                        <div class="mb-1"><label class="form-label">Phone Number</label>
                          <input name="phone_num" class="form-control" value="{{ u.phone_num or '' }}"
                                 pattern="09[0-9]{9}" maxlength="11" placeholder="09XXXXXXXXX"
                                 title="11 digits starting with 09">
                          <small style="color:var(--muted);">Format: 09XXXXXXXXX (11 digits).</small>
                        </div>
                      </div>
                      <div class="modal-footer" style="border-color:var(--border);">
                        <button type="button" class="btn-ghost" data-bs-dismiss="modal">Cancel</button>
                        <button type="submit" class="btn-farm">Save Changes</button>
                      </div>
                    </form>
                  </div>
                </div>
              </div>

              <div class="modal fade" id="resetPasswordModal{{ u.user_id }}" tabindex="-1">
                <div class="modal-dialog modal-dialog-centered">
                  <div class="modal-content" style="background:var(--card-bg);border:1px solid var(--border);border-radius:16px;">
                    <div class="modal-header" style="border-color:var(--border);">
                      <h5 class="modal-title" style="font-weight:800;"><i class="fas fa-key me-2" style="color:#a16207;"></i>Reset Password: {{ u.full_name }}</h5>
                      <button type="button" class="btn-close" data-bs-dismiss="modal"></button>
                    </div>
                    <form method="post" action="/owner/user/reset-password/{{ u.user_id }}">
                      <div class="modal-body">
                        <div class="mb-1"><label class="form-label">New Password</label><input type="password" name="new_password" class="form-control" required minlength="6"></div>
                        <small style="color:var(--muted);">Minimum 6 characters.</small>
                      </div>
                      <div class="modal-footer" style="border-color:var(--border);">
                        <button type="button" class="btn-ghost" data-bs-dismiss="modal">Cancel</button>
                        <button type="submit" class="btn-farm">Reset Password</button>
                      </div>
                    </form>
                  </div>
                </div>
              </div>
              {% else %}
              <tr><td colspan="7" class="text-center py-4" style="color:var(--muted);">No users found.</td></tr>
              {% endfor %}
              </tbody>
            </table>
          </div>
        </div>
      </div>
    </div>

    <!-- ==================== MARKET PRICES ==================== -->
    <div id="market-price" class="tab-content">
      <div class="stat-grid mb-4">
        <div class="stat-card sc-farm-forest">
          <div class="sc-icon"><i class="fas fa-tower-broadcast"></i></div>
          <div class="sc-label">DA Bantay Presyo — Chicken Price</div>
          <div class="sc-value">₱{{ "%.2f"|format(live_market.retail_avg) }}</div>
          <div style="font-size:11px;opacity:0.8;margin-top:4px;">{{ live_market.source }} · {{ live_market.last_update }}</div>
        </div>
        <div class="stat-card sc-farm-blue">
          <div class="sc-icon"><i class="fas fa-pen"></i></div>
          <div class="sc-label">Given Price (Today)</div>
          <div class="sc-value">{% if latest_owner_price %}₱{{ "%.2f"|format(latest_owner_price.price_per_kg) }}{% else %}—{% endif %}</div>
          <div style="font-size:11px;opacity:0.8;margin-top:4px;">{% if latest_owner_price %}{{ latest_owner_price.record_date.strftime('%b %d, %Y') }}{% else %}No price recorded for today{% endif %}</div>
        </div>
      </div>

      <div class="card">
        <div class="card-header-custom">
          <div class="section-header" style="margin:0;">
            <div class="section-divider"></div>
            <h5><i class="fas fa-table-list me-2" style="color:var(--accent);"></i>Given Price (Today)</h5>
          </div>
          <button class="btn-farm" data-bs-toggle="modal" data-bs-target="#addPriceModal" style="font-size:13px;padding:7px 14px;">
            <i class="fas fa-plus me-1"></i> Record Price
          </button>
        </div>
        <div class="card-body-custom">
          <div style="font-size:12px;color:var(--muted);margin-bottom:14px;">
            Only today's price is shown. Each new day starts fresh with a new given price.
          </div>
          <div class="table-responsive">
            <table class="table table-hover align-middle">
              <thead><tr><th>Date</th><th>Given Price / kg</th></tr></thead>
              <tbody>
              {% for p in today_prices %}
              <tr>
                <td>{{ p.record_date.strftime('%b %d, %Y') }}</td>
                <td style="font-weight:700;color:var(--accent);">₱{{ "%.2f"|format(p.price_per_kg) }}</td>
              </tr>
              {% else %}
              <tr><td colspan="2" class="text-center py-4" style="color:var(--muted);">No price recorded for today yet.</td></tr>
              {% endfor %}
              </tbody>
            </table>
          </div>
        </div>
      </div>
    </div>

    <!-- ==================== FLOCK MANAGEMENT ==================== -->
    <div id="flock-mgmt" class="tab-content">
      <div class="card mb-4">
        <div class="card-header-custom">
          <div class="section-header" style="margin:0;">
            <div class="section-divider"></div>
            <h5><i class="fas fa-layer-group me-2" style="color:var(--accent);"></i>Flock Management</h5>
          </div>
          <button class="btn-farm" data-bs-toggle="modal" data-bs-target="#addFlockModal" style="font-size:13px;padding:7px 14px;">
            <i class="fas fa-plus me-1"></i> New Flock Batch
          </button>
        </div>
        <div class="card-body-custom">
          <div style="font-size:12px;color:var(--muted);margin-bottom:14px;">
            <i class="fas fa-info-circle me-1"></i> Owner can add, edit, and delete batches. Harvesting is done by the Manager.
          </div>
          <div style="position:relative;max-width:320px;margin-bottom:14px;">
            <i class="fas fa-magnifying-glass" style="position:absolute;left:12px;top:50%;transform:translateY(-50%);color:var(--muted);font-size:13px;"></i>
            <input type="text" id="flockSearchInput" class="form-control" style="padding-left:34px;" placeholder="Search batch name or status..." onkeyup="filterFlockTable()">
          </div>
          <div class="table-responsive">
            <table class="table table-hover align-middle" id="flockTable">
              <thead><tr>
                <th>Batch</th><th>Season</th><th>Initial</th><th>Current</th><th>Deaths</th><th>Mortality %</th><th>Age</th><th>Start Date</th><th>Status</th><th>Actions</th>
              </tr></thead>
              <tbody>
              {% for f in flocks %}
              <tr>
                <td style="font-weight:700;">{{ f.batch_name }}</td>
                <td>{% if f.season %}<span class="badge-info">{{ f.season }}</span>{% else %}—{% endif %}</td>
                <td>{{ "{:,}".format(f.initial_bird_count) }}</td>
                <td>{{ "{:,}".format(f.current_bird_count) }}</td>
                <td style="color:#dc2626;font-weight:700;">{{ "{:,}".format(f.mortality_count) }}</td>
                <td style="color:{{ '#dc2626' if f.mortality_percentage > 10 else 'var(--text)' }};">{{ f.mortality_percentage }}%</td>
                <td>{{ f.age_days }} / 35</td>
                <td style="font-size:13px;color:var(--muted);">{{ f.start_date.strftime('%b %d, %Y') if f.start_date else '—' }}</td>
                <td>
                  {% if f.flock_status == 'Active' %}<span class="badge-active">Active</span>
                  {% else %}<span class="badge-harvested">Harvested</span>{% endif %}
                </td>
                <td>
                  <div class="tbl-actions">
                    {% if f.flock_status == 'Active' %}
                    <button class="btn-sm-icon btn-edit" data-bs-toggle="modal" data-bs-target="#editFlockModal{{ f.batch_id }}" title="Edit"><i class="fas fa-pen"></i></button>
                    {% else %}
                    <button class="btn-sm-icon" disabled title="Harvested flocks can no longer be edited" style="opacity:0.4;cursor:not-allowed;"><i class="fas fa-pen"></i></button>
                    {% endif %}
                    <form method="post" action="/owner/flock/delete/{{ f.batch_id }}" onsubmit="return confirm('Delete flock {{ f.batch_name }}? This removes all its related records.')">
                      <button class="btn-sm-icon btn-del" type="submit"><i class="fas fa-trash"></i></button>
                    </form>
                  </div>
                </td>
              </tr>
              {% else %}
              <tr><td colspan="10" class="text-center py-4" style="color:var(--muted);">No flocks added yet.</td></tr>
              {% endfor %}
              </tbody>
            </table>
            <div id="flockNoMatch" class="text-center py-4" style="color:var(--muted);display:none;">
              <i class="fas fa-magnifying-glass fa-2x mb-2 d-block"></i>
              No flocks match "<span id="flockNoMatchTerm"></span>".
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- ==================== HARVEST HISTORY — REVISED ==================== -->
    <div id="harvest-history" class="tab-content">
      <div class="row g-4">
        <!-- Batch picker -->
        <div class="col-lg-4">
          <div class="card">
            <div class="card-header-custom">
              <div class="section-header" style="margin:0;">
                <div class="section-divider"></div>
                <h5><i class="fas fa-list me-2" style="color:var(--accent);"></i>Select Batch</h5>
              </div>
            </div>
            <div class="card-body-custom">
              <div style="margin-bottom:12px;">
                <label class="form-label">Sort by Gain/Loss</label>
                <select class="form-select" onchange="location.href='?sort='+this.value+'#harvest-history'">
                  <option value="highest" {% if current_sort == 'highest' %}selected{% endif %}>Highest Gain → Lowest</option>
                  <option value="lowest" {% if current_sort == 'lowest' %}selected{% endif %}>Lowest → Highest Gain</option>
                </select>
              </div>
              <div style="display:flex;flex-direction:column;gap:6px;max-height:500px;overflow-y:auto;">
                {% for h in all_harvest_data %}
                <button type="button" class="harvest-pick-btn" data-batch-id="{{ h.id }}" onclick="showHarvestDetail({{ h.id }})"
                        style="text-align:left;padding:12px 14px;border-radius:10px;border:1px solid var(--border);background:var(--bg);cursor:pointer;transition:all 0.15s;width:100%;">
                  <div style="font-weight:700;font-size:13px;color:var(--text);">{{ h.batch_name }}</div>
                  <div style="font-size:11px;color:var(--muted);margin-top:2px;">{{ h.end_date.strftime('%b %d, %Y') if h.end_date else '—' }}</div>
                  <div style="font-size:12px;font-weight:700;margin-top:4px;color:{{ '#15803d' if h.loss_gain and h.loss_gain >= 0 else '#dc2626' }};">
                    {{ '+' if h.loss_gain and h.loss_gain >= 0 else '' }}₱{{ "{:,.0f}".format(h.loss_gain) if h.loss_gain is not none else '—' }}
                  </div>
                </button>
                {% else %}
                <div style="color:var(--muted);font-size:13px;padding:20px;text-align:center;">No harvest history yet.</div>
                {% endfor %}
              </div>
            </div>
          </div>
        </div>

        <!-- Performance detail -->
        <div class="col-lg-8">
          <div class="card" id="harvestDetailCard">
            <div class="card-header-custom">
              <div class="section-header" style="margin:0;">
                <div class="section-divider"></div>
                <h5><i class="fas fa-chart-line me-2" style="color:var(--accent);"></i>Performance Data</h5>
              </div>
            </div>
            <div class="card-body-custom" id="harvestDetailBody">
              <div class="text-center py-5" style="color:var(--muted);">
                <i class="fas fa-hand-pointer fa-3x mb-3 d-block"></i>
                <h5 style="font-weight:700;">Select a batch</h5>
                <p>Pick a harvested batch from the list to view its performance data.</p>
              </div>
            </div>
          </div>
        </div>
      </div>

      <!-- Summary metrics -->
      <div class="card mt-4">
        <div class="card-header-custom">
          <div class="section-header" style="margin:0;">
            <div class="section-divider"></div>
            <h5><i class="fas fa-chart-bar me-2" style="color:var(--accent);"></i>Overall Harvest Summary</h5>
          </div>
          <button class="btn-ghost" data-bs-toggle="modal" data-bs-target="#archivesModal" style="font-size:13px;padding:7px 14px;">
            <i class="fas fa-archive me-1"></i> Archives
          </button>
        </div>
        <div class="card-body-custom">
          <div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(180px,1fr));gap:14px;">
            <div style="background:{{ '#f0fdf4' if harvest_profit_summary.total_profit >= 0 else '#fef2f2' }};border:1px solid {{ '#bbf7d0' if harvest_profit_summary.total_profit >= 0 else '#fecaca' }};border-radius:10px;padding:14px 16px;">
              <div style="font-size:11px;text-transform:uppercase;letter-spacing:.03em;color:var(--muted);margin-bottom:4px;">Total Profit ({{ harvest_profit_summary.batch_count }} Batch{{ 'es' if harvest_profit_summary.batch_count != 1 else '' }})</div>
              <div style="font-size:22px;font-weight:800;color:{{ '#15803d' if harvest_profit_summary.total_profit >= 0 else '#dc2626' }};">
                {{ '+' if harvest_profit_summary.total_profit >= 0 else '' }}₱{{ "{:,.0f}".format(harvest_profit_summary.total_profit) }}
              </div>
            </div>
            <div style="background:var(--card-bg);border:1px solid var(--border);border-radius:10px;padding:14px 16px;">
              <div style="font-size:11px;text-transform:uppercase;letter-spacing:.03em;color:var(--muted);margin-bottom:4px;">Total Revenue</div>
              <div style="font-size:22px;font-weight:800;">₱{{ "{:,.0f}".format(harvest_profit_summary.total_revenue) }}</div>
            </div>
            <div style="background:var(--card-bg);border:1px solid var(--border);border-radius:10px;padding:14px 16px;">
              <div style="font-size:11px;text-transform:uppercase;letter-spacing:.03em;color:var(--muted);margin-bottom:4px;">Total Batch Expenses</div>
              <div style="font-size:22px;font-weight:800;">₱{{ "{:,.0f}".format(harvest_profit_summary.total_batch_expenses) }}</div>
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- ==================== SUMMARY REPORTS ==================== -->
    <div id="summary-reports" class="tab-content">
      <div class="card">
        <div class="card-header-custom">
          <div class="section-header" style="margin:0;">
            <div class="section-divider"></div>
            <h5><i class="fas fa-file-alt me-2" style="color:var(--accent);"></i>Farm Head/Manager Reports</h5>
          </div>
          <button class="btn-farm" data-bs-toggle="modal" data-bs-target="#printReportModal" style="font-size:13px;padding:7px 14px;">
            <i class="fas fa-print me-1"></i> Print Report
          </button>
        </div>
        <div class="card-body-custom">
          <div style="font-size:12px;color:var(--muted);margin-bottom:14px;">
            Reports filed by the Farm Head/Manager.
          </div>
          <div class="table-responsive">
            <table class="table table-hover align-middle">
              <thead><tr><th>Batch</th><th>Age</th><th>Initial</th><th>Harvest</th><th>Mortality</th><th>Start</th><th>Harvest</th><th>ADG</th><th>FCR</th><th>LW</th><th>Loss/Gain</th><th>Actions</th></tr></thead>
              <tbody>
              {% for r in summary_reports_list %}
              <tr>
                <td style="font-weight:700;">{{ r.batch_name }}</td>
                <td>{{ r.age }}</td>
                <td>{{ "{:,}".format(r.initial_count) }}</td>
                <td>{{ "{:,}".format(r.harvest_count) }}</td>
                <td style="color:{{ '#dc2626' if r.mortality_pct > 10 else 'var(--text)' }};">{{ r.mortality_pct }}%</td>
                <td style="font-size:13px;color:var(--muted);">{{ r.start_date }}</td>
                <td style="font-size:13px;color:var(--muted);">{{ r.harvest_date or '—' }}</td>
                <td>{{ r.adg }}</td>
                <td>{{ r.fcr }}</td>
                <td>{{ r.lw }} g</td>
                <td style="font-weight:700;color:{{ '#15803d' if r.loss_gain and r.loss_gain >= 0 else '#dc2626' }};">
                  {% if r.loss_gain is not none %}
                  {{ '+' if r.loss_gain >= 0 else '' }}₱{{ "{:,.0f}".format(r.loss_gain) }}
                  {% else %}—{% endif %}
                </td>
                <td><a href="/report/{{ r.report_id }}/print" target="_blank" class="btn-farm" style="font-size:12px;padding:5px 12px;"><i class="fas fa-eye me-1"></i>View</a></td>
              </tr>
              {% else %}
              <tr><td colspan="12" class="text-center py-4" style="color:var(--muted);">No reports filed yet.</td></tr>
              {% endfor %}
              </tbody>
            </table>
          </div>
        </div>
      </div>
    </div>

  </div></div></div>

<!-- ==================== MODALS ==================== -->

<!-- Add Price Modal -->
<div class="modal fade" id="addPriceModal" tabindex="-1">
  <div class="modal-dialog modal-dialog-centered">
    <div class="modal-content" style="background:var(--card-bg);border:1px solid var(--border);border-radius:16px;">
      <div class="modal-header" style="border-color:var(--border);">
        <h5 class="modal-title" style="font-weight:800;"><i class="fas fa-peso-sign me-2" style="color:var(--accent);"></i>Record Market Price</h5>
        <button type="button" class="btn-close" data-bs-dismiss="modal"></button>
      </div>
      <form method="post" action="/owner/market-price/add">
        <div class="modal-body">
          <div class="mb-3">
            <label class="form-label">Date</label>
            <input type="date" name="record_date" class="form-control" required max="{{ today_str }}" value="{{ today_str }}">
            <small style="color:var(--muted);">Cannot be later than today.</small>
          </div>
          <div class="mb-3"><label class="form-label">Price per kg (₱)</label><input type="number" step="0.01" name="price_per_kg" class="form-control" required></div>
          <div class="mb-1"><label class="form-label">Location (optional)</label><input name="location" class="form-control"></div>
        </div>
        <div class="modal-footer" style="border-color:var(--border);">
          <button type="button" class="btn-ghost" data-bs-dismiss="modal">Cancel</button>
          <button type="submit" class="btn-farm">Save</button>
        </div>
      </form>
    </div>
  </div>
</div>

<!-- Add User Modal -->
<div class="modal fade" id="addUserModal" tabindex="-1">
  <div class="modal-dialog modal-dialog-centered">
    <div class="modal-content" style="background:var(--card-bg);border:1px solid var(--border);border-radius:16px;">
      <div class="modal-header" style="border-color:var(--border);">
        <h5 class="modal-title" style="font-weight:800;"><i class="fas fa-user-plus me-2" style="color:var(--accent);"></i>Add New User</h5>
        <button type="button" class="btn-close" data-bs-dismiss="modal"></button>
      </div>
      <form method="post" action="/owner/user/add">
        <div class="modal-body">
          <div class="row g-2 mb-3">
            <div class="col-4"><label class="form-label">First Name</label><input name="first_name" class="form-control" required></div>
            <div class="col-4"><label class="form-label">Middle Name</label><input name="middle_name" class="form-control"></div>
            <div class="col-4"><label class="form-label">Last Name</label><input name="last_name" class="form-control" required></div>
          </div>
          <div class="mb-3">
            <label class="form-label">Phone Number</label>
            <input name="phone_num" class="form-control" required
                   pattern="09[0-9]{9}" maxlength="11" placeholder="09XXXXXXXXX"
                   title="11 digits starting with 09">
            <small style="color:var(--muted);">Format: 09XXXXXXXXX (11 digits).</small>
          </div>
          <div class="row g-2 mb-3">
            <div class="col-6"><label class="form-label">Username</label><input name="username" class="form-control" required></div>
            <div class="col-6"><label class="form-label">Password</label>
              <div style="position:relative;">
                <input type="password" name="password" id="addUserPw" class="form-control" required minlength="6" style="padding-right:38px;">
                <i class="fas fa-eye" style="position:absolute;right:12px;top:50%;transform:translateY(-50%);cursor:pointer;color:var(--muted);" onclick="
                  const f=document.getElementById('addUserPw'); const show = f.type==='password';
                  f.type = show ? 'text' : 'password';
                  this.classList.toggle('fa-eye'); this.classList.toggle('fa-eye-slash');
                "></i>
              </div>
            </div>
          </div>
          <div class="mb-1"><label class="form-label">Role</label>
            <select name="role" class="form-select">
              <option value="Manager">Manager</option>
              <option value="Worker" selected>Worker</option>
            </select>
          </div>
        </div>
        <div class="modal-footer" style="border-color:var(--border);">
          <button type="button" class="btn-ghost" data-bs-dismiss="modal">Cancel</button>
          <button type="submit" class="btn-farm">Add User</button>
        </div>
      </form>
    </div>
  </div>
</div>

<!-- Add Flock Modal -->
<div class="modal fade" id="addFlockModal" tabindex="-1">
  <div class="modal-dialog modal-dialog-centered">
    <div class="modal-content" style="background:var(--card-bg);border:1px solid var(--border);border-radius:16px;">
      <div class="modal-header" style="border-color:var(--border);">
        <h5 class="modal-title" style="font-weight:800;"><i class="fas fa-plus me-2" style="color:var(--accent);"></i>New Flock Batch</h5>
        <button type="button" class="btn-close" data-bs-dismiss="modal"></button>
      </div>
      <form method="post" action="/owner/flock/add">
        <div class="modal-body">
          {% if active_flocks %}
          <div class="alert" style="background:#fef3c7;color:#92400e;border:1px solid #fde68a;font-size:13px;border-radius:10px;padding:10px 14px;margin-bottom:14px;">
            <i class="fas fa-triangle-exclamation me-1"></i> <strong>{{ active_flocks[0].batch_name }}</strong> is still Active. Harvest it first — this farm raises one batch at a time.
          </div>
          {% endif %}

          <div class="mb-3">
            <label class="form-label">Batch Suffix / Custom Name <span style="color:var(--muted);font-weight:400;">(optional)</span></label>
            <input name="batch_suffix" class="form-control" placeholder="e.g. Summer Cycle"
                   {% if active_flocks %}disabled{% endif %}>
            <small style="color:var(--muted);">Auto-generated as <code>Batch-{{ current_year }}-X</code> + your suffix.</small>
          </div>

          <div class="mb-3">
            <label class="form-label">Initial Bird Count</label>
            <input type="number" name="initial_bird_count" class="form-control" placeholder="0" min="0" required {% if active_flocks %}disabled{% endif %}>
          </div>

          <div class="row g-2 mb-3">
            <div class="col-6">
              <label class="form-label">Date of Arrival <span class="text-danger">*</span></label>
              <input type="date" name="start_date" class="form-control" required {% if active_flocks %}disabled{% endif %}>
            </div>
            <div class="col-6">
              <label class="form-label">Target Harvest Date <span class="text-danger">*</span></label>
              <input type="date" name="target_harvest_date" class="form-control" required {% if active_flocks %}disabled{% endif %}>
            </div>
          </div>

          <div class="mb-1">
            <label class="form-label">Season of Arrival <span class="text-danger">*</span></label>
            <select name="season" class="form-select" required {% if active_flocks %}disabled{% endif %}>
              <option value="">— Select Season —</option>
              <option value="Dry">Dry</option>
              <option value="Wet">Wet</option>
            </select>
          </div>
        </div>
        <div class="modal-footer" style="border-color:var(--border);">
          <button type="button" class="btn-ghost" data-bs-dismiss="modal">Cancel</button>
          <button type="submit" class="btn-farm" {% if active_flocks %}disabled{% endif %}>Create Flock</button>
        </div>
      </form>
    </div>
  </div>
</div>

<!-- Edit Flock Modals -->
{% for f in flocks %}
<div class="modal fade" id="editFlockModal{{ f.batch_id }}" tabindex="-1">
  <div class="modal-dialog modal-dialog-centered">
    <div class="modal-content" style="background:var(--card-bg);border:1px solid var(--border);border-radius:16px;">
      <div class="modal-header" style="border-color:var(--border);">
        <h5 class="modal-title" style="font-weight:800;">Edit: {{ f.batch_name }}</h5>
        <button type="button" class="btn-close" data-bs-dismiss="modal"></button>
      </div>
      <form method="post" action="/owner/flock/edit/{{ f.batch_id }}">
        <div class="modal-body">
          <div class="mb-3"><label class="form-label">Batch Name</label>
            <input name="batch_name" class="form-control" value="{{ f.batch_name }}" required></div>
          <div class="mb-3"><label class="form-label">Current Bird Count</label>
            <div style="font-weight:700;font-size:15px;">{{ "{:,}".format(f.current_bird_count) }}
              <span style="font-weight:400;color:var(--muted);font-size:12px;">— auto-calculated from mortality/cull records</span>
            </div>
          </div>
          <div class="mt-3"><label class="form-label">Status</label>
            <select name="flock_status" class="form-select">
              <option value="Active" {% if f.flock_status=='Active' %}selected{% endif %}>Active</option>
              <option value="Harvested" {% if f.flock_status=='Harvested' %}selected{% endif %}>Harvested</option>
            </select>
            <small style="color:var(--muted);">System blocks marking as Harvested until the batch has recorded data.</small>
          </div>
        </div>
        <div class="modal-footer" style="border-color:var(--border);">
          <button type="button" class="btn-ghost" data-bs-dismiss="modal">Cancel</button>
          <button type="submit" class="btn-farm">Save Changes</button>
        </div>
      </form>
    </div>
  </div>
</div>
{% endfor %}

<!-- Archives Modal -->
<div class="modal fade" id="archivesModal" tabindex="-1">
  <div class="modal-dialog modal-dialog-centered modal-lg">
    <div class="modal-content" style="background:var(--card-bg);border:1px solid var(--border);border-radius:16px;">
      <div class="modal-header" style="border-color:var(--border);">
        <h5 class="modal-title" style="font-weight:800;"><i class="fas fa-archive me-2" style="color:var(--accent);"></i>Harvest Archives by Year</h5>
        <button type="button" class="btn-close" data-bs-dismiss="modal"></button>
      </div>
      <div class="modal-body">
        <p style="font-size:13px;color:var(--muted);margin-bottom:14px;">Select a year to filter the Harvest History list.</p>
        <div style="display:flex;flex-wrap:wrap;gap:8px;">
          {% for year in harvest_years %}
          <button class="btn-ghost" onclick="filterByYear({{ year }}); bootstrap.Modal.getInstance(document.getElementById('archivesModal')).hide();" style="font-size:13px;padding:8px 16px;">{{ year }}</button>
          {% else %}
          <span style="color:var(--muted);font-size:13px;">No archived years yet.</span>
          {% endfor %}
          {% if harvest_years %}
          <button class="btn-farm" onclick="filterByYear(null); bootstrap.Modal.getInstance(document.getElementById('archivesModal')).hide();" style="font-size:13px;padding:8px 16px;">All Years</button>
          {% endif %}
        </div>
      </div>
      <div class="modal-footer" style="border-color:var(--border);">
        <button type="button" class="btn-ghost" data-bs-dismiss="modal">Close</button>
      </div>
    </div>
  </div>
</div>

<!-- Print Report Modal (Owner) -->
<div class="modal fade" id="printReportModal" tabindex="-1">
  <div class="modal-dialog modal-dialog-centered modal-lg">
    <div class="modal-content" style="background:var(--card-bg);border:1px solid var(--border);border-radius:16px;">
      <div class="modal-header" style="border-color:var(--border);">
        <h5 class="modal-title" style="font-weight:800;"><i class="fas fa-print me-2" style="color:var(--accent);"></i>Generate Summary Report</h5>
        <button type="button" class="btn-close" data-bs-dismiss="modal"></button>
      </div>
      <div class="modal-body">
        <p style="font-size:13px;color:var(--muted);margin-bottom:14px;">
          Select which fields you want to include in the report, then choose a batch to print.
        </p>
        <div class="mb-3">
          <label class="form-label">Select Batch</label>
          <select id="reportBatchSelect" class="form-select">
            <option value="">— Select a harvested batch —</option>
            {% for r in summary_reports_list %}
            <option value="{{ r.report_id }}">{{ r.batch_name }} ({{ r.harvest_date }})</option>
            {% endfor %}
          </select>
        </div>
        <label class="form-label">Fields to Include</label>
        <div class="report-field-list" id="reportFieldsList">
          <label class="report-field-item"><input type="checkbox" checked data-field="batch_name"> Batch Name</label>
          <label class="report-field-item"><input type="checkbox" checked data-field="age"> Age</label>
          <label class="report-field-item"><input type="checkbox" checked data-field="initial_count"> Initial Count</label>
          <label class="report-field-item"><input type="checkbox" checked data-field="harvest_count"> Harvest Count</label>
          <label class="report-field-item"><input type="checkbox" checked data-field="mortality_pct"> Mortality %</label>
          <label class="report-field-item"><input type="checkbox" checked data-field="start_date"> Start Date</label>
          <label class="report-field-item"><input type="checkbox" checked data-field="harvest_date"> Harvest Date</label>
          <label class="report-field-item"><input type="checkbox" checked data-field="adg"> ADG</label>
          <label class="report-field-item"><input type="checkbox" checked data-field="fcr"> FCR</label>
          <label class="report-field-item"><input type="checkbox" checked data-field="lw"> LW</label>
          <label class="report-field-item"><input type="checkbox" checked data-field="expenses"> Expenses</label>
          <label class="report-field-item"><input type="checkbox" checked data-field="season"> Season</label>
          <label class="report-field-item"><input type="checkbox" checked data-field="chick_booster"> Chick Booster</label>
          <label class="report-field-item"><input type="checkbox" checked data-field="grower_pellets"> Grower Pellets</label>
          <label class="report-field-item"><input type="checkbox" checked data-field="finisher_pellets"> Finisher Pellets</label>
          <label class="report-field-item"><input type="checkbox" checked data-field="vaccine_day_12"> Vaccine Day 12</label>
          <label class="report-field-item"><input type="checkbox" checked data-field="vaccine_day_16"> Vaccine Day 16</label>
          <label class="report-field-item"><input type="checkbox" checked data-field="medicines"> Medicines</label>
          <label class="report-field-item"><input type="checkbox" checked data-field="loss_gain"> Loss/Gain</label>
          <label class="report-field-item"><input type="checkbox" checked data-field="remarks"> Remarks</label>
        </div>
      </div>
      <div class="modal-footer" style="border-color:var(--border);">
        <button type="button" class="btn-ghost" data-bs-dismiss="modal">Cancel</button>
        <button type="button" class="btn-farm" onclick="openSelectedReport()"><i class="fas fa-print me-1"></i> Open Report</button>
      </div>
    </div>
  </div>
</div>

""" + _BASE_SCRIPT + """
<script>
var harvestDataMap = {
  {% for h in all_harvest_data %}
  "{{ h.id }}": {
    batch_name: "{{ h.batch_name }}",
    age: "{{ h.age }}",
    initial_count: "{{ h.initial_count }}",
    harvest_count: "{{ h.harvest_count }}",
    mortality_pct: "{{ h.mortality_pct }}",
    start_date: "{{ h.start_date.strftime('%b %d, %Y') if h.start_date else '' }}",
    end_date: "{{ h.end_date.strftime('%b %d, %Y') if h.end_date else '' }}",
    adg: "{{ h.adg }}",
    fcr: "{{ h.fcr }}",
    lw: "{{ h.lw }}",
    expenses: "{{ h.expenses }}",
    season: "{{ h.season or '' }}",
    vaccine_day_12: "{{ h.vaccine_day_12 or '' }}",
    vaccine_day_16: "{{ h.vaccine_day_16 or '' }}",
    loss_gain: "{{ h.loss_gain if h.loss_gain is not none else '' }}",
    remarks: "{{ h.remarks or '' }}"
  }{% if not loop.last %},{% endif %}
  {% endfor %}
};

function showHarvestDetail(id) {
  document.querySelectorAll('.harvest-pick-btn').forEach(function(b){
    b.style.borderColor = 'var(--border)';
    b.style.background = 'var(--bg)';
  });
  var btn = document.querySelector('.harvest-pick-btn[data-batch-id="' + id + '"]');
  if (btn) { btn.style.borderColor = '#166534'; btn.style.background = '#f0fdf4'; }

  var d = harvestDataMap[id];
  if (!d) return;
  var lg = d.loss_gain !== '' ? parseFloat(d.loss_gain) : 0;
  var lgColor = lg >= 0 ? '#15803d' : '#dc2626';
  var lgSign = lg >= 0 ? '+' : '';

  var html = '';
  html += '<div style="margin-bottom:16px;"><div style="font-family:Inter,sans-serif;font-size:22px;font-weight:800;">' + d.batch_name + '</div>';
  html += '<div style="font-size:12px;color:var(--muted);">' + d.start_date + ' → ' + d.end_date + ' · ' + d.age + ' days</div></div>';

  html += '<div class="detail-grid">';
  html += '<div class="detail-item"><div class="label">Initial Count</div><div class="value">' + parseInt(d.initial_count).toLocaleString() + '</div></div>';
  html += '<div class="detail-item"><div class="label">Harvest Count</div><div class="value">' + parseInt(d.harvest_count).toLocaleString() + '</div></div>';
  html += '<div class="detail-item"><div class="label">Mortality</div><div class="value" style="color:#dc2626;">' + d.mortality_pct + '%</div></div>';
  html += '<div class="detail-item"><div class="label">Season</div><div class="value">' + (d.season || '—') + '</div></div>';
  html += '<div class="detail-item"><div class="label">ADG</div><div class="value" style="color:#15803d;">' + d.adg + ' g/day</div></div>';
  html += '<div class="detail-item"><div class="label">FCR</div><div class="value" style="color:#d97706;">' + d.fcr + '</div></div>';
  html += '<div class="detail-item"><div class="label">Live Weight</div><div class="value" style="color:#0ea5e9;">' + d.lw + ' g</div></div>';
  html += '<div class="detail-item"><div class="label">Expenses</div><div class="value">₱' + parseFloat(d.expenses).toLocaleString() + '</div></div>';
  html += '<div class="detail-item"><div class="label">Vaccine Day 12</div><div class="value">' + (d.vaccine_day_12 || '—') + '</div></div>';
  html += '<div class="detail-item"><div class="label">Vaccine Day 16</div><div class="value">' + (d.vaccine_day_16 || '—') + '</div></div>';
  html += '<div class="detail-item"><div class="label">Loss/Gain</div><div class="value" style="color:' + lgColor + ';font-size:16px;">' + lgSign + '₱' + Math.abs(lg).toLocaleString() + '</div></div>';
  html += '</div>';

  if (d.remarks) {
    html += '<div style="margin-top:14px;padding:12px;background:var(--bg);border-radius:8px;border:1px solid var(--border);font-size:13px;color:var(--muted);"><i class="fas fa-comment me-1"></i>' + d.remarks + '</div>';
  }

  html += '<div style="margin-top:16px;"><a href="/report/' + id + '/print" target="_blank" class="btn-farm" style="font-size:13px;padding:7px 16px;"><i class="fas fa-print me-1"></i> Print Performance Report</a></div>';

  document.getElementById('harvestDetailBody').innerHTML = html;
}

function filterFlockTable() {
  var term = document.getElementById('flockSearchInput').value.trim().toLowerCase();
  var rows = document.querySelectorAll('#flockTable tbody tr');
  var visibleCount = 0;
  rows.forEach(function(row) {
    if (row.children.length < 2) { return; }
    var text = row.textContent.toLowerCase();
    var match = text.indexOf(term) !== -1;
    row.style.display = match ? '' : 'none';
    if (match) { visibleCount++; }
  });
  var noMatch = document.getElementById('flockNoMatch');
  var noMatchTerm = document.getElementById('flockNoMatchTerm');
  if (term && visibleCount === 0) {
    noMatchTerm.textContent = document.getElementById('flockSearchInput').value.trim();
    noMatch.style.display = 'block';
  } else {
    noMatch.style.display = 'none';
  }
}

function filterByYear(year) {
  var buttons = document.querySelectorAll('.harvest-pick-btn');
  buttons.forEach(function(btn) {
    if (!year) { btn.style.display = ''; return; }
    var text = btn.textContent;
    btn.style.display = text.indexOf(year.toString()) !== -1 ? '' : 'none';
  });
}

function openSelectedReport() {
  var sel = document.getElementById('reportBatchSelect');
  if (!sel.value) { alert('Please select a batch first.'); return; }
  var fields = [];
  document.querySelectorAll('#reportFieldsList input[type="checkbox"]:checked').forEach(function(cb) {
    fields.push(cb.dataset.field);
  });
  var url = '/report/' + sel.value + '/print?fields=' + fields.join(',');
  window.open(url, '_blank');
}
</script>
</body></html>
"""

# ─────────────────────────────────────────────────────────────────────────────
# MANAGER DASHBOARD — REVISED
# ─────────────────────────────────────────────────────────────────────────────
TEMPLATE_MANAGER = """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Manager Dashboard — FlockIQ</title>
""" + _BASE_STYLE + """
</head>
<body>
<script>(function(){const t=localStorage.getItem("theme");if(t==="dark")document.documentElement.classList.add("dark");})()</script>
<div id="mobileOverlay" class="mobile-overlay" onclick="toggleSidebar()"></div>
<div class="mobile-topbar">
  <button onclick="toggleSidebar()" style="background:none;border:none;color:var(--text);font-size:20px;"><i class="fas fa-bars"></i></button>
  <span style="font-family:'Inter',sans-serif;font-weight:800;font-size:16px;">FlockIQ</span>
  <button class="theme-toggle" onclick="toggleDark()"><i class="fas fa-moon"></i></button>
</div>
<div class="app-shell">

<nav id="sidebar" class="sidebar">
  <div class="sidebar-brand">
    <div class="brand-icon" style="background:linear-gradient(135deg,#3f6212,#166534);">""" + logo_svg(22) + """</div>
    <div><div class="brand-text">FlockIQ</div><div class="brand-sub">Manager View</div></div>
  </div>
  <div class="sidebar-nav">
    <div class="nav-section-label">Manager Panel</div>
    <a onclick="showTab('mgr-overview', this)" class="nav-link active"><i class="fas fa-gauge"></i> Overview</a>
    <a onclick="showTab('mgr-verification', this)" class="nav-link"><i class="fas fa-clipboard-check"></i> Record Verification {% if pending_submissions %}<span class="badge-count">{{ pending_submissions|length }}</span>{% endif %}</a>
    <a onclick="showTab('mgr-expenses', this)" class="nav-link"><i class="fas fa-receipt"></i> Expenses</a>
    <a onclick="showTab('vaccination-mgmt', this)" class="nav-link"><i class="fas fa-syringe"></i> Vaccination Management</a>
    <a onclick="showTab('vitamin-mgmt', this)" class="nav-link"><i class="fas fa-tablets"></i> Vitamins & Medicine</a>
    <a onclick="showTab('feed-mgmt', this)" class="nav-link"><i class="fas fa-wheat-awn"></i> Feed Inventory</a>
    <a onclick="showTab('mgr-reports', this)" class="nav-link"><i class="fas fa-file-alt"></i> Reports</a>
  </div>
  <div class="sidebar-footer">
    <div style="display:flex;align-items:center;gap:10px;padding:8px 12px;margin-bottom:8px;">
      <div style="width:34px;height:34px;border-radius:50%;background:linear-gradient(135deg,#3f6212,#166534);display:flex;align-items:center;justify-content:center;color:#fff;font-size:13px;"><i class="fas fa-user-tie"></i></div>
      <div><div style="font-size:13px;font-weight:700;">{{ full_name }}</div><span class="role-badge role-manager">Manager</span></div>
    </div>
    <a href="/logout" class="logout-btn"><i class="fas fa-sign-out-alt"></i> Logout</a>
  </div>
</nav>

<div class="main-content">
  <div class="topbar">
    <span class="topbar-title">Manager Dashboard</span>
    <div class="topbar-actions">
      <button class="theme-toggle" onclick="toggleDark()"><i class="fas fa-moon"></i></button>
    </div>
  </div>
  <div class="page-body">

    {% with msgs = get_flashed_messages() %}{% if msgs %}
    {% for m in msgs %}
    <div class="alert alert-success alert-dismissible fade show alert-flash mb-3" role="alert">
      <i class="fas fa-check-circle me-2"></i>{{ m }}
      <button type="button" class="btn-close" data-bs-dismiss="alert"></button>
    </div>
    {% endfor %}{% endif %}{% endwith %}

    <!-- ==================== OVERVIEW ==================== -->
    <div id="mgr-overview" class="tab-content active">
        <div class="hero-banner">
          <div style="position:relative;z-index:1;">
            <div style="font-size:13px;font-weight:600;opacity:0.85;margin-bottom:6px;">Manager Portal</div>
            <h2 style="font-family:'Inter',sans-serif;font-weight:800;font-size:24px;margin:0 0 14px;">{{ full_name }} <i class="fas fa-user-tie" style="font-size:16px;opacity:0.8;"></i></h2>
            <div style="display:flex;flex-wrap:wrap;gap:8px;">
              <div class="metric-pill"><i class="fas fa-feather-pointed"></i> {{ totals.remaining }} Remaining Birds</div>
              <div class="metric-pill"><i class="fas fa-skull-crossbones"></i> {{ totals.deaths }} Total Deaths ({{ totals.mortality_pct }}%)</div>
            </div>
          </div>
          <div style="position:relative;z-index:1;">""" + logo_svg(90, 0.25) + """</div>
        </div>

        <div class="stat-grid mb-4">
          <div class="stat-card sc-farm-green">
            <div class="sc-icon"><i class="fas fa-feather-pointed"></i></div>
            <div class="sc-label">Remaining Birds</div>
            <div class="sc-value">{{ totals.remaining }}</div>
          </div>
          <div class="stat-card sc-farm-red">
            <div class="sc-icon"><i class="fas fa-skull-crossbones"></i></div>
            <div class="sc-label">Mortality</div>
            <div class="sc-value">{{ totals.deaths }} <span style="font-size:16px;">({{ totals.mortality_pct }}%)</span></div>
          </div>
          <div class="stat-card sc-farm-blue">
            <div class="sc-icon"><i class="fas fa-syringe"></i></div>
            <div class="sc-label">Vaccination Schedules</div>
            <div class="sc-value" style="font-size:15px;line-height:1.4;">Day 12: {{ day12_vaccine or '—' }}<br>Day 16: {{ day16_vaccine or '—' }}</div>
          </div>
          <div class="stat-card sc-farm-olive">
            <div class="sc-icon"><i class="fas fa-pills"></i></div>
            <div class="sc-label">Medicine Schedules</div>
            <div class="sc-value" style="font-size:18px;">{{ medication_count }} scheduled</div>
          </div>
          <div class="stat-card" style="background:linear-gradient(135deg,{{ '#b45309,#f59e0b' if pending_submissions else '#166534,#15803d' }});cursor:pointer;" onclick="showTab('mgr-verification', document.querySelector('[onclick*=mgr-verification]'))">
            <div class="sc-icon"><i class="fas fa-clipboard-check"></i></div>
            <div class="sc-label">Pending Records</div>
            <div class="sc-value">{{ pending_submissions|length }}</div>
          </div>
        </div>

        <!-- Harvest button for active batch -->
        {% if active_flocks %}
        {% for f in active_flocks %}
        <div class="card mb-4" style="border-left:4px solid #166534;">
          <div class="card-body-custom">
            <div style="display:flex;flex-wrap:wrap;align-items:center;justify-content:space-between;gap:16px;">
              <div>
                <div style="font-weight:800;font-size:16px;">{{ f.batch_name }}</div>
                <div style="font-size:13px;color:var(--muted);">Day {{ f.age_days }} of 35 · {{ "{:,}".format(f.current_bird_count) }} birds remaining</div>
              </div>
              <button class="btn-farm" data-bs-toggle="modal" data-bs-target="#harvestFlockModal{{ f.batch_id }}" style="padding:9px 20px;">
                <i class="fas fa-check me-1"></i> Harvest Batch
              </button>
            </div>
          </div>
        </div>

        <div class="modal fade" id="harvestFlockModal{{ f.batch_id }}" tabindex="-1">
          <div class="modal-dialog modal-dialog-centered">
            <div class="modal-content" style="background:var(--card-bg);border:1px solid var(--border);border-radius:16px;">
              <div class="modal-header" style="border-color:var(--border);">
                <h5 class="modal-title" style="font-weight:800;"><i class="fas fa-check-circle me-2" style="color:#166534;"></i>Confirm Harvest</h5>
                <button type="button" class="btn-close" data-bs-dismiss="modal"></button>
              </div>
              <form method="post" action="/manager/flock/harvest/{{ f.batch_id }}">
                <div class="modal-body">
                  <p style="font-size:14px;margin-bottom:16px;">Are you sure you want to mark <strong>{{ f.batch_name }}</strong> as Harvested? This will:</p>
                  <ul style="font-size:13px;color:var(--muted);margin-bottom:16px;">
                    <li>Archive the batch to Harvest History</li>
                    <li>Lock the batch from further edits</li>
                    <li>Allow the Owner to create a new flock batch</li>
                  </ul>
                  {% if not f.has_data %}
                  <div class="alert" style="background:#fef2f2;color:#991b1b;border:1px solid #fecaca;font-size:13px;border-radius:10px;padding:10px 14px;margin-bottom:12px;">
                    <i class="fas fa-triangle-exclamation me-1"></i>
                    <strong>This batch has no recorded data yet.</strong> The system will reject the harvest until daily records, growth, feed, or sales exist.
                  </div>
                  {% endif %}
                  <div style="background:var(--bg);border-radius:10px;padding:14px;border:1px solid var(--border);">
                    <div class="confirm-row"><span class="label">Batch</span><span class="value">{{ f.batch_name }}</span></div>
                    <div class="confirm-row"><span class="label">Season</span><span class="value">{{ f.season or '—' }}</span></div>
                    <div class="confirm-row"><span class="label">Age</span><span class="value">Day {{ f.age_days }} of 35</span></div>
                    <div class="confirm-row"><span class="label">Initial Count</span><span class="value">{{ "{:,}".format(f.initial_bird_count) }}</span></div>
                    <div class="confirm-row"><span class="label">Current Count</span><span class="value">{{ "{:,}".format(f.current_bird_count) }}</span></div>
                    <div class="confirm-row"><span class="label">Mortality</span><span class="value">{{ f.mortality_count }} ({{ f.mortality_percentage }}%)</span></div>
                  </div>
                </div>
                <div class="modal-footer" style="border-color:var(--border);">
                  <button type="button" class="btn-ghost" data-bs-dismiss="modal">Cancel</button>
                  <button type="submit" class="btn-farm" {% if not f.has_data %}disabled style="opacity:0.5;cursor:not-allowed;"{% endif %}>
                    Confirm Harvest
                  </button>
                </div>
              </form>
            </div>
          </div>
        </div>
        {% endfor %}
        {% endif %}

        <div class="card">
          <div class="card-header-custom">
            <div class="section-header" style="margin:0;">
              <div class="section-divider"></div>
              <h5><i class="fas fa-chart-column me-2" style="color:var(--accent);"></i>Flock Analytics — ADG & FCR by Batch</h5>
            </div>
          </div>
          <div class="card-body-custom">
            {% if flock_analytics %}
            <div class="chart-container-sm">
              <canvas id="overviewAnalyticsChart"></canvas>
            </div>
            <script>
            (function(){
              var el = document.getElementById('overviewAnalyticsChart');
              if (el && window.Chart) {
                new Chart(el, {
                  type: 'bar',
                  data: {
                    labels: {{ flock_analytics|map(attribute='flock.batch_name')|list|tojson }},
                    datasets: [
                      { label: 'ADG (g/day)', data: {{ flock_analytics|map(attribute='analytics.adg')|list|tojson }}, backgroundColor: '#15803d', borderRadius: 6, yAxisID: 'y' },
                      { label: 'FCR', data: {{ flock_analytics|map(attribute='analytics.fcr')|list|tojson }}, backgroundColor: '#d97706', borderRadius: 6, yAxisID: 'y1' }
                    ]
                  },
                  options: {
                    responsive: true, maintainAspectRatio: false,
                    plugins: { legend: { display: true, position: 'top' } },
                    scales: {
                      y: { beginAtZero: true, position: 'left', title: { display: true, text: 'ADG (g/day)' } },
                      y1: { beginAtZero: true, position: 'right', title: { display: true, text: 'FCR' }, grid: { drawOnChartArea: false } }
                    }
                  }
                });
              }
            })();
            </script>
            {% else %}
            <div class="text-center py-4" style="color:var(--muted);">
              <i class="fas fa-chart-column fa-2x mb-2 d-block"></i>
              No flock data yet.
            </div>
            {% endif %}
          </div>
        </div>
    </div>

    <!-- ==================== RECORD VERIFICATION ==================== -->
    <div id="mgr-verification" class="tab-content">
      <div class="card">
        <div class="card-header-custom">
          <div class="section-header" style="margin:0;">
            <div class="section-divider"></div>
            <h5><i class="fas fa-clipboard-check me-2" style="color:var(--accent);"></i>Pending Worker Submissions</h5>
          </div>
        </div>
        <div class="card-body-custom">
          <div style="font-size:12px;color:var(--muted);margin-bottom:14px;">
            Nothing here affects bird counts, ADG, or FCR until you Approve it.
          </div>
          {% if pending_submissions %}
          <div class="table-responsive">
            <table class="table table-hover align-middle">
              <thead><tr><th>Batch</th><th>Worker</th><th>Date</th><th>Weight</th><th>Mortality / Cull</th><th>Feed</th><th>Health Notes</th><th></th></tr></thead>
              <tbody>
              {% for s in pending_submissions %}
              <tr>
                <td style="font-weight:700;">{{ s.batch.batch_name if s.batch else '—' }}</td>
                <td>{{ s.worker.full_name if s.worker else '—' }}</td>
                <td style="font-size:13px;color:var(--muted);">{{ s.record_date.strftime('%b %d, %Y') if s.record_date else '—' }}</td>
                <td>{{ s.avg_weight_g }} g</td>
                <td>{{ s.mortality }} / {{ s.cull }}{% if s.cause %}<div style="font-size:11px;color:var(--muted);">{{ s.cause }}</div>{% endif %}</td>
                <td>{{ s.feed_kg }} kg{% if s.feed %}<div style="font-size:11px;color:var(--muted);">{{ s.feed.feed_name }}</div>{% endif %}</td>
                <td style="font-size:12px;">
                  {% if s.water_consumption %}<div>💧 {{ s.water_consumption }}</div>{% endif %}
                  {% if s.abnormal_behavior %}<div style="color:#b45309;">⚠ {{ s.abnormal_behavior }}</div>{% endif %}
                  {% if s.visible_illness %}<div style="color:#dc2626;">🩺 {{ s.visible_illness }}</div>{% endif %}
                  {% if s.remarks %}<div style="color:var(--muted);">{{ s.remarks }}</div>{% endif %}
                </td>
                <td style="white-space:nowrap;">
                  <form method="post" action="/manager/submission/approve/{{ s.submission_id }}" style="display:inline;">
                    <button type="submit" class="btn-sm-icon btn-ok" title="Approve"><i class="fas fa-check"></i></button>
                  </form>
                  <button type="button" class="btn-sm-icon btn-del" data-bs-toggle="modal" data-bs-target="#rejectModal{{ s.submission_id }}" title="Reject"><i class="fas fa-xmark"></i></button>
                </td>
              </tr>
              {% endfor %}
              </tbody>
            </table>
          </div>
          {% else %}
          <div class="text-center py-4" style="color:var(--muted);">
            <i class="fas fa-clipboard-check fa-2x mb-2 d-block"></i>
            No pending submissions — all caught up.
          </div>
          {% endif %}
        </div>
      </div>
    </div>

    {% for s in pending_submissions %}
    <div class="modal fade" id="rejectModal{{ s.submission_id }}" tabindex="-1">
      <div class="modal-dialog modal-dialog-centered">
        <div class="modal-content" style="background:var(--card-bg);border:1px solid var(--border);border-radius:16px;">
          <div class="modal-header" style="border-color:var(--border);">
            <h5 class="modal-title" style="font-weight:800;"><i class="fas fa-xmark me-2" style="color:#dc2626;"></i>Reject Submission</h5>
            <button type="button" class="btn-close" data-bs-dismiss="modal"></button>
          </div>
          <form method="post" action="/manager/submission/reject/{{ s.submission_id }}">
            <div class="modal-body">
              <p style="font-size:13px;color:var(--muted);">{{ s.batch.batch_name if s.batch else '—' }} — {{ s.record_date.strftime('%b %d, %Y') if s.record_date else '—' }}, submitted by {{ s.worker.full_name if s.worker else '—' }}</p>
              <div class="mb-1"><label class="form-label">Reason <span style="font-weight:400;color:var(--muted);">(optional)</span></label>
                <textarea name="review_notes" class="form-control" rows="2" placeholder="e.g. Weight looks off, please re-check"></textarea>
              </div>
            </div>
            <div class="modal-footer" style="border-color:var(--border);">
              <button type="button" class="btn-ghost" data-bs-dismiss="modal">Cancel</button>
              <button type="submit" class="btn-farm" style="background:#dc2626;border-color:#dc2626;">Reject</button>
            </div>
          </form>
        </div>
      </div>
    </div>
    {% endfor %}

    <!-- ==================== EXPENSES — REVISED ==================== -->
    <div id="mgr-expenses" class="tab-content">

      <div class="stat-grid mb-4">
        <div class="stat-card" style="background:linear-gradient(135deg,#0369a1,#0ea5e9);">
          <div class="sc-icon"><i class="fas fa-droplet"></i></div>
          <div class="sc-label">Water</div>
          <div class="sc-value">₱{{ "{:,.0f}".format(expense_summary.water) }}</div>
        </div>
        <div class="stat-card" style="background:linear-gradient(135deg,#b45309,#facc15);">
          <div class="sc-icon"><i class="fas fa-bolt"></i></div>
          <div class="sc-label">Electricity</div>
          <div class="sc-value">₱{{ "{:,.0f}".format(expense_summary.electricity) }}</div>
        </div>
        <div class="stat-card" style="background:linear-gradient(135deg,#a16207,#d97706);">
          <div class="sc-icon"><i class="fas fa-fire"></i></div>
          <div class="sc-label">LPG</div>
          <div class="sc-value">₱{{ "{:,.0f}".format(expense_summary.lpg) }}</div>
        </div>
        <div class="stat-card" style="background:linear-gradient(135deg,#5b21b6,#7c3aed);">
          <div class="sc-icon"><i class="fas fa-people-carry-box"></i></div>
          <div class="sc-label">Labor</div>
          <div class="sc-value">₱{{ "{:,.0f}".format(expense_summary.labor) }}</div>
        </div>
        <div class="stat-card" style="background:linear-gradient(135deg,#0f766e,#14b8a6);">
          <div class="sc-icon"><i class="fas fa-syringe"></i></div>
          <div class="sc-label">Vaccine</div>
          <div class="sc-value">₱{{ "{:,.0f}".format(expense_summary.vaccine) }}</div>
        </div>
        <div class="stat-card" style="background:linear-gradient(135deg,#9f1239,#be123c);">
          <div class="sc-icon"><i class="fas fa-wheat-awn"></i></div>
          <div class="sc-label">Feed</div>
          <div class="sc-value">₱{{ "{:,.0f}".format(expense_summary.feed) }}</div>
        </div>
        <div class="stat-card" style="background:linear-gradient(135deg,#7c2d12,#c2410c);">
          <div class="sc-icon"><i class="fas fa-file-invoice-dollar"></i></div>
          <div class="sc-label">Total</div>
          <div class="sc-value">₱{{ "{:,.0f}".format(expense_summary.total) }}</div>
        </div>
      </div>

      <div class="card mb-4">
        <div class="card-header-custom">
          <div class="section-header" style="margin:0;">
            <div class="section-divider"></div>
            <h5><i class="fas fa-chart-pie me-2" style="color:var(--accent);"></i>Expense Breakdown</h5>
          </div>
        </div>
        <div class="card-body-custom">
          {% if expense_summary.total > 0 %}
          <div style="display:flex;flex-wrap:wrap;align-items:center;gap:28px;">
            <div class="chart-container-sm" style="max-width:280px;flex:1 1 240px;">
              <canvas id="expensePieChart"></canvas>
            </div>
            <div style="flex:1 1 200px;display:flex;flex-direction:column;gap:10px;">
              <div style="display:flex;align-items:center;gap:8px;font-size:13px;"><span style="width:12px;height:12px;border-radius:3px;background:#0ea5e9;display:inline-block;"></span> Water — ₱{{ "{:,.0f}".format(expense_summary.water) }}</div>
              <div style="display:flex;align-items:center;gap:8px;font-size:13px;"><span style="width:12px;height:12px;border-radius:3px;background:#facc15;display:inline-block;"></span> Electricity — ₱{{ "{:,.0f}".format(expense_summary.electricity) }}</div>
              <div style="display:flex;align-items:center;gap:8px;font-size:13px;"><span style="width:12px;height:12px;border-radius:3px;background:#d97706;display:inline-block;"></span> LPG — ₱{{ "{:,.0f}".format(expense_summary.lpg) }}</div>
              <div style="display:flex;align-items:center;gap:8px;font-size:13px;"><span style="width:12px;height:12px;border-radius:3px;background:#7c3aed;display:inline-block;"></span> Labor — ₱{{ "{:,.0f}".format(expense_summary.labor) }}</div>
              <div style="display:flex;align-items:center;gap:8px;font-size:13px;"><span style="width:12px;height:12px;border-radius:3px;background:#14b8a6;display:inline-block;"></span> Vaccine — ₱{{ "{:,.0f}".format(expense_summary.vaccine) }}</div>
              <div style="display:flex;align-items:center;gap:8px;font-size:13px;"><span style="width:12px;height:12px;border-radius:3px;background:#be123c;display:inline-block;"></span> Feed — ₱{{ "{:,.0f}".format(expense_summary.feed) }}</div>
              <div style="display:flex;align-items:center;gap:8px;font-size:13px;"><span style="width:12px;height:12px;border-radius:3px;background:#c2410c;display:inline-block;"></span> Other — ₱{{ "{:,.0f}".format(expense_summary.other) }}</div>
            </div>
          </div>
          <script>
          (function(){
            var el = document.getElementById('expensePieChart');
            if (el && window.Chart) {
              new Chart(el, {
                type: 'pie',
                data: {
                  labels: ['Water', 'Electricity', 'LPG', 'Labor', 'Vaccine', 'Feed', 'Other'],
                  datasets: [{
                    data: [{{ expense_summary.water }}, {{ expense_summary.electricity }}, {{ expense_summary.lpg }}, {{ expense_summary.labor }}, {{ expense_summary.vaccine }}, {{ expense_summary.feed }}, {{ expense_summary.other }}],
                    backgroundColor: ['#0ea5e9', '#facc15', '#d97706', '#7c3aed', '#14b8a6', '#be123c', '#c2410c'],
                    borderWidth: 0
                  }]
                },
                options: {
                  responsive: true, maintainAspectRatio: false,
                  plugins: {
                    legend: { display: false },
                    tooltip: {
                      callbacks: {
                        label: function(ctx) {
                          var val = ctx.parsed || 0;
                          var total = ctx.dataset.data.reduce(function(a,b){ return a+b; }, 0);
                          var pct = total > 0 ? ((val/total)*100).toFixed(1) : '0.0';
                          return ctx.label + ': ₱' + val.toLocaleString(undefined,{minimumFractionDigits:0,maximumFractionDigits:0}) + ' (' + pct + '%)';
                        }
                      }
                    }
                  }
                }
              });
            }
          })();
          </script>
          {% else %}
          <div class="text-center py-4" style="color:var(--muted);">
            <i class="fas fa-chart-pie fa-2x mb-2 d-block"></i>
            No expenses logged yet.
          </div>
          {% endif %}
        </div>
      </div>

      <div class="card mb-4">
        <div class="card-header-custom">
          <div class="section-header" style="margin:0;">
            <div class="section-divider"></div>
            <h5><i class="fas fa-layer-group me-2" style="color:var(--accent);"></i>Spending by Category — {{ category_spending.month_label }}</h5>
          </div>
          <form method="get" style="display:flex;gap:8px;align-items:center;">
            <input type="month" name="month" class="form-control" style="width:170px;" value="{{ category_spending.month_value }}" onchange="this.form.submit()">
          </form>
        </div>
        <div class="card-body-custom">
          {% if category_spending.rows %}
          <div class="table-responsive">
            <table class="table table-hover align-middle">
              <thead><tr><th>Category</th><th>Total Spent</th></tr></thead>
              <tbody>
              {% for r in category_spending.rows %}
              <tr>
                <td style="font-weight:600;">{{ r.category }}</td>
                <td style="font-weight:700;">₱{{ "{:,.2f}".format(r.total) }}</td>
              </tr>
              {% endfor %}
              <tr style="border-top:2px solid var(--border);">
                <td style="font-weight:800;">Total</td>
                <td style="font-weight:800;">₱{{ "{:,.2f}".format(category_spending.grand_total) }}</td>
              </tr>
              </tbody>
            </table>
          </div>
          {% else %}
          <div class="text-center py-3" style="color:var(--muted);font-size:13px;">No expenses logged for {{ category_spending.month_label }}.</div>
          {% endif %}
        </div>
      </div>

      <div class="card mb-4">
        <div class="card-header-custom">
          <div class="section-header" style="margin:0;">
            <div class="section-divider"></div>
            <h5><i class="fas fa-tags me-2" style="color:var(--accent);"></i>Expense Categories</h5>
          </div>
          <button class="btn-farm" data-bs-toggle="modal" data-bs-target="#addCategoryModal" style="font-size:13px;padding:7px 14px;">
            <i class="fas fa-plus me-1"></i> Add Category
          </button>
        </div>
        <div class="card-body-custom">
          <div style="font-size:12px;color:var(--muted);margin-bottom:10px;">
            Custom categories for "Other" expenses. Water, Electricity, LPG, and Labor are tagged automatically.
          </div>
          <div style="display:flex;flex-wrap:wrap;gap:8px;">
            {% set system_cats = ['water', 'electricity', 'lpg', 'labor', 'vaccine', 'feed'] %}
            {% for c in expense_categories if c.category_name|lower not in system_cats %}
            <form method="post" action="/owner/expense-category/delete/{{ c.expense_category_id }}" onsubmit="return confirm('Delete category {{ c.category_name }}?')" style="display:inline-flex;align-items:center;gap:6px;background:var(--sidebar-hover);border-radius:20px;padding:5px 6px 5px 14px;font-size:13px;font-weight:600;">
              {{ c.category_name }}
              <button type="submit" class="btn-sm-icon btn-del" style="width:22px;height:22px;font-size:10px;"><i class="fas fa-xmark"></i></button>
            </form>
            {% else %}
            <span style="color:var(--muted);font-size:13px;">No custom categories yet.</span>
            {% endfor %}
          </div>
        </div>
      </div>

      <!-- Standard expense cards -->
      <div class="analytics-grid">
        <div class="card">
          <div class="card-header-custom">
            <div class="section-header" style="margin:0;"><div class="section-divider"></div>
              <h5><i class="fas fa-droplet me-2" style="color:#0369a1;"></i>Water Expenses</h5></div>
            <button class="btn-farm" data-bs-toggle="modal" data-bs-target="#addWaterModal" style="font-size:12px;padding:6px 12px;"><i class="fas fa-plus me-1"></i> Add</button>
          </div>
          <div class="card-body-custom input-table-section">
            <table class="table table-hover align-middle">
              <thead><tr><th>Date</th><th>Amount</th><th>Status</th><th></th></tr></thead>
              <tbody>
              {% for e in water_expenses %}
              <tr>
                <td style="font-size:13px;color:var(--muted);">{{ e.expense_date.strftime('%b %d, %Y') if e.expense_date else '—' }}</td>
                <td style="font-weight:700;">₱{{ "%.2f"|format(e.water_expense_amount) }}</td>
                <td><form method="post" action="/owner/expense/water/toggle/{{ e.expense_id }}"><button type="submit" class="status-pill {{ 'status-paid' if e.water_expense_status == 'Paid' else 'status-pending' }}" style="border:none;cursor:pointer;">{{ e.water_expense_status }}</button></form></td>
                <td><form method="post" action="/owner/expense/water/delete/{{ e.expense_id }}"><button class="btn-sm-icon btn-del"><i class="fas fa-trash"></i></button></form></td>
              </tr>
              {% else %}<tr><td colspan="4" class="text-center py-3" style="color:var(--muted);font-size:13px;">No water expenses logged.</td></tr>{% endfor %}
              </tbody>
            </table>
          </div>
        </div>

        <div class="card">
          <div class="card-header-custom">
            <div class="section-header" style="margin:0;"><div class="section-divider"></div>
              <h5><i class="fas fa-bolt me-2" style="color:#b45309;"></i>Electricity Expenses</h5></div>
            <button class="btn-farm" data-bs-toggle="modal" data-bs-target="#addElectricityModal" style="font-size:12px;padding:6px 12px;"><i class="fas fa-plus me-1"></i> Add</button>
          </div>
          <div class="card-body-custom input-table-section">
            <table class="table table-hover align-middle">
              <thead><tr><th>Date</th><th>Amount</th><th>Status</th><th></th></tr></thead>
              <tbody>
              {% for e in electricity_expenses %}
              <tr>
                <td style="font-size:13px;color:var(--muted);">{{ e.expense_date.strftime('%b %d, %Y') if e.expense_date else '—' }}</td>
                <td style="font-weight:700;">₱{{ "%.2f"|format(e.electricity_expense_amount) }}</td>
                <td><form method="post" action="/owner/expense/electricity/toggle/{{ e.expense_id }}"><button type="submit" class="status-pill {{ 'status-paid' if e.electricity_expense_status == 'Paid' else 'status-pending' }}" style="border:none;cursor:pointer;">{{ e.electricity_expense_status }}</button></form></td>
                <td><form method="post" action="/owner/expense/electricity/delete/{{ e.expense_id }}"><button class="btn-sm-icon btn-del"><i class="fas fa-trash"></i></button></form></td>
              </tr>
              {% else %}<tr><td colspan="4" class="text-center py-3" style="color:var(--muted);font-size:13px;">No electricity expenses logged.</td></tr>{% endfor %}
              </tbody>
            </table>
          </div>
        </div>
      </div>

      <div class="analytics-grid mt-4">
        <div class="card">
          <div class="card-header-custom">
            <div class="section-header" style="margin:0;"><div class="section-divider"></div>
              <h5><i class="fas fa-fire me-2" style="color:#a16207;"></i>LPG Expenses</h5></div>
            <button class="btn-farm" data-bs-toggle="modal" data-bs-target="#addLpgModal" style="font-size:12px;padding:6px 12px;"><i class="fas fa-plus me-1"></i> Add</button>
          </div>
          <div class="card-body-custom input-table-section">
            <table class="table table-hover align-middle">
              <thead><tr><th>Date</th><th>Amount</th><th>Provider</th><th>Status</th><th></th></tr></thead>
              <tbody>
              {% for e in lpg_expenses %}
              <tr>
                <td style="font-size:13px;color:var(--muted);">{{ e.expense_date.strftime('%b %d, %Y') if e.expense_date else '—' }}</td>
                <td style="font-weight:700;">₱{{ "%.2f"|format(e.lpg_expense_amount) }}</td>
                <td style="font-size:13px;color:var(--muted);">{{ e.lpg_provider or '—' }}</td>
                <td><form method="post" action="/owner/expense/lpg/toggle/{{ e.expense_id }}"><button type="submit" class="status-pill {{ 'status-paid' if e.lpg_expense_status == 'Paid' else 'status-pending' }}" style="border:none;cursor:pointer;">{{ e.lpg_expense_status }}</button></form></td>
                <td><form method="post" action="/owner/expense/lpg/delete/{{ e.expense_id }}"><button class="btn-sm-icon btn-del"><i class="fas fa-trash"></i></button></form></td>
              </tr>
              {% else %}<tr><td colspan="5" class="text-center py-3" style="color:var(--muted);font-size:13px;">No LPG expenses logged.</td></tr>{% endfor %}
              </tbody>
            </table>
          </div>
        </div>

        <div class="card">
          <div class="card-header-custom">
            <div class="section-header" style="margin:0;"><div class="section-divider"></div>
              <h5><i class="fas fa-people-carry-box me-2" style="color:#7c3aed;"></i>Labor Expenses</h5></div>
            <button class="btn-farm" data-bs-toggle="modal" data-bs-target="#addLaborModal" style="font-size:12px;padding:6px 12px;"><i class="fas fa-plus me-1"></i> Add</button>
          </div>
          <div class="card-body-custom input-table-section">
            <table class="table table-hover align-middle">
              <thead><tr><th>Date</th><th>Amount</th><th>Status</th><th></th></tr></thead>
              <tbody>
              {% for e in labor_expenses %}
              <tr>
                <td style="font-size:13px;color:var(--muted);">{{ e.expense_date.strftime('%b %d, %Y') if e.expense_date else '—' }}</td>
                <td style="font-weight:700;">₱{{ "%.2f"|format(e.labor_expense_amount) }}</td>
                <td><form method="post" action="/owner/expense/labor/toggle/{{ e.expense_id }}"><button type="submit" class="status-pill {{ 'status-paid' if e.labor_expense_status == 'Paid' else 'status-pending' }}" style="border:none;cursor:pointer;">{{ e.labor_expense_status }}</button></form></td>
                <td><form method="post" action="/owner/expense/labor/delete/{{ e.expense_id }}"><button class="btn-sm-icon btn-del"><i class="fas fa-trash"></i></button></form></td>
              </tr>
              {% else %}<tr><td colspan="4" class="text-center py-3" style="color:var(--muted);font-size:13px;">No labor expenses logged.</td></tr>{% endfor %}
              </tbody>
            </table>
          </div>
        </div>
      </div>

      <!-- Vaccine & Feed expense cards -->
      <div class="analytics-grid mt-4">
        <div class="card">
          <div class="card-header-custom">
            <div class="section-header" style="margin:0;"><div class="section-divider"></div>
              <h5><i class="fas fa-syringe me-2" style="color:#0f766e;"></i>Vaccine Expenses</h5></div>
          </div>
          <div class="card-body-custom input-table-section">
            <div style="font-size:12px;color:var(--muted);margin-bottom:10px;">
              Auto-logged when a vaccination is marked as administered.
            </div>
            <table class="table table-hover align-middle">
              <thead><tr><th>Date</th><th>Description</th><th>Amount</th><th>Status</th></tr></thead>
              <tbody>
              {% for e in vaccine_expenses %}
              <tr>
                <td style="font-size:13px;color:var(--muted);">{{ e.expense_date.strftime('%b %d, %Y') if e.expense_date else '—' }}</td>
                <td style="font-size:13px;">{{ e.description or '—' }}</td>
                <td style="font-weight:700;">₱{{ "%.2f"|format(e.vaccine_expense_amount) }}</td>
                <td><span class="status-pill {{ 'status-paid' if e.vaccine_expense_status == 'Paid' else 'status-pending' }}">{{ e.vaccine_expense_status }}</span></td>
              </tr>
              {% else %}<tr><td colspan="4" class="text-center py-3" style="color:var(--muted);font-size:13px;">No vaccine expenses logged.</td></tr>{% endfor %}
              </tbody>
            </table>
          </div>
        </div>

        <div class="card">
          <div class="card-header-custom">
            <div class="section-header" style="margin:0;"><div class="section-divider"></div>
              <h5><i class="fas fa-wheat-awn me-2" style="color:#be123c;"></i>Feed Expenses</h5></div>
          </div>
          <div class="card-body-custom input-table-section">
            <div style="font-size:12px;color:var(--muted);margin-bottom:10px;">
              Auto-logged when a verified daily record includes feed.
            </div>
            <table class="table table-hover align-middle">
              <thead><tr><th>Date</th><th>Description</th><th>Amount</th><th>Status</th></tr></thead>
              <tbody>
              {% for e in feed_expenses %}
              <tr>
                <td style="font-size:13px;color:var(--muted);">{{ e.expense_date.strftime('%b %d, %Y') if e.expense_date else '—' }}</td>
                <td style="font-size:13px;">{{ e.description or '—' }}</td>
                <td style="font-weight:700;">₱{{ "%.2f"|format(e.feed_expense_amount) }}</td>
                <td><span class="status-pill {{ 'status-paid' if e.feed_expense_status == 'Paid' else 'status-pending' }}">{{ e.feed_expense_status }}</span></td>
              </tr>
              {% else %}<tr><td colspan="4" class="text-center py-3" style="color:var(--muted);font-size:13px;">No feed expenses logged.</td></tr>{% endfor %}
              </tbody>
            </table>
          </div>
        </div>
      </div>

      <!-- Dynamic Other Expense cards grouped by category -->
      <div class="mt-4">
        <div class="section-header">
          <div class="section-divider"></div>
          <h5><i class="fas fa-sack-dollar me-2" style="color:#c2410c;"></i>Other Expenses by Category</h5>
          <button class="btn-farm ms-auto" data-bs-toggle="modal" data-bs-target="#addOtherModal" style="font-size:12px;padding:6px 12px;"><i class="fas fa-plus me-1"></i> Add</button>
        </div>

        {% if other_by_category %}
        <div class="row g-4">
          {% for cat_name, expenses in other_by_category.items() %}
          <div class="col-md-6">
            <div class="card">
              <div class="card-header-custom">
                <div class="section-header" style="margin:0;">
                  <div class="section-divider"></div>
                  <h5 style="font-size:14px;"><i class="fas fa-tag me-2" style="color:#c2410c;"></i>{{ cat_name }}</h5>
                </div>
                <span style="font-size:12px;color:var(--muted);">
                  Total: ₱{{ "{:,.2f}".format(expenses|sum(attribute='other_expense_amount')) }}
                </span>
              </div>
              <div class="card-body-custom input-table-section">
                <table class="table table-hover align-middle">
                  <thead><tr><th>Date</th><th>Amount</th><th>Status</th><th></th></tr></thead>
                  <tbody>
                  {% for e in expenses %}
                  <tr>
                    <td style="font-size:13px;color:var(--muted);">{{ e.expense_date.strftime('%b %d, %Y') if e.expense_date else '—' }}</td>
                    <td style="font-weight:700;">₱{{ "%.2f"|format(e.other_expense_amount) }}</td>
                    <td><form method="post" action="/owner/expense/other/toggle/{{ e.expense_id }}"><button type="submit" class="status-pill {{ 'status-paid' if e.other_expense_status == 'Paid' else 'status-pending' }}" style="border:none;cursor:pointer;">{{ e.other_expense_status }}</button></form></td>
                    <td><form method="post" action="/owner/expense/other/delete/{{ e.expense_id }}"><button class="btn-sm-icon btn-del"><i class="fas fa-trash"></i></button></form></td>
                  </tr>
                  {% endfor %}
                  </tbody>
                </table>
              </div>
            </div>
          </div>
          {% endfor %}
        </div>
        {% else %}
        <div class="card">
          <div class="card-body-custom text-center py-4" style="color:var(--muted);font-size:13px;">
            <i class="fas fa-sack-dollar fa-2x mb-2 d-block"></i>
            No other expenses logged yet.
          </div>
        </div>
        {% endif %}
      </div>
    </div>

    <!-- ==================== VACCINATION MANAGEMENT ==================== -->
    <div id="vaccination-mgmt" class="tab-content">
      <div class="card mb-4">
        <div class="card-header-custom">
          <div class="section-header" style="margin:0;">
            <div class="section-divider"></div>
            <h5><i class="fas fa-vial-circle-check me-2" style="color:var(--accent);"></i>Vaccination Inventory</h5>
          </div>
          <button class="btn-farm" data-bs-toggle="modal" data-bs-target="#addVaccineModal" style="font-size:13px;padding:7px 14px;">
            <i class="fas fa-plus me-1"></i> Add Vaccine
          </button>
        </div>
        <div class="card-body-custom">
          <div class="table-responsive">
            <table class="table table-hover align-middle">
              <thead><tr><th>Vaccine</th><th>Type</th><th>Expiry</th><th>mL / Bottle</th><th>Bottles Left</th><th>Cost / Bottle</th><th>Actions</th></tr></thead>
              <tbody>
              {% for v in vaccines %}
              <tr>
                <td style="font-weight:700;">{{ v.vaccine_name }}</td>
                <td>{{ v.vaccine_type or '—' }}</td>
                <td style="font-size:13px;color:var(--muted);">{{ v.vaccine_exp_date.strftime('%b %d, %Y') if v.vaccine_exp_date else '—' }}</td>
                <td>{{ v.milliliters_per_bottle }}</td>
                <td>
                  {% if v.remaining_quantity <= 2 %}
                  <span class="status-pill status-missed"><i class="fas fa-triangle-exclamation"></i> {{ v.remaining_quantity }} left</span>
                  {% else %}{{ v.remaining_quantity }}{% endif %}
                </td>
                <td style="font-weight:700;color:#0f766e;">₱{{ "%.2f"|format(v.cost_per_bottle or 0) }}</td>
                <td>
                  <div class="tbl-actions">
                    <button class="btn-sm-icon btn-edit" data-bs-toggle="modal" data-bs-target="#editVaccineModal{{ v.vaccine_id }}"><i class="fas fa-pen"></i></button>
                    <form method="post" action="/manager/vaccine/delete/{{ v.vaccine_id }}" onsubmit="return confirm('Remove {{ v.vaccine_name }}?')">
                      <button class="btn-sm-icon btn-del" type="submit"><i class="fas fa-trash"></i></button>
                    </form>
                  </div>
                </td>
              </tr>
              {% else %}
              <tr><td colspan="7" class="text-center py-4" style="color:var(--muted);">No vaccines in inventory yet.</td></tr>
              {% endfor %}
              </tbody>
            </table>
          </div>
        </div>
      </div>

      <div class="card">
        <div class="card-header-custom">
          <div class="section-header" style="margin:0;">
            <div class="section-divider"></div>
            <h5><i class="fas fa-calendar-check me-2" style="color:var(--accent);"></i>Vaccination Scheduling <span style="font-weight:400;color:var(--muted);font-size:12px;">(Day 12 & Day 16)</span></h5>
          </div>
          <button class="btn-farm" data-bs-toggle="modal" data-bs-target="#scheduleVaccinationModal" style="font-size:13px;padding:7px 14px;" {% if not vaccines %}disabled{% endif %}>
            <i class="fas fa-calendar-plus me-1"></i> Schedule Vaccination
          </button>
        </div>
        <div class="card-body-custom">
          <div class="table-responsive">
            <table class="table table-hover align-middle">
              <thead><tr><th>Batch</th><th>Vaccine</th><th>Dose/Bird</th><th>Scheduled</th><th>Status</th><th>Administered By</th><th>Actions</th></tr></thead>
              <tbody>
              {% for vr in vaccination_records %}
              <tr>
                <td style="font-weight:700;">{{ vr.batch.batch_name if vr.batch else '—' }}</td>
                <td>{{ vr.vaccine.vaccine_name if vr.vaccine else '—' }}</td>
                <td>{{ vr.dose_per_bird }} mL</td>
                <td style="font-size:13px;color:var(--muted);">{{ vr.scheduled_date.strftime('%b %d, %Y %I:%M %p') }}</td>
                <td>
                  {% if vr.status == 'Scheduled' %}<span class="status-pill status-scheduled">Scheduled</span>
                  {% elif vr.status == 'Administered' %}<span class="status-pill status-administered">Administered</span>
                  {% else %}<span class="status-pill status-missed">{{ vr.status }}</span>{% endif %}
                </td>
                <td style="font-size:13px;color:var(--muted);">{{ vr.administered_by or '—' }}</td>
                <td>
                  <div class="tbl-actions">
                    {% if vr.status == 'Scheduled' %}
                    <form method="post" action="/manager/vaccination/administer/{{ vr.vaccination_record_id }}">
                      <button class="btn-sm-icon btn-ok" type="submit" title="Mark administered"><i class="fas fa-check"></i></button>
                    </form>
                    {% endif %}
                    <form method="post" action="/manager/vaccination/delete/{{ vr.vaccination_record_id }}" onsubmit="return confirm('Delete this schedule entry?')">
                      <button class="btn-sm-icon btn-del" type="submit"><i class="fas fa-trash"></i></button>
                    </form>
                  </div>
                </td>
              </tr>
              {% else %}
              <tr><td colspan="7" class="text-center py-4" style="color:var(--muted);">No vaccinations scheduled yet.</td></tr>
              {% endfor %}
              </tbody>
            </table>
          </div>
        </div>
      </div>
    </div>

    <!-- ==================== VITAMINS & MEDICINE ==================== -->
    <div id="vitamin-mgmt" class="tab-content">
      <div class="card mb-4">
        <div class="card-header-custom">
          <div class="section-header" style="margin:0;">
            <div class="section-divider"></div>
            <h5><i class="fas fa-tablets me-2" style="color:var(--accent);"></i>Vitamins Inventory</h5>
          </div>
          <div style="display:flex;gap:10px;flex-wrap:wrap;">
            <div style="position:relative;">
              <i class="fas fa-magnifying-glass" style="position:absolute;left:12px;top:50%;transform:translateY(-50%);color:var(--muted);font-size:13px;"></i>
              <input type="text" id="vitaminSearchInput" class="form-control" style="padding-left:34px;width:220px;" placeholder="Search vitamins..." onkeyup="filterVitaminTable()">
            </div>
            <button class="btn-farm" data-bs-toggle="modal" data-bs-target="#addVitaminModal" style="font-size:13px;padding:7px 14px;">
              <i class="fas fa-plus me-1"></i> Add Vitamin
            </button>
          </div>
        </div>
        <div class="card-body-custom">
          <div class="table-responsive">
            <table class="table table-hover align-middle" id="vitaminTable">
              <thead><tr><th>Vitamin</th><th>Type</th><th>Expiry</th><th>Quantity</th><th>Cost/Unit</th><th>Actions</th></tr></thead>
              <tbody>
              {% for v in vitamins %}
              <tr>
                <td style="font-weight:700;">{{ v.vitamin_name }}</td>
                <td>{{ v.vitamin_type or '—' }}</td>
                <td style="font-size:13px;color:var(--muted);">{{ v.vitamin_exp_date.strftime('%b %d, %Y') if v.vitamin_exp_date else '—' }}</td>
                <td>{{ v.quantity }} {{ v.unit or 'units' }}</td>
                <td style="font-weight:700;color:#0f766e;">₱{{ "%.2f"|format(v.cost_per_unit or 0) }}</td>
                <td>
                  <div class="tbl-actions">
                    <button class="btn-sm-icon btn-edit" data-bs-toggle="modal" data-bs-target="#editVitaminModal{{ v.vitamin_id }}"><i class="fas fa-pen"></i></button>
                    <form method="post" action="/manager/vitamin/delete/{{ v.vitamin_id }}" onsubmit="return confirm('Remove {{ v.vitamin_name }}?')">
                      <button class="btn-sm-icon btn-del" type="submit"><i class="fas fa-trash"></i></button>
                    </form>
                  </div>
                </td>
              </tr>
              {% else %}
              <tr><td colspan="6" class="text-center py-4" style="color:var(--muted);">No vitamins in inventory yet.</td></tr>
              {% endfor %}
              </tbody>
            </table>
          </div>
        </div>
      </div>

      <div class="card mb-4">
        <div class="card-header-custom">
          <div class="section-header" style="margin:0;">
            <div class="section-divider"></div>
            <h5><i class="fas fa-calendar-check me-2" style="color:var(--accent);"></i>Vitamins Scheduling</h5>
          </div>
          <button class="btn-farm" data-bs-toggle="modal" data-bs-target="#scheduleVitaminModal" style="font-size:13px;padding:7px 14px;" {% if not vitamins %}disabled{% endif %}>
            <i class="fas fa-calendar-plus me-1"></i> Schedule Vitamin
          </button>
        </div>
        <div class="card-body-custom">
          <div class="table-responsive">
            <table class="table table-hover align-middle">
              <thead><tr><th>Batch</th><th>Vitamin</th><th>Day Given</th><th>Dosage</th><th>Status</th><th>Actions</th></tr></thead>
              <tbody>
              {% for vs in vitamin_schedules %}
              <tr>
                <td style="font-weight:700;">{{ vs.batch.batch_name if vs.batch else '—' }}</td>
                <td>{{ vs.vitamin.vitamin_name if vs.vitamin else '—' }}</td>
                <td style="font-size:13px;color:var(--muted);">Day {{ vs.day_given }}</td>
                <td>{{ vs.dosage or '—' }}</td>
                <td>
                  {% if vs.status == 'Scheduled' %}<span class="status-pill status-scheduled">Scheduled</span>
                  {% elif vs.status == 'Administered' %}<span class="status-pill status-administered">Administered</span>
                  {% else %}<span class="status-pill status-skipped">{{ vs.status }}</span>{% endif %}
                </td>
                <td>
                  <div class="tbl-actions">
                    {% if vs.status == 'Scheduled' %}
                    <form method="post" action="/manager/vitamin/administer/{{ vs.schedule_id }}">
                      <button class="btn-sm-icon btn-ok" type="submit" title="Mark administered"><i class="fas fa-check"></i></button>
                    </form>
                    {% endif %}
                    <form method="post" action="/manager/vitamin/delete/{{ vs.schedule_id }}" onsubmit="return confirm('Delete this schedule entry?')">
                      <button class="btn-sm-icon btn-del" type="submit"><i class="fas fa-trash"></i></button>
                    </form>
                  </div>
                </td>
              </tr>
              {% else %}
              <tr><td colspan="6" class="text-center py-4" style="color:var(--muted);">No vitamins scheduled yet.</td></tr>
              {% endfor %}
              </tbody>
            </table>
          </div>
        </div>
      </div>

      <div class="card">
        <div class="card-header-custom">
          <div class="section-header" style="margin:0;">
            <div class="section-divider"></div>
            <h5><i class="fas fa-pills me-2" style="color:var(--accent);"></i>Medicine Scheduling</h5>
          </div>
          <button class="btn-farm" data-bs-toggle="modal" data-bs-target="#scheduleMedicineModal" style="font-size:13px;padding:7px 14px;">
            <i class="fas fa-calendar-plus me-1"></i> Schedule Medicine
          </button>
        </div>
        <div class="card-body-custom">
          <div class="table-responsive">
            <table class="table table-hover align-middle">
              <thead><tr><th>Batch</th><th>Medicine</th><th>Dosage</th><th>Scheduled</th><th>Status</th><th>Actions</th></tr></thead>
              <tbody>
              {% for ms in medication_schedules %}
              <tr>
                <td style="font-weight:700;">{{ ms.batch.batch_name if ms.batch else '—' }}</td>
                <td>{{ ms.item_name }}</td>
                <td>{{ ms.dosage or '—' }}</td>
                <td style="font-size:13px;color:var(--muted);">{{ ms.scheduled_date.strftime('%b %d, %Y') }}</td>
                <td>
                  {% if ms.status == 'Scheduled' %}<span class="status-pill status-scheduled">Scheduled</span>
                  {% elif ms.status == 'Administered' %}<span class="status-pill status-administered">Administered</span>
                  {% else %}<span class="status-pill status-skipped">{{ ms.status }}</span>{% endif %}
                </td>
                <td>
                  <div class="tbl-actions">
                    {% if ms.status == 'Scheduled' %}
                    <form method="post" action="/manager/medicine/administer/{{ ms.schedule_id }}">
                      <button class="btn-sm-icon btn-ok" type="submit" title="Mark administered"><i class="fas fa-check"></i></button>
                    </form>
                    {% endif %}
                    <form method="post" action="/manager/medicine/delete/{{ ms.schedule_id }}" onsubmit="return confirm('Delete this schedule entry?')">
                      <button class="btn-sm-icon btn-del" type="submit"><i class="fas fa-trash"></i></button>
                    </form>
                  </div>
                </td>
              </tr>
              {% else %}
              <tr><td colspan="6" class="text-center py-4" style="color:var(--muted);">No medicines scheduled yet.</td></tr>
              {% endfor %}
              </tbody>
            </table>
          </div>
        </div>
      </div>
    </div>

    <!-- ==================== FEED INVENTORY ==================== -->
    <div id="feed-mgmt" class="tab-content">
      <div class="card">
        <div class="card-header-custom">
          <div class="section-header" style="margin:0;">
            <div class="section-divider"></div>
            <h5><i class="fas fa-wheat-awn me-2" style="color:var(--accent);"></i>Feed Inventory</h5>
          </div>
          <div style="display:flex;gap:10px;flex-wrap:wrap;">
            <div style="position:relative;">
              <i class="fas fa-magnifying-glass" style="position:absolute;left:12px;top:50%;transform:translateY(-50%);color:var(--muted);font-size:13px;"></i>
              <input type="text" id="feedSearchInput" class="form-control" style="padding-left:34px;width:220px;" placeholder="Search feed..." onkeyup="filterFeedTable()">
            </div>
            <button class="btn-farm" data-bs-toggle="modal" data-bs-target="#addFeedModal" style="font-size:13px;padding:7px 14px;">
              <i class="fas fa-plus me-1"></i> Add Feed Type
            </button>
          </div>
        </div>
        <div class="card-body-custom">
          <div style="font-size:12px;color:var(--muted);margin-bottom:14px;">
            Three main feed categories: Chick Booster, Grower Pellets, Finisher Pellets. Full nutrient profile shown.
          </div>
          <div class="table-responsive">
            <table class="table table-hover align-middle" id="feedTable">
              <thead><tr>
                <th>Category</th><th>Feed Name</th>
                <th>CP %</th><th>Fat %</th><th>Fiber %</th><th>Moisture %</th><th>Ca %</th><th>P %</th>
                <th>Cost/KG</th><th>Expiration</th><th>Remaining</th><th>Actions</th>
              </tr></thead>
              <tbody>
              {% for f in feed_records %}
              <tr>
                <td><span class="badge {{ 'badge-success' if f.feed_category == 'Chick Booster' else ('badge-warning' if f.feed_category == 'Grower Pellets' else 'badge-info') }}">{{ f.feed_category }}</span></td>
                <td style="font-weight:700;">{{ f.feed_name }}</td>
                <td>{{ f.crude_protein }}%</td>
                <td>{{ f.crude_fat }}%</td>
                <td>{{ f.crude_fiber }}%</td>
                <td>{{ f.moisture }}%</td>
                <td>{{ f.calcium }}%</td>
                <td>{{ f.phosphorus }}%</td>
                <td>₱{{ "%.2f"|format(f.cost_per_kg) }}</td>
                <td style="font-size:13px;color:var(--muted);">{{ f.expiration_date.strftime('%b %d, %Y') if f.expiration_date else '—' }}</td>
                <td>
                  {% if f.remaining_quantity <= 50 %}
                  <span class="status-pill status-missed">{{ f.remaining_quantity }} kg</span>
                  {% else %}{{ f.remaining_quantity }} kg{% endif %}
                </td>
                <td>
                  <div class="tbl-actions">
                    <button class="btn-sm-icon btn-edit" data-bs-toggle="modal" data-bs-target="#editFeedModal{{ f.feed_record_id }}"><i class="fas fa-pen"></i></button>
                    <form method="post" action="/manager/feed/delete/{{ f.feed_record_id }}" onsubmit="return confirm('Remove {{ f.feed_name }}?')">
                      <button class="btn-sm-icon btn-del" type="submit"><i class="fas fa-trash"></i></button>
                    </form>
                  </div>
                </td>
              </tr>
              {% else %}
              <tr><td colspan="12" class="text-center py-4" style="color:var(--muted);">No feed types added yet.</td></tr>
              {% endfor %}
              </tbody>
            </table>
          </div>
        </div>
      </div>
    </div>

    <!-- ==================== REPORTS ==================== -->
    <div id="mgr-reports" class="tab-content">
      <div class="card">
        <div class="card-header-custom">
          <div class="section-header" style="margin:0;">
            <div class="section-divider"></div>
            <h5><i class="fas fa-file-alt me-2" style="color:var(--accent);"></i>Submit Performance Report</h5>
          </div>
        </div>
        <div class="card-body-custom">
          <div style="font-size:12px;color:var(--muted);margin-bottom:14px;">
            Select the batch and choose which fields to include in the report.
          </div>
          <div class="row g-3 mb-4">
            <div class="col-md-6">
              <label class="form-label">Select Harvested Batch</label>
              <select id="mgrReportBatchSelect" class="form-select">
                <option value="">— Select a harvested batch —</option>
                {% for h in harvest_history %}
                <option value="{{ h.id }}">{{ h.batch_name }} ({{ h.end_date.strftime('%b %d, %Y') if h.end_date else '—' }})</option>
                {% endfor %}
              </select>
            </div>
            <div class="col-md-6 d-flex align-items-end">
              <button type="button" class="btn-farm w-100" onclick="openMgrReport()">
                <i class="fas fa-eye me-1"></i> Preview & Submit Report
              </button>
            </div>
          </div>
        </div>
      </div>
    </div>

  </div></div></div>

<!-- ==================== MODALS ==================== -->

<!-- Add Vaccine Modal -->
<div class="modal fade" id="addVaccineModal" tabindex="-1">
  <div class="modal-dialog modal-dialog-centered">
    <div class="modal-content" style="background:var(--card-bg);border:1px solid var(--border);border-radius:16px;">
      <div class="modal-header" style="border-color:var(--border);">
        <h5 class="modal-title" style="font-weight:800;"><i class="fas fa-vial-circle-check me-2" style="color:var(--accent);"></i>Add Vaccine</h5>
        <button type="button" class="btn-close" data-bs-dismiss="modal"></button>
      </div>
      <form method="post" action="/manager/vaccine/add">
        <div class="modal-body">
          <div class="mb-3"><label class="form-label">Vaccine Name</label><input name="vaccine_name" class="form-control" placeholder="e.g. Newcastle Disease Vaccine" required></div>
          <div class="row g-2 mb-3">
            <div class="col-6"><label class="form-label">Type</label><input name="vaccine_type" class="form-control" placeholder="e.g. Live, Killed"></div>
            <div class="col-6"><label class="form-label">Expiry Date</label><input type="date" name="vaccine_exp_date" class="form-control"></div>
          </div>
          <div class="row g-2 mb-3">
            <div class="col-6"><label class="form-label">mL / Bottle</label><input type="number" step="0.01" name="milliliters_per_bottle" class="form-control" placeholder="0"></div>
            <div class="col-6"><label class="form-label">Bottles in Stock</label><input type="number" step="0.01" name="remaining_quantity" class="form-control" placeholder="0"></div>
          </div>
          <div class="mb-1"><label class="form-label">Cost per Bottle (₱)</label>
            <input type="number" step="0.01" name="cost_per_bottle" class="form-control" placeholder="0">
            <small style="color:var(--muted);">Used to auto-compute vaccine expenses when administered.</small>
          </div>
        </div>
        <div class="modal-footer" style="border-color:var(--border);">
          <button type="button" class="btn-ghost" data-bs-dismiss="modal">Cancel</button>
          <button type="submit" class="btn-farm">Add Vaccine</button>
        </div>
      </form>
    </div>
  </div>
</div>

<!-- Edit Vaccine Modals -->
{% for v in vaccines %}
<div class="modal fade" id="editVaccineModal{{ v.vaccine_id }}" tabindex="-1">
  <div class="modal-dialog modal-dialog-centered">
    <div class="modal-content" style="background:var(--card-bg);border:1px solid var(--border);border-radius:16px;">
      <div class="modal-header" style="border-color:var(--border);">
        <h5 class="modal-title" style="font-weight:800;">Edit: {{ v.vaccine_name }}</h5>
        <button type="button" class="btn-close" data-bs-dismiss="modal"></button>
      </div>
      <form method="post" action="/manager/vaccine/edit/{{ v.vaccine_id }}">
        <div class="modal-body">
          <div class="mb-3"><label class="form-label">Vaccine Name</label><input name="vaccine_name" class="form-control" value="{{ v.vaccine_name }}" required></div>
          <div class="row g-2 mb-3">
            <div class="col-6"><label class="form-label">Type</label><input name="vaccine_type" class="form-control" value="{{ v.vaccine_type or '' }}"></div>
            <div class="col-6"><label class="form-label">Expiry Date</label><input type="date" name="vaccine_exp_date" class="form-control" value="{{ v.vaccine_exp_date.strftime('%Y-%m-%d') if v.vaccine_exp_date else '' }}"></div>
          </div>
          <div class="row g-2 mb-3">
            <div class="col-6"><label class="form-label">mL / Bottle</label><input type="number" step="0.01" name="milliliters_per_bottle" class="form-control" value="{{ v.milliliters_per_bottle }}"></div>
            <div class="col-6"><label class="form-label">Bottles in Stock</label><input type="number" step="0.01" name="remaining_quantity" class="form-control" value="{{ v.remaining_quantity }}"></div>
          </div>
          <div class="mb-1"><label class="form-label">Cost per Bottle (₱)</label><input type="number" step="0.01" name="cost_per_bottle" class="form-control" value="{{ v.cost_per_bottle or 0 }}"></div>
        </div>
        <div class="modal-footer" style="border-color:var(--border);">
          <button type="button" class="btn-ghost" data-bs-dismiss="modal">Cancel</button>
          <button type="submit" class="btn-farm">Save Changes</button>
        </div>
      </form>
    </div>
  </div>
</div>
{% endfor %}

<!-- Schedule Vaccination Modal -->
<div class="modal fade" id="scheduleVaccinationModal" tabindex="-1">
  <div class="modal-dialog modal-dialog-centered">
    <div class="modal-content" style="background:var(--card-bg);border:1px solid var(--border);border-radius:16px;">
      <div class="modal-header" style="border-color:var(--border);">
        <h5 class="modal-title" style="font-weight:800;"><i class="fas fa-calendar-plus me-2" style="color:var(--accent);"></i>Schedule Vaccination</h5>
        <button type="button" class="btn-close" data-bs-dismiss="modal"></button>
      </div>
      <form method="post" action="/manager/vaccination/schedule">
        <div class="modal-body">
          <div class="row g-2 mb-3">
            <div class="col-6"><label class="form-label">Flock Batch</label>
              <select name="batch_id" class="form-select" required>
                {% for f in active_flocks %}<option value="{{ f.batch_id }}">{{ f.batch_name }}</option>{% endfor %}
              </select>
            </div>
            <div class="col-6"><label class="form-label">Vaccine</label>
              <select name="vaccine_id" class="form-select" required>
                {% for v in vaccines %}<option value="{{ v.vaccine_id }}">{{ v.vaccine_name }}</option>{% endfor %}
              </select>
            </div>
          </div>
          <div class="row g-2 mb-3">
            <div class="col-6"><label class="form-label">Dose / Bird (mL)</label><input type="number" step="0.01" name="dose_per_bird" class="form-control" placeholder="0"></div>
            <div class="col-6"><label class="form-label">Day (12 or 16)</label>
              <select name="vaccine_day" class="form-select">
                <option value="12">Day 12</option>
                <option value="16">Day 16</option>
              </select>
            </div>
          </div>
          <div class="mb-1"><label class="form-label">Scheduled Date & Time</label><input type="datetime-local" name="scheduled_date" class="form-control" required></div>
        </div>
        <div class="modal-footer" style="border-color:var(--border);">
          <button type="button" class="btn-ghost" data-bs-dismiss="modal">Cancel</button>
          <button type="submit" class="btn-farm">Schedule</button>
        </div>
      </form>
    </div>
  </div>
</div>

<!-- Add Vitamin Modal -->
<div class="modal fade" id="addVitaminModal" tabindex="-1">
  <div class="modal-dialog modal-dialog-centered">
    <div class="modal-content" style="background:var(--card-bg);border:1px solid var(--border);border-radius:16px;">
      <div class="modal-header" style="border-color:var(--border);">
        <h5 class="modal-title" style="font-weight:800;"><i class="fas fa-tablets me-2" style="color:var(--accent);"></i>Add Vitamin</h5>
        <button type="button" class="btn-close" data-bs-dismiss="modal"></button>
      </div>
      <form method="post" action="/manager/vitamin/add">
        <div class="modal-body">
          <div class="mb-3"><label class="form-label">Vitamin Name</label><input name="vitamin_name" class="form-control" placeholder="e.g. Vitamin B-Complex" required></div>
          <div class="row g-2 mb-3">
            <div class="col-6"><label class="form-label">Type</label><input name="vitamin_type" class="form-control" placeholder="e.g. Water-soluble"></div>
            <div class="col-6"><label class="form-label">Expiry Date</label><input type="date" name="vitamin_exp_date" class="form-control"></div>
          </div>
          <div class="row g-2 mb-3">
            <div class="col-6"><label class="form-label">Quantity</label><input type="number" step="0.01" name="quantity" class="form-control" placeholder="0"></div>
            <div class="col-6"><label class="form-label">Unit</label><input name="unit" class="form-control" placeholder="e.g. mL, tablets"></div>
          </div>
          <div class="mb-1"><label class="form-label">Cost per Unit (₱)</label><input type="number" step="0.01" name="cost_per_unit" class="form-control" placeholder="0"></div>
        </div>
        <div class="modal-footer" style="border-color:var(--border);">
          <button type="button" class="btn-ghost" data-bs-dismiss="modal">Cancel</button>
          <button type="submit" class="btn-farm">Add Vitamin</button>
        </div>
      </form>
    </div>
  </div>
</div>

<!-- Edit Vitamin Modals -->
{% for v in vitamins %}
<div class="modal fade" id="editVitaminModal{{ v.vitamin_id }}" tabindex="-1">
  <div class="modal-dialog modal-dialog-centered">
    <div class="modal-content" style="background:var(--card-bg);border:1px solid var(--border);border-radius:16px;">
      <div class="modal-header" style="border-color:var(--border);">
        <h5 class="modal-title" style="font-weight:800;">Edit: {{ v.vitamin_name }}</h5>
        <button type="button" class="btn-close" data-bs-dismiss="modal"></button>
      </div>
      <form method="post" action="/manager/vitamin/edit/{{ v.vitamin_id }}">
        <div class="modal-body">
          <div class="mb-3"><label class="form-label">Vitamin Name</label><input name="vitamin_name" class="form-control" value="{{ v.vitamin_name }}" required></div>
          <div class="row g-2 mb-3">
            <div class="col-6"><label class="form-label">Type</label><input name="vitamin_type" class="form-control" value="{{ v.vitamin_type or '' }}"></div>
            <div class="col-6"><label class="form-label">Expiry Date</label><input type="date" name="vitamin_exp_date" class="form-control" value="{{ v.vitamin_exp_date.strftime('%Y-%m-%d') if v.vitamin_exp_date else '' }}"></div>
          </div>
          <div class="row g-2 mb-3">
            <div class="col-6"><label class="form-label">Quantity</label><input type="number" step="0.01" name="quantity" class="form-control" value="{{ v.quantity }}"></div>
            <div class="col-6"><label class="form-label">Unit</label><input name="unit" class="form-control" value="{{ v.unit or '' }}"></div>
          </div>
          <div class="mb-1"><label class="form-label">Cost per Unit (₱)</label><input type="number" step="0.01" name="cost_per_unit" class="form-control" value="{{ v.cost_per_unit or 0 }}"></div>
        </div>
        <div class="modal-footer" style="border-color:var(--border);">
          <button type="button" class="btn-ghost" data-bs-dismiss="modal">Cancel</button>
          <button type="submit" class="btn-farm">Save Changes</button>
        </div>
      </form>
    </div>
  </div>
</div>
{% endfor %}

<!-- Schedule Vitamin Modal -->
<div class="modal fade" id="scheduleVitaminModal" tabindex="-1">
  <div class="modal-dialog modal-dialog-centered">
    <div class="modal-content" style="background:var(--card-bg);border:1px solid var(--border);border-radius:16px;">
      <div class="modal-header" style="border-color:var(--border);">
        <h5 class="modal-title" style="font-weight:800;"><i class="fas fa-calendar-plus me-2" style="color:var(--accent);"></i>Schedule Vitamin</h5>
        <button type="button" class="btn-close" data-bs-dismiss="modal"></button>
      </div>
      <form method="post" action="/manager/vitamin/schedule">
        <div class="modal-body">
          <div class="row g-2 mb-3">
            <div class="col-6"><label class="form-label">Flock Batch</label>
              <select name="batch_id" class="form-select" required>
                {% for f in active_flocks %}<option value="{{ f.batch_id }}">{{ f.batch_name }}</option>{% endfor %}
              </select>
            </div>
            <div class="col-6"><label class="form-label">Vitamin</label>
              <select name="vitamin_id" class="form-select" required>
                {% for v in vitamins %}<option value="{{ v.vitamin_id }}">{{ v.vitamin_name }}</option>{% endfor %}
              </select>
            </div>
          </div>
          <div class="row g-2">
            <div class="col-6"><label class="form-label">Day Given (e.g. 12)</label><input type="number" name="day_given" class="form-control" placeholder="12" required></div>
            <div class="col-6"><label class="form-label">Dosage</label><input name="dosage" class="form-control" placeholder="e.g. 2mL/L water"></div>
          </div>
        </div>
        <div class="modal-footer" style="border-color:var(--border);">
          <button type="button" class="btn-ghost" data-bs-dismiss="modal">Cancel</button>
          <button type="submit" class="btn-farm">Schedule</button>
        </div>
      </form>
    </div>
  </div>
</div>

<!-- Schedule Medicine Modal -->
<div class="modal fade" id="scheduleMedicineModal" tabindex="-1">
  <div class="modal-dialog modal-dialog-centered">
    <div class="modal-content" style="background:var(--card-bg);border:1px solid var(--border);border-radius:16px;">
      <div class="modal-header" style="border-color:var(--border);">
        <h5 class="modal-title" style="font-weight:800;"><i class="fas fa-pills me-2" style="color:var(--accent);"></i>Schedule Medicine</h5>
        <button type="button" class="btn-close" data-bs-dismiss="modal"></button>
      </div>
      <form method="post" action="/manager/medicine/schedule">
        <div class="modal-body">
          <div class="row g-2 mb-3">
            <div class="col-6"><label class="form-label">Flock Batch</label>
              <select name="batch_id" class="form-select" required>
                {% for f in active_flocks %}<option value="{{ f.batch_id }}">{{ f.batch_name }}</option>{% endfor %}
              </select>
            </div>
            <div class="col-6"><label class="form-label">Medicine Name</label>
              <input name="item_name" class="form-control" placeholder="e.g. Amoxicillin" required>
            </div>
          </div>
          <div class="row g-2 mb-3">
            <div class="col-6"><label class="form-label">Dosage</label><input name="dosage" class="form-control" placeholder="e.g. 1g/L water"></div>
            <div class="col-6"><label class="form-label">Scheduled Date</label><input type="date" name="scheduled_date" class="form-control" required></div>
          </div>
          <div class="mb-1"><label class="form-label">Notes</label><input name="notes" class="form-control" placeholder="Optional notes"></div>
        </div>
        <div class="modal-footer" style="border-color:var(--border);">
          <button type="button" class="btn-ghost" data-bs-dismiss="modal">Cancel</button>
          <button type="submit" class="btn-farm">Schedule</button>
        </div>
      </form>
    </div>
  </div>
</div>

<!-- Add Feed Modal -->
<div class="modal fade" id="addFeedModal" tabindex="-1">
  <div class="modal-dialog modal-dialog-centered modal-lg">
    <div class="modal-content" style="background:var(--card-bg);border:1px solid var(--border);border-radius:16px;">
      <div class="modal-header" style="border-color:var(--border);">
        <h5 class="modal-title" style="font-weight:800;"><i class="fas fa-wheat-awn me-2" style="color:var(--accent);"></i>Add Feed Type</h5>
        <button type="button" class="btn-close" data-bs-dismiss="modal"></button>
      </div>
      <form method="post" action="/manager/feed/add">
        <div class="modal-body">
          <div class="mb-3"><label class="form-label">Feed Name</label><input name="feed_name" class="form-control" placeholder="e.g. Broiler Starter Mash" required></div>
          <div class="row g-2 mb-3">
            <div class="col-6"><label class="form-label">Category</label>
              <select name="feed_category" class="form-select" required>
                <option value="Chick Booster">Chick Booster</option>
                <option value="Grower Pellets">Grower Pellets</option>
                <option value="Finisher Pellets">Finisher Pellets</option>
              </select>
            </div>
            <div class="col-6"><label class="form-label">Cost / KG (₱)</label>
              <input type="number" step="0.01" name="cost_per_kg" class="form-control" placeholder="0"></div>
          </div>
          <label class="form-label">Nutritional Profile (% each)</label>
          <div class="row g-2 mb-3">
            <div class="col-4"><label class="form-label" style="font-size:11px;">Crude Protein</label><input type="number" step="0.01" name="crude_protein" class="form-control" placeholder="0"></div>
            <div class="col-4"><label class="form-label" style="font-size:11px;">Crude Fat</label><input type="number" step="0.01" name="crude_fat" class="form-control" placeholder="0"></div>
            <div class="col-4"><label class="form-label" style="font-size:11px;">Crude Fiber</label><input type="number" step="0.01" name="crude_fiber" class="form-control" placeholder="0"></div>
            <div class="col-4"><label class="form-label" style="font-size:11px;">Moisture</label><input type="number" step="0.01" name="moisture" class="form-control" placeholder="0"></div>
            <div class="col-4"><label class="form-label" style="font-size:11px;">Calcium</label><input type="number" step="0.01" name="calcium" class="form-control" placeholder="0"></div>
            <div class="col-4"><label class="form-label" style="font-size:11px;">Phosphorus</label><input type="number" step="0.01" name="phosphorus" class="form-control" placeholder="0"></div>
          </div>
          <div class="row g-2 mb-3">
            <div class="col-6"><label class="form-label">Remaining (kg)</label><input type="number" step="0.1" name="remaining_quantity" class="form-control" placeholder="0"></div>
            <div class="col-6"><label class="form-label">Expiration Date</label><input type="date" name="expiration_date" class="form-control"></div>
          </div>
        </div>
        <div class="modal-footer" style="border-color:var(--border);">
          <button type="button" class="btn-ghost" data-bs-dismiss="modal">Cancel</button>
          <button type="submit" class="btn-farm">Add Feed</button>
        </div>
      </form>
    </div>
  </div>
</div>

<!-- Edit Feed Modals -->
{% for f in feed_records %}
<div class="modal fade" id="editFeedModal{{ f.feed_record_id }}" tabindex="-1">
  <div class="modal-dialog modal-dialog-centered modal-lg">
    <div class="modal-content" style="background:var(--card-bg);border:1px solid var(--border);border-radius:16px;">
      <div class="modal-header" style="border-color:var(--border);">
        <h5 class="modal-title" style="font-weight:800;">Edit: {{ f.feed_name }}</h5>
        <button type="button" class="btn-close" data-bs-dismiss="modal"></button>
      </div>
      <form method="post" action="/manager/feed/edit/{{ f.feed_record_id }}">
        <div class="modal-body">
          <div class="mb-3"><label class="form-label">Feed Name</label><input name="feed_name" class="form-control" value="{{ f.feed_name }}" required></div>
          <div class="row g-2 mb-3">
            <div class="col-6"><label class="form-label">Category</label>
              <select name="feed_category" class="form-select" required>
                <option value="Chick Booster" {% if f.feed_category == 'Chick Booster' %}selected{% endif %}>Chick Booster</option>
                <option value="Grower Pellets" {% if f.feed_category == 'Grower Pellets' %}selected{% endif %}>Grower Pellets</option>
                <option value="Finisher Pellets" {% if f.feed_category == 'Finisher Pellets' %}selected{% endif %}>Finisher Pellets</option>
              </select>
            </div>
            <div class="col-6"><label class="form-label">Cost / KG (₱)</label><input type="number" step="0.01" name="cost_per_kg" class="form-control" value="{{ f.cost_per_kg }}"></div>
          </div>
          <label class="form-label">Nutritional Profile (% each)</label>
          <div class="row g-2 mb-3">
            <div class="col-4"><label class="form-label" style="font-size:11px;">Crude Protein</label><input type="number" step="0.01" name="crude_protein" class="form-control" value="{{ f.crude_protein }}"></div>
            <div class="col-4"><label class="form-label" style="font-size:11px;">Crude Fat</label><input type="number" step="0.01" name="crude_fat" class="form-control" value="{{ f.crude_fat }}"></div>
            <div class="col-4"><label class="form-label" style="font-size:11px;">Crude Fiber</label><input type="number" step="0.01" name="crude_fiber" class="form-control" value="{{ f.crude_fiber }}"></div>
            <div class="col-4"><label class="form-label" style="font-size:11px;">Moisture</label><input type="number" step="0.01" name="moisture" class="form-control" value="{{ f.moisture }}"></div>
            <div class="col-4"><label class="form-label" style="font-size:11px;">Calcium</label><input type="number" step="0.01" name="calcium" class="form-control" value="{{ f.calcium }}"></div>
            <div class="col-4"><label class="form-label" style="font-size:11px;">Phosphorus</label><input type="number" step="0.01" name="phosphorus" class="form-control" value="{{ f.phosphorus }}"></div>
          </div>
          <div class="row g-2 mb-3">
            <div class="col-6"><label class="form-label">Remaining (kg)</label><input type="number" step="0.1" name="remaining_quantity" class="form-control" value="{{ f.remaining_quantity }}"></div>
            <div class="col-6"><label class="form-label">Expiration Date</label><input type="date" name="expiration_date" class="form-control" value="{{ f.expiration_date.strftime('%Y-%m-%d') if f.expiration_date else '' }}"></div>
          </div>
        </div>
        <div class="modal-footer" style="border-color:var(--border);">
          <button type="button" class="btn-ghost" data-bs-dismiss="modal">Cancel</button>
          <button type="submit" class="btn-farm">Save Changes</button>
        </div>
      </form>
    </div>
  </div>
</div>
{% endfor %}

<!-- Add Category Modal -->
<div class="modal fade" id="addCategoryModal" tabindex="-1">
  <div class="modal-dialog modal-dialog-centered">
    <div class="modal-content" style="background:var(--card-bg);border:1px solid var(--border);border-radius:16px;">
      <div class="modal-header" style="border-color:var(--border);">
        <h5 class="modal-title" style="font-weight:800;">Add Expense Category</h5>
        <button type="button" class="btn-close" data-bs-dismiss="modal"></button>
      </div>
      <form method="post" action="/owner/expense-category/add">
        <div class="modal-body">
          <div class="mb-1"><label class="form-label">Category Name</label><input name="category_name" class="form-control" placeholder="e.g. Utilities" required></div>
        </div>
        <div class="modal-footer" style="border-color:var(--border);">
          <button type="button" class="btn-ghost" data-bs-dismiss="modal">Cancel</button>
          <button type="submit" class="btn-farm">Add</button>
        </div>
      </form>
    </div>
  </div>
</div>

<!-- Add Water Modal -->
<div class="modal fade" id="addWaterModal" tabindex="-1">
  <div class="modal-dialog modal-dialog-centered">
    <div class="modal-content" style="background:var(--card-bg);border:1px solid var(--border);border-radius:16px;">
      <div class="modal-header" style="border-color:var(--border);">
        <h5 class="modal-title" style="font-weight:800;"><i class="fas fa-droplet me-2" style="color:#0369a1;"></i>Add Water Expense</h5>
        <button type="button" class="btn-close" data-bs-dismiss="modal"></button>
      </div>
      <form method="post" action="/owner/expense/water/add">
        <div class="modal-body">
          <div class="row g-2">
            <div class="col-6"><label class="form-label">Amount (₱)</label><input type="number" step="0.01" name="amount" class="form-control" required></div>
            <div class="col-6"><label class="form-label">Status</label>
              <select name="status" class="form-select"><option value="Pending">Pending</option><option value="Paid">Paid</option></select>
            </div>
          </div>
          <div class="mb-1 mt-2"><label class="form-label">Date</label><input type="date" name="expense_date" class="form-control" value="{{ today_str }}"></div>
          <div style="font-size:11px;color:var(--muted);margin-top:8px;"><i class="fas fa-info-circle me-1"></i>Automatically assigned to the current active batch.</div>
        </div>
        <div class="modal-footer" style="border-color:var(--border);">
          <button type="button" class="btn-ghost" data-bs-dismiss="modal">Cancel</button>
          <button type="submit" class="btn-farm">Add</button>
        </div>
      </form>
    </div>
  </div>
</div>

<!-- Add Electricity Modal -->
<div class="modal fade" id="addElectricityModal" tabindex="-1">
  <div class="modal-dialog modal-dialog-centered">
    <div class="modal-content" style="background:var(--card-bg);border:1px solid var(--border);border-radius:16px;">
      <div class="modal-header" style="border-color:var(--border);">
        <h5 class="modal-title" style="font-weight:800;"><i class="fas fa-bolt me-2" style="color:#b45309;"></i>Add Electricity Expense</h5>
        <button type="button" class="btn-close" data-bs-dismiss="modal"></button>
      </div>
      <form method="post" action="/owner/expense/electricity/add">
        <div class="modal-body">
          <div class="row g-2">
            <div class="col-6"><label class="form-label">Amount (₱)</label><input type="number" step="0.01" name="amount" class="form-control" required></div>
            <div class="col-6"><label class="form-label">Status</label>
              <select name="status" class="form-select"><option value="Pending">Pending</option><option value="Paid">Paid</option></select>
            </div>
          </div>
          <div class="mb-1 mt-2"><label class="form-label">Date</label><input type="date" name="expense_date" class="form-control" value="{{ today_str }}"></div>
          <div style="font-size:11px;color:var(--muted);margin-top:8px;"><i class="fas fa-info-circle me-1"></i>Automatically assigned to the current active batch.</div>
        </div>
        <div class="modal-footer" style="border-color:var(--border);">
          <button type="button" class="btn-ghost" data-bs-dismiss="modal">Cancel</button>
          <button type="submit" class="btn-farm">Add</button>
        </div>
      </form>
    </div>
  </div>
</div>

<!-- Add LPG Modal -->
<div class="modal fade" id="addLpgModal" tabindex="-1">
  <div class="modal-dialog modal-dialog-centered">
    <div class="modal-content" style="background:var(--card-bg);border:1px solid var(--border);border-radius:16px;">
      <div class="modal-header" style="border-color:var(--border);">
        <h5 class="modal-title" style="font-weight:800;"><i class="fas fa-fire me-2" style="color:#a16207;"></i>Add LPG Expense</h5>
        <button type="button" class="btn-close" data-bs-dismiss="modal"></button>
      </div>
      <form method="post" action="/owner/expense/lpg/add">
        <div class="modal-body">
          <div class="row g-2 mb-3">
            <div class="col-6"><label class="form-label">Amount (₱)</label><input type="number" step="0.01" name="amount" class="form-control" required></div>
            <div class="col-6"><label class="form-label">Provider</label><input name="lpg_provider" class="form-control" placeholder="e.g. Petron Gas"></div>
          </div>
          <div class="row g-2">
            <div class="col-6"><label class="form-label">Status</label>
              <select name="status" class="form-select"><option value="Pending">Pending</option><option value="Paid">Paid</option></select>
            </div>
            <div class="col-6"><label class="form-label">Date</label><input type="date" name="expense_date" class="form-control" value="{{ today_str }}"></div>
          </div>
          <div style="font-size:11px;color:var(--muted);margin-top:8px;"><i class="fas fa-info-circle me-1"></i>Automatically assigned to the current active batch.</div>
        </div>
        <div class="modal-footer" style="border-color:var(--border);">
          <button type="button" class="btn-ghost" data-bs-dismiss="modal">Cancel</button>
          <button type="submit" class="btn-farm">Add</button>
        </div>
      </form>
    </div>
  </div>
</div>

<!-- Add Labor Expense Modal -->
<div class="modal fade" id="addLaborModal" tabindex="-1">
  <div class="modal-dialog modal-dialog-centered">
    <div class="modal-content" style="background:var(--card-bg);border:1px solid var(--border);border-radius:16px;">
      <div class="modal-header" style="border-color:var(--border);">
        <h5 class="modal-title" style="font-weight:800;"><i class="fas fa-people-carry-box me-2" style="color:#7c3aed;"></i>Add Labor Expense</h5>
        <button type="button" class="btn-close" data-bs-dismiss="modal"></button>
      </div>
      <form method="post" action="/owner/expense/labor/add">
        <div class="modal-body">
          <div class="row g-2">
            <div class="col-6"><label class="form-label">Amount (₱)</label><input type="number" step="0.01" name="amount" class="form-control" required></div>
            <div class="col-6"><label class="form-label">Status</label>
              <select name="status" class="form-select"><option value="Pending">Pending</option><option value="Paid">Paid</option></select>
            </div>
          </div>
          <div class="mb-1 mt-2"><label class="form-label">Date</label><input type="date" name="expense_date" class="form-control" value="{{ today_str }}"></div>
          <div style="font-size:11px;color:var(--muted);margin-top:8px;"><i class="fas fa-info-circle me-1"></i>Automatically assigned to the current active batch.</div>
        </div>
        <div class="modal-footer" style="border-color:var(--border);">
          <button type="button" class="btn-ghost" data-bs-dismiss="modal">Cancel</button>
          <button type="submit" class="btn-farm">Add</button>
        </div>
      </form>
    </div>
  </div>
</div>

<!-- Add Other Expense Modal (REMOVED batch selector) -->
<div class="modal fade" id="addOtherModal" tabindex="-1">
  <div class="modal-dialog modal-dialog-centered">
    <div class="modal-content" style="background:var(--card-bg);border:1px solid var(--border);border-radius:16px;">
      <div class="modal-header" style="border-color:var(--border);">
        <h5 class="modal-title" style="font-weight:800;"><i class="fas fa-sack-dollar me-2" style="color:#c2410c;"></i>Add Other Expense</h5>
        <button type="button" class="btn-close" data-bs-dismiss="modal"></button>
      </div>
      <form method="post" action="/owner/expense/other/add">
        <div class="modal-body">
          <div class="mb-3"><label class="form-label">Category</label>
            <select name="expense_category_id" class="form-select" required>
              {% for c in expense_categories %}{% if c.category_name|lower not in ['labor', 'water', 'electricity', 'lpg', 'vaccine', 'feed'] %}<option value="{{ c.expense_category_id }}">{{ c.category_name }}</option>{% endif %}{% endfor %}
            </select>
            <div style="font-size:11px;color:var(--muted);margin-top:4px;">For salaries/wages, water, electricity, LPG, vaccine, or feed, use their own cards instead.</div>
          </div>
          <div class="row g-2">
            <div class="col-6"><label class="form-label">Amount (₱)</label><input type="number" step="0.01" name="amount" class="form-control" required></div>
            <div class="col-6"><label class="form-label">Status</label>
              <select name="status" class="form-select"><option value="Pending">Pending</option><option value="Paid">Paid</option></select>
            </div>
          </div>
          <div class="mb-1 mt-2"><label class="form-label">Date</label><input type="date" name="expense_date" class="form-control" value="{{ today_str }}"></div>
          <div style="font-size:11px;color:var(--muted);margin-top:8px;"><i class="fas fa-info-circle me-1"></i>Automatically assigned to the current active batch.</div>
        </div>
        <div class="modal-footer" style="border-color:var(--border);">
          <button type="button" class="btn-ghost" data-bs-dismiss="modal">Cancel</button>
          <button type="submit" class="btn-farm">Add</button>
        </div>
      </form>
    </div>
  </div>
</div>

""" + _BASE_SCRIPT + """
<script>
function filterVitaminTable() {
  var term = document.getElementById('vitaminSearchInput').value.trim().toLowerCase();
  var rows = document.querySelectorAll('#vitaminTable tbody tr');
  rows.forEach(function(row) {
    var text = row.textContent.toLowerCase();
    row.style.display = text.indexOf(term) !== -1 ? '' : 'none';
  });
}

function filterFeedTable() {
  var term = document.getElementById('feedSearchInput').value.trim().toLowerCase();
  var rows = document.querySelectorAll('#feedTable tbody tr');
  rows.forEach(function(row) {
    var text = row.textContent.toLowerCase();
    row.style.display = text.indexOf(term) !== -1 ? '' : 'none';
  });
}

function openMgrReport() {
  var sel = document.getElementById('mgrReportBatchSelect');
  if (!sel.value) { alert('Please select a batch first.'); return; }
  var url = '/report/' + sel.value + '/print?fields=all&submit=1';
  window.open(url, '_blank');
}
</script>
</body></html>
"""

# ─────────────────────────────────────────────────────────────────────────────
# WORKER DASHBOARD — REVISED (auto flock batch)
# ─────────────────────────────────────────────────────────────────────────────
TEMPLATE_WORKER = """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Worker Dashboard — FlockIQ</title>
""" + _BASE_STYLE + """
</head>
<body>
<script>(function(){const t=localStorage.getItem("theme");if(t==="dark")document.documentElement.classList.add("dark");})()</script>
<div id="mobileOverlay" class="mobile-overlay" onclick="toggleSidebar()"></div>
<div class="mobile-topbar">
  <button onclick="toggleSidebar()" style="background:none;border:none;color:var(--text);font-size:20px;"><i class="fas fa-bars"></i></button>
  <span style="font-family:'Inter',sans-serif;font-weight:800;font-size:16px;">FlockIQ</span>
  <button class="theme-toggle" onclick="toggleDark()"><i class="fas fa-moon"></i></button>
</div>
<div class="app-shell">

<nav id="sidebar" class="sidebar">
  <div class="sidebar-brand">
    <div class="brand-icon" style="background:linear-gradient(135deg,#15803d,#166534);">""" + logo_svg(22) + """</div>
    <div><div class="brand-text">FlockIQ</div><div class="brand-sub">Worker View</div></div>
  </div>
  <div class="sidebar-nav">
    <div class="nav-section-label">Worker Panel</div>
    <a onclick="showTab('wkr-overview', this)" class="nav-link active"><i class="fas fa-gauge"></i> Overview</a>
    <a onclick="showTab('wkr-submit', this)" class="nav-link"><i class="fas fa-pen-to-square"></i> Submit Flock Record</a>
  </div>
  <div class="sidebar-footer">
    <div style="display:flex;align-items:center;gap:10px;padding:8px 12px;margin-bottom:8px;">
      <div style="width:34px;height:34px;border-radius:50%;background:linear-gradient(135deg,#15803d,#166534);display:flex;align-items:center;justify-content:center;color:#fff;font-size:13px;"><i class="fas fa-hard-hat"></i></div>
      <div><div style="font-size:13px;font-weight:700;">{{ full_name }}</div><span class="role-badge role-worker">Worker</span></div>
    </div>
    <a href="/logout" class="logout-btn"><i class="fas fa-sign-out-alt"></i> Logout</a>
  </div>
</nav>

<div class="main-content">
  <div class="topbar">
    <span class="topbar-title">Worker Dashboard</span>
    <div class="topbar-actions">
      <button class="theme-toggle" onclick="toggleDark()"><i class="fas fa-moon"></i></button>
    </div>
  </div>
  <div class="page-body">

    {% with msgs = get_flashed_messages() %}{% if msgs %}
    {% for m in msgs %}
    <div class="alert alert-success alert-dismissible fade show alert-flash mb-3" role="alert">
      <i class="fas fa-check-circle me-2"></i>{{ m }}
      <button type="button" class="btn-close" data-bs-dismiss="alert"></button>
    </div>
    {% endfor %}{% endif %}{% endwith %}

    <div id="wkr-overview" class="tab-content active">
        <div class="hero-banner">
          <div style="position:relative;z-index:1;">
            <div style="font-size:13px;font-weight:600;opacity:0.85;margin-bottom:6px;">Worker Portal</div>
            <h2 style="font-family:'Inter',sans-serif;font-weight:800;font-size:24px;margin:0 0 14px;">{{ full_name }} <i class="fas fa-hard-hat" style="font-size:16px;opacity:0.8;"></i></h2>
            <div style="display:flex;flex-wrap:wrap;gap:8px;">
              {% if active_batch %}
              <div class="metric-pill"><i class="fas fa-layer-group"></i> Active: {{ active_batch.batch_name }}</div>
              {% endif %}
              <div class="metric-pill"><i class="fas fa-clipboard-list"></i> {{ my_records|length }} Recent Submissions</div>
              <div class="metric-pill"><i class="fas fa-tasks"></i> {{ today_tasks|length }} Tasks Today</div>
            </div>
          </div>
          <div style="position:relative;z-index:1;">""" + logo_svg(90, 0.25) + """</div>
        </div>

        {% if active_batch %}
        <div class="card mb-4" style="border-left:4px solid #166534;">
          <div class="card-body-custom">
            <div style="display:flex;flex-wrap:wrap;align-items:center;justify-content:space-between;gap:16px;">
              <div>
                <div style="font-size:11px;color:var(--muted);text-transform:uppercase;letter-spacing:.04em;">Current Active Batch</div>
                <div style="font-weight:800;font-size:18px;margin-top:4px;">{{ active_batch.batch_name }}</div>
                <div style="font-size:13px;color:var(--muted);">Day {{ active_batch.age_days }} of 35 · {{ "{:,}".format(active_batch.current_bird_count) }} birds remaining</div>
              </div>
              <button class="btn-farm" onclick="showTab('wkr-submit', document.querySelector('[onclick*=wkr-submit]'))"><i class="fas fa-pen-to-square me-1"></i> Submit Record</button>
            </div>
          </div>
        </div>
        {% endif %}

        <div class="card mb-4">
          <div class="card-header-custom">
            <div class="section-header" style="margin:0;">
              <div class="section-divider"></div>
              <h5><i class="fas fa-tasks me-2" style="color:var(--accent);"></i>Today's Tasks</h5>
            </div>
          </div>
          <div class="card-body-custom">
            {% if today_tasks %}
            <div class="schedule-list">
              {% for task in today_tasks %}
              <div class="schedule-item">
                <div class="si-icon"><i class="fas {{ task.icon }}"></i></div>
                <div class="si-body">
                  <div class="si-title">{{ task.title }} <span style="color:var(--muted);font-weight:500;">— {{ task.type }}</span></div>
                  <div class="si-sub">Batch: {{ task.batch }}</div>
                </div>
                <div class="si-date">{{ task.date.strftime('%I:%M %p') if task.date else '—' }}</div>
              </div>
              {% endfor %}
            </div>
            {% else %}
            <div class="text-center py-4" style="color:var(--muted);"><i class="fas fa-check-circle fa-2x mb-2 d-block" style="color:#166534;"></i>No tasks scheduled for today. Great job!</div>
            {% endif %}
          </div>
        </div>

        <div class="card">
          <div class="card-header-custom">
            <div class="section-header" style="margin:0;">
              <div class="section-divider"></div>
              <h5><i class="fas fa-clock-rotate-left me-2" style="color:var(--accent);"></i>My Recent Submissions</h5>
            </div>
          </div>
          <div class="card-body-custom">
            <div class="table-responsive">
              <table class="table table-hover align-middle">
                <thead><tr><th>Batch</th><th>Date</th><th>Weight</th><th>Mortality</th><th>Status</th></tr></thead>
                <tbody>
                {% for r in my_records %}
                <tr>
                  <td style="font-weight:700;">{{ r.batch.batch_name if r.batch else '—' }}</td>
                  <td style="font-size:13px;color:var(--muted);">{{ r.record_date.strftime('%b %d, %Y') if r.record_date else '—' }}</td>
                  <td>{{ r.avg_weight_g }} g</td>
                  <td>{{ r.mortality }}</td>
                  <td>
                    {% if r.status == 'Verified' %}
                    <span class="status-pill status-paid"><i class="fas fa-check me-1"></i>Verified</span>
                    {% elif r.status == 'Rejected' %}
                    <span class="status-pill" style="background:#fee2e2;color:#991b1b;" title="{{ r.review_notes or '' }}"><i class="fas fa-xmark me-1"></i>Rejected</span>
                    {% else %}
                    <span class="status-pill status-pending"><i class="fas fa-hourglass-half me-1"></i>Pending</span>
                    {% endif %}
                    {% if r.status == 'Rejected' and r.review_notes %}
                    <div style="font-size:11px;color:#991b1b;margin-top:3px;">{{ r.review_notes }}</div>
                    {% endif %}
                  </td>
                </tr>
                {% else %}
                <tr><td colspan="5" class="text-center py-4" style="color:var(--muted);">No submissions yet.</td></tr>
                {% endfor %}
                </tbody>
              </table>
            </div>
          </div>
        </div>
    </div>

    <div id="wkr-submit" class="tab-content">
      <div class="card">
        <div class="card-header-custom">
          <div class="section-header" style="margin:0;">
            <div class="section-divider"></div>
            <h5><i class="fas fa-pen-to-square me-2" style="color:var(--accent);"></i>Submit Flock Record</h5>
          </div>
        </div>
        <div class="card-body-custom">
          {% if active_batch %}
          <div class="alert" style="background:#f0fdf4;color:#166534;border:1px solid #bbf7d0;font-size:13px;border-radius:10px;padding:10px 14px;margin-bottom:16px;">
            <i class="fas fa-info-circle me-1"></i>Recording for <strong>{{ active_batch.batch_name }}</strong> — automatically selected as the current active batch.
          </div>
          <form id="workerRecordForm" method="post" action="/worker/record/add" onsubmit="return confirmRecordSubmit(event)">
            <input type="hidden" name="batch_id" value="{{ active_batch.batch_id }}">
            <div class="row g-3">

              <div class="col-md-6">
                <label class="form-label">Flock Batch</label>
                <input type="text" class="form-control" value="{{ active_batch.batch_name }}" disabled>
              </div>

              <div class="col-md-6">
                <label class="form-label">Date <span class="text-danger">*</span></label>
                <input type="date" name="record_date" id="wkrDate" class="form-control" value="{{ today_date }}" required onchange="updateDayNumber()">
              </div>

              <div class="col-md-4">
                <label class="form-label">Day Number (out of 35)</label>
                <input type="number" id="dayNumber" class="form-control" value="{{ active_batch.age_days }}" disabled>
                <small class="text-muted">Days since start / 35-day grace period</small>
              </div>

              <div class="col-md-4">
                <label class="form-label">Mortality <span class="text-danger">*</span></label>
                <input type="number" name="mortality" id="wkrMortality" class="form-control" placeholder="0" value="0" min="0" required>
              </div>

              <div class="col-md-4">
                <label class="form-label">Culled</label>
                <input type="number" name="cull" id="wkrCull" class="form-control" placeholder="0" value="0" min="0">
              </div>

              <div class="col-md-6">
                <label class="form-label">Feed Type <span class="text-danger">*</span></label>
                <select name="feed_record_id" id="wkrFeedType" class="form-select" required>
                  <option value="">— Select Feed Type —</option>
                  {% for fr in feed_records %}
                  <option value="{{ fr.feed_record_id }}">{{ fr.feed_category }} — {{ fr.feed_name }} (₱{{ "%.2f"|format(fr.cost_per_kg) }}/kg)</option>
                  {% endfor %}
                </select>
              </div>

              <div class="col-md-6">
                <label class="form-label">Daily Feed Given (kg) <span class="text-danger">*</span></label>
                <input type="number" step="0.1" name="feed_consumed" id="wkrFeedConsumed" class="form-control" placeholder="Daily feed given" required>
                <small class="text-muted">Log the exact amount of feed given today — accumulates for FCR calculation and feed expenses</small>
              </div>

              <div class="col-md-6">
                <label class="form-label">Average Bird Weight (grams) <span class="text-danger">*</span></label>
                <input type="number" step="0.1" name="avg_weight" id="wkrWeight" class="form-control" placeholder="e.g. 850" required>
              </div>

              <div class="col-md-6">
                <label class="form-label">Cause of Death / Cull</label>
                <input name="cause" id="wkrCause" class="form-control" placeholder="e.g. Heat stress, disease, injury">
              </div>

              <div class="col-md-4">
                <label class="form-label">Water Consumption</label>
                <input name="water_consumption" id="wkrWater" class="form-control" placeholder="e.g. 850 L">
              </div>

              <div class="col-md-4">
                <label class="form-label">Abnormal Behavior</label>
                <input name="abnormal_behavior" id="wkrBehavior" class="form-control" placeholder="e.g. lethargy, huddling">
              </div>

              <div class="col-md-4">
                <label class="form-label">Visible Illness</label>
                <input name="visible_illness" id="wkrIllness" class="form-control" placeholder="e.g. respiratory signs">
              </div>

              <div class="col-12">
                <label class="form-label">Remarks</label>
                <textarea name="remarks" id="wkrRemarks" class="form-control" rows="2" placeholder="Any other observations for the Manager"></textarea>
              </div>

            </div>
            <button type="submit" class="btn-farm mt-4" style="padding:11px 26px;"><i class="fas fa-paper-plane me-2"></i>Submit Daily Record</button>
          </form>
          {% else %}
          <div class="text-center py-5" style="color:var(--muted);">
            <i class="fas fa-layer-group fa-2x mb-3 d-block"></i>
            No active flock batch. Ask your Owner to create one.
          </div>
          {% endif %}
        </div>
      </div>
    </div>

  </div></div></div>

<div class="modal fade" id="submitConfirmModal" tabindex="-1" data-bs-backdrop="static">
  <div class="modal-dialog modal-dialog-centered">
    <div class="modal-content" style="background:var(--card-bg);border:1px solid var(--border);border-radius:16px;">
      <div class="modal-header" style="border-color:var(--border);">
        <h5 class="modal-title" style="font-weight:800;"><i class="fas fa-clipboard-check me-2" style="color:var(--accent);"></i>Confirm Daily Record</h5>
        <button type="button" class="btn-close" data-bs-dismiss="modal"></button>
      </div>
      <div class="modal-body">
        <p style="font-size:13px;color:var(--muted);margin-bottom:14px;">
          Please double-check the details below before submitting.
        </p>
        <div style="background:var(--bg);border-radius:10px;padding:14px;border:1px solid var(--border);" id="confirmDetails"></div>
      </div>
      <div class="modal-footer" style="border-color:var(--border);">
        <button type="button" class="btn-ghost" data-bs-dismiss="modal">Go Back & Edit</button>
        <button type="button" class="btn-farm" onclick="reallySubmit()"><i class="fas fa-paper-plane me-1"></i> Confirm Submit</button>
      </div>
    </div>
  </div>
</div>

""" + _BASE_SCRIPT + """
<script>
var batchStart = "{{ active_batch.start_date.strftime('%Y-%m-%d') if active_batch else '' }}";

function updateDayNumber() {
  if (!batchStart) return;
  var d = document.getElementById('wkrDate').value;
  if (!d) return;
  var start = new Date(batchStart);
  var sel = new Date(d);
  var diff = Math.ceil((sel - start) / (1000 * 60 * 60 * 24));
  document.getElementById('dayNumber').value = diff > 0 ? diff : 0;
}

function confirmRecordSubmit(event) {
  event.preventDefault();
  const feedSelect = document.getElementById('wkrFeedType');
  const batchName = "{{ active_batch.batch_name if active_batch else '' }}";
  const feedText = feedSelect.selectedIndex > 0 ? feedSelect.options[feedSelect.selectedIndex].text.trim() : '(no feed selected)';
  const recordDate = document.getElementById('wkrDate').value || '(no date)';
  const mortality = document.getElementById('wkrMortality').value || '0';
  const cull = document.getElementById('wkrCull').value || '0';
  const feedConsumed = document.getElementById('wkrFeedConsumed').value || '0';
  const avgWeight = document.getElementById('wkrWeight').value || '0';
  const cause = document.getElementById('wkrCause').value.trim();
  const water = document.getElementById('wkrWater').value.trim();
  const behavior = document.getElementById('wkrBehavior').value.trim();
  const illness = document.getElementById('wkrIllness').value.trim();
  const remarks = document.getElementById('wkrRemarks').value.trim();
  const dayNum = document.getElementById('dayNumber').value || '0';

  let html = '';
  html += '<div class="confirm-row"><span class="label">Batch</span><span class="value">' + batchName + '</span></div>';
  html += '<div class="confirm-row"><span class="label">Date</span><span class="value">' + recordDate + '</span></div>';
  html += '<div class="confirm-row"><span class="label">Day Number</span><span class="value">Day ' + dayNum + ' of 35</span></div>';
  html += '<div class="confirm-row"><span class="label">Mortality</span><span class="value">' + mortality + '</span></div>';
  html += '<div class="confirm-row"><span class="label">Culled</span><span class="value">' + cull + '</span></div>';
  html += '<div class="confirm-row"><span class="label">Feed Type</span><span class="value">' + feedText + '</span></div>';
  html += '<div class="confirm-row"><span class="label">Feed Given</span><span class="value">' + feedConsumed + ' kg</span></div>';
  html += '<div class="confirm-row"><span class="label">Avg Bird Weight</span><span class="value">' + avgWeight + ' g</span></div>';
  if (cause) html += '<div class="confirm-row"><span class="label">Cause</span><span class="value">' + cause + '</span></div>';
  if (water) html += '<div class="confirm-row"><span class="label">Water</span><span class="value">' + water + '</span></div>';
  if (behavior) html += '<div class="confirm-row"><span class="label">Abnormal Behavior</span><span class="value">' + behavior + '</span></div>';
  if (illness) html += '<div class="confirm-row"><span class="label">Visible Illness</span><span class="value">' + illness + '</span></div>';
  if (remarks) html += '<div class="confirm-row"><span class="label">Remarks</span><span class="value">' + remarks + '</span></div>';

  document.getElementById('confirmDetails').innerHTML = html;
  var modal = new bootstrap.Modal(document.getElementById('submitConfirmModal'));
  modal.show();
  return false;
}

function reallySubmit() {
  document.getElementById('workerRecordForm').submit();
}
</script>
</body></html>
"""

# ─────────────────────────────────────────────────────────────────────────────
# Printable Performance Report (unchanged)
# ─────────────────────────────────────────────────────────────────────────────
TEMPLATE_PERFORMANCE_REPORT_PRINT = """<!doctype html>
<html><head><meta charset="utf-8"><title>Performance Report</title>
<script src="https://cdn.jsdelivr.net/npm/html2pdf.js@0.10.1/dist/html2pdf.bundle.min.js"></script>
<style>
  body{font-family:Arial,Helvetica,sans-serif;font-size:13px;color:#111;margin:30px;}
  h1{font-size:20px;margin:0;letter-spacing:1px;}
  .sub{font-size:12px;color:#555;margin-bottom:4px;}
  .title{font-size:14px;font-weight:700;letter-spacing:2px;text-align:center;margin:18px 0 10px;}
  table{width:100%;border-collapse:collapse;margin-top:6px;}
  th,td{border:1px solid #333;padding:5px 8px;text-align:left;}
  th{background:#f0f0f0;}
  .no-print{margin-bottom:16px;display:flex;gap:10px;}
  .no-print button{padding:8px 16px;font-weight:700;cursor:pointer;border:1px solid #333;border-radius:4px;background:#fff;}
  .no-print button:hover{background:#f0f0f0;}
  .sig{margin-top:60px;font-size:13px;}
  .sig-line{display:inline-block;min-width:260px;border-bottom:1px solid #111;margin-left:8px;}
  @media print{ .no-print{display:none;} body{margin:0.5in;} }
</style></head>
<body>
  <div class="no-print">
    <button onclick="window.print()">Print</button>
    <button onclick="saveReportPdf()">Save PDF</button>
  </div>

  <div id="reportContent">
  <h1>AGRADECIDO CORP.</h1>
  <div class="sub">Unit 204 A7 Bldg Floro Subd., Zigzag Hills, Malhacan, Meycauayan City Bulacan</div>
  <div class="title">PERFORMANCE REPORT</div>

  <table>
    <tr><th>Field</th><th>Value</th></tr>
    {% if 'batch_name' in selected_fields %}<tr><td>Batch Name</td><td>{{ report.batch.batch_name if report.batch else '—' }}</td></tr>{% endif %}
    {% if 'age' in selected_fields %}<tr><td>Age</td><td>{{ report.age or '—' }} days</td></tr>{% endif %}
    {% if 'initial_count' in selected_fields %}<tr><td>Initial Head Count</td><td>{{ report.initial_count or '—' }}</td></tr>{% endif %}
    {% if 'harvest_count' in selected_fields %}<tr><td>Harvest Count</td><td>{{ report.harvest_count or '—' }}</td></tr>{% endif %}
    {% if 'mortality_pct' in selected_fields %}<tr><td>Mortality Rate</td><td>{{ report.mortality_pct or '—' }}%</td></tr>{% endif %}
    {% if 'start_date' in selected_fields %}<tr><td>Start Date</td><td>{{ report.batch.start_date.strftime('%d-%m-%Y') if report.batch and report.batch.start_date else '—' }}</td></tr>{% endif %}
    {% if 'harvest_date' in selected_fields %}<tr><td>Harvest Date</td><td>{{ report.end_date or '—' }}</td></tr>{% endif %}
    {% if 'adg' in selected_fields %}<tr><td>ADG (Average Daily Gain)</td><td>{{ report.adg or '—' }} g/day</td></tr>{% endif %}
    {% if 'fcr' in selected_fields %}<tr><td>FCR (Feed Conversion Ratio)</td><td>{{ report.fcr or '—' }}</td></tr>{% endif %}
    {% if 'lw' in selected_fields %}<tr><td>Live Weight (LW)</td><td>{{ report.lw or '—' }} g</td></tr>{% endif %}
    {% if 'expenses' in selected_fields %}<tr><td>Expenses</td><td>₱{{ "{:,.2f}".format(report.expenses) if report.expenses else '—' }}</td></tr>{% endif %}
    {% if 'season' in selected_fields %}<tr><td>Season</td><td>{{ report.season or '—' }}</td></tr>{% endif %}
    {% if 'chick_booster' in selected_fields %}<tr><td>Chick Booster</td><td>{{ report.chick_booster or '—' }}</td></tr>{% endif %}
    {% if 'grower_pellets' in selected_fields %}<tr><td>Grower Pellets</td><td>{{ report.grower_pellets or '—' }}</td></tr>{% endif %}
    {% if 'finisher_pellets' in selected_fields %}<tr><td>Finisher Pellets</td><td>{{ report.finisher_pellets or '—' }}</td></tr>{% endif %}
    {% if 'vaccine_day_12' in selected_fields %}<tr><td>Vaccine Day 12</td><td>{{ report.vaccine_day_12 or '—' }}</td></tr>{% endif %}
    {% if 'vaccine_day_16' in selected_fields %}<tr><td>Vaccine Day 16</td><td>{{ report.vaccine_day_16 or '—' }}</td></tr>{% endif %}
    {% if 'medicines' in selected_fields %}<tr><td>Medicines</td><td>{{ report.medicines or '—' }}</td></tr>{% endif %}
    {% if 'loss_gain' in selected_fields %}<tr><td>Loss/Gain</td><td style="color:{{ '#15803d' if report.loss_gain and report.loss_gain >= 0 else '#dc2626' }};font-weight:700;">{{ '+' if report.loss_gain and report.loss_gain >= 0 else '' }}₱{{ "{:,.2f}".format(report.loss_gain) if report.loss_gain is not none else '—' }}</td></tr>{% endif %}
    {% if 'remarks' in selected_fields %}<tr><td>Remarks</td><td>{{ report.remarks or '—' }}</td></tr>{% endif %}
  </table>

  <div style="margin-top:16px;font-size:11px;color:#666;">
    <em>Loss/Gain is based on the performance of the chicken and the total expenses.</em>
  </div>

  <div class="sig">Name of Farm Head: <span class="sig-line">{{ report.farm_head_name or '' }}</span></div>
  </div>

  <script>
  function saveReportPdf() {
    var batchName = "{{ (report.batch.batch_name if report.batch else 'report') | replace(' ', '_') }}";
    var opt = {
      margin: 0.5,
      filename: 'Performance_Report_' + batchName + '.pdf',
      image: { type: 'jpeg', quality: 0.98 },
      html2canvas: { scale: 2 },
      jsPDF: { unit: 'in', format: 'letter', orientation: 'portrait' }
    };
    html2pdf().set(opt).from(document.getElementById('reportContent')).save();
  }
  </script>
</body></html>
"""