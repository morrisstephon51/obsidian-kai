#!/usr/bin/env python3
"""Bundle the whole static site into one self-contained preview.html.

The preview renders each real page inside an iframe (full fidelity), with a
slim review bar for navigation. Internal links work; forms are disabled with
a notice (they are live only on the deployed site); images/CSS/JS are
inlined so the file needs no server.

    python3 _build/preview.py  ->  ../_preview/preview.html
"""
import base64, json, pathlib, re

ROOT = pathlib.Path(__file__).resolve().parent.parent
OUT = ROOT / "_preview" / "preview.html"

css = (ROOT / "assets/css/site.css").read_text(encoding="utf-8")
js = (ROOT / "assets/js/site.js").read_text(encoding="utf-8")

def data_uri(path, mime):
    return f"data:{mime};base64," + base64.b64encode((ROOT / path).read_bytes()).decode()

ASSETS = {
    "/assets/img/logo.png": data_uri("assets/img/logo.png", "image/png"),
    "/assets/img/favicon.png": data_uri("assets/img/favicon.png", "image/png"),
    "/assets/img/hero-team.jpg": data_uri("assets/img/hero-team.jpg", "image/jpeg"),
}

INJECT = """<script>
(function(){
  document.addEventListener('click', function(e){
    var a = e.target.closest('a'); if(!a) return;
    var href = a.getAttribute('href')||'';
    if(href.startsWith('/')){ e.preventDefault(); parent.postMessage({nav:href}, '*'); }
    else if(href.startsWith('http')){ a.target='_blank'; a.rel='noopener'; }
  });
  document.addEventListener('submit', function(e){
    e.preventDefault();
    var n=document.createElement('p');
    n.textContent='Preview mode: forms are disabled here. On the live site this delivers to info@eccstaffing.com.';
    n.style.cssText='background:#F6ECDB;border:1px solid #D9A75B;border-radius:8px;padding:12px 16px;font-weight:600;color:#1F2A44;margin-top:8px';
    if(!e.target.querySelector('.pv-note')){ n.className='pv-note'; e.target.appendChild(n); }
  });
  window.addEventListener('message', function(ev){
    if(ev.data && ev.data.vertical){
      var s=document.querySelector('select[name="vertical"]');
      if(s) s.value=ev.data.vertical;
    }
  });
})();
</script>"""

pages = {}
for f in sorted(ROOT.rglob("*.html")):
    if "_build" in f.parts or "_preview" in f.parts:
        continue
    rel = "/" + str(f.relative_to(ROOT)).replace("\\", "/")
    route = rel[:-len("index.html")] if rel.endswith("/index.html") else rel
    t = f.read_text(encoding="utf-8")
    t = t.replace('<link rel="stylesheet" href="/assets/css/site.css">', "<style>" + css + "</style>")
    t = t.replace('<script src="/assets/js/site.js"></script>', "<script>" + js + "</script>")
    t = re.sub(r'<link rel="icon"[^>]*>', "", t)
    for path, uri in ASSETS.items():
        t = t.replace(f'src="{path}"', f'src="{uri}"')
    t = t.replace("</body>", INJECT + "</body>")
    m = re.search(r"<title>(.*?)</title>", t)
    pages[route] = {"title": m.group(1) if m else "Elite Career Compass", "html": t}

routes_json = json.dumps(pages).replace("</", "<\\/")

shellpage = """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>ECC Staffing Site Preview</title>
<style>
:root{--navy:#1B2437;--ink:#0B1020;--gold:#D9A75B;--line:#3a4356}
html,body{margin:0;height:100%}
body{display:flex;flex-direction:column;font-family:system-ui,sans-serif;background:var(--ink)}
.bar{display:flex;align-items:center;gap:12px;background:var(--navy);color:#fff;padding:8px 14px;font-size:13.5px;flex-wrap:wrap}
.bar .t{font-weight:700}
.bar .badge{background:var(--gold);color:#1B2437;font-weight:800;font-size:11px;letter-spacing:.08em;text-transform:uppercase;padding:3px 9px;border-radius:99px}
.bar select{margin-left:auto;font:inherit;padding:5px 8px;border-radius:6px;border:1px solid var(--line);background:#0B1020;color:#fff;max-width:46vw}
iframe{flex:1;border:0;width:100%;background:#fff}
</style>
</head>
<body>
<div class="bar">
  <span class="badge">Preview</span>
  <span class="t">Elite Career Compass — eccstaffing.com</span>
  <span id="path"></span>
  <select id="jump" aria-label="Go to page"></select>
</div>
<iframe id="frame" title="Site preview"></iframe>
<script type="application/json" id="routes">__ROUTES__</script>
<script>
var PAGES = JSON.parse(document.getElementById('routes').textContent);
var frame = document.getElementById('frame');
var jump = document.getElementById('jump');
var ORDER = ["/","/clients/","/clients/contract-staffing/","/clients/contract-to-hire/","/clients/direct-placement/",
 "/industries/healthcare/","/industries/administrative/","/industries/light-industrial/","/industries/finance-accounting/","/industries/technology/",
 "/request-talent/","/applicants/","/applicants/how-it-works/","/applicants/open-roles/","/apply/",
 "/about/","/about/results/","/insights/","/insights/contract-to-hire-vs-direct-placement/","/insights/how-to-work-with-a-recruiter/",
 "/contact/","/admin/","/privacy/","/terms/","/accessibility/","/404.html"];
ORDER.forEach(function(r){ if(PAGES[r]){ var o=document.createElement('option'); o.value=r; o.textContent=r==="/"?"/ (Home)":r; jump.appendChild(o);} });
Object.keys(PAGES).forEach(function(r){ if(ORDER.indexOf(r)<0){ var o=document.createElement('option'); o.value=r; o.textContent=r; jump.appendChild(o);} });
function go(route){
  var q = route.split('?')[1]||''; var path = route.split('?')[0];
  if(!PAGES[path]) path = "/404.html";
  frame.srcdoc = PAGES[path].html;
  document.title = PAGES[path].title + " — Preview";
  document.getElementById('path').textContent = path;
  jump.value = PAGES[path] ? path : "/404.html";
  try{ history.replaceState(null,'','#'+route); }catch(e){}
  if(q.indexOf('vertical=')>-1){
    var v = q.split('vertical=')[1].split('&')[0];
    frame.addEventListener('load', function once(){ frame.removeEventListener('load', once);
      frame.contentWindow.postMessage({vertical:v}, '*'); });
  }
}
window.addEventListener('message', function(e){ if(e.data && e.data.nav) go(e.data.nav); });
jump.addEventListener('change', function(){ go(jump.value); });
go((location.hash||'#/').slice(1) || '/');
</script>
</body>
</html>"""

OUT.parent.mkdir(exist_ok=True)
OUT.write_text(shellpage.replace("__ROUTES__", routes_json), encoding="utf-8")
print(f"Wrote {OUT} ({OUT.stat().st_size//1024} KB), {len(pages)} routes")
