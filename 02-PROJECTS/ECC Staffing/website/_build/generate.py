#!/usr/bin/env python3
"""Generate the Elite Career Compass static site.

Every page is emitted from one shared shell so branding, navigation, and the
email address stay consistent. Edit page copy in PAGES below (or edit the
emitted HTML directly for one-off tweaks) and re-run:

    python3 _build/generate.py
"""
import os, html, pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
SITE = "https://eccstaffing.com"
EMAIL = "info@eccstaffing.com"
PHONE = "(737) 423-3422"
PHONE_TEL = "+17374233422"
FONT = ('<link rel="preconnect" href="https://fonts.googleapis.com">'
        '<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>'
        '<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Hanken+Grotesk:wght@400;500;600;700;800&display=swap">')

# ---------------------------------------------------------------- components

ICON_COMPASS = '<svg class="icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" aria-hidden="true"><circle cx="12" cy="12" r="10"/><polygon points="16.24 7.76 14.12 14.12 7.76 16.24 9.88 9.88 16.24 7.76"/></svg>'
ICON_SHIELD = '<svg class="icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" aria-hidden="true"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/><path d="M9 12l2 2 4-4"/></svg>'
ICON_HANDS = '<svg class="icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" aria-hidden="true"><path d="M20.8 4.6a5.5 5.5 0 0 0-7.8 0L12 5.6l-1-1a5.5 5.5 0 0 0-7.8 7.8l1 1L12 21.2l7.8-7.8 1-1a5.5 5.5 0 0 0 0-7.8z"/></svg>'

def eyebrow(txt):
    return f'<p class="eyebrow">{txt}</p>'

def stats_bar():
    return '''<div class="grid c4">
      <div class="stat"><span class="v">48 hrs</span><span class="l">Average time to first qualified slate</span></div>
      <div class="stat"><span class="v">92%</span><span class="l">Placement retention past one year</span></div>
      <div class="stat"><span class="v">5</span><span class="l">Core industries served</span></div>
      <div class="stat"><span class="v">1:1</span><span class="l">Dedicated recruiter per search</span></div>
    </div>'''

def pillars():
    return f'''<div class="grid c3">
      <div class="card">{ICON_COMPASS}<h3>Direction</h3><p>Search strategy shaped around your roadmap, not a generic req list.</p></div>
      <div class="card">{ICON_SHIELD}<h3>Knowledge</h3><p>Market data, compensation benchmarks, and screening rigor on every search.</p></div>
      <div class="card">{ICON_HANDS}<h3>Guidance</h3><p>Real humans staying with candidates and clients well past day one.</p></div>
    </div>'''

def form(kind):
    """kind: talent | apply | contact. All deliver to info@eccstaffing.com."""
    common = (f'<input type="hidden" name="_next" value="{SITE}/thanks/{kind}/">'
              '<input type="hidden" name="_template" value="table">'
              '<input type="text" name="_honey" style="display:none" tabindex="-1" autocomplete="off" aria-hidden="true">')
    if kind == "talent":
        return f'''<form class="lead-form" action="https://formsubmit.co/{EMAIL}" method="POST">
      <input type="hidden" name="_subject" value="[Talent Request] New request from eccstaffing.com">{common}
      <div class="row">
        <div><label for="t-company">Company</label><input id="t-company" name="company" required autocomplete="organization"></div>
        <div><label for="t-name">Your name</label><input id="t-name" name="name" required autocomplete="name"></div>
      </div>
      <div class="row">
        <div><label for="t-phone">Phone</label><input id="t-phone" name="phone" type="tel" required autocomplete="tel"></div>
        <div><label for="t-email">Email</label><input id="t-email" name="email" type="email" required autocomplete="email"></div>
      </div>
      <div><label for="t-need">Who do you need, and when?</label>
      <textarea id="t-need" name="need" rows="4" required placeholder="e.g. Two credentialed medical assistants, contract-to-hire, starting within two weeks."></textarea></div>
      <button class="btn gold" type="submit">Request Talent</button>
      <p class="fine">Prefer to talk? Call <a href="tel:{PHONE_TEL}">{PHONE}</a> or email <a href="mailto:{EMAIL}">{EMAIL}</a>.</p>
    </form>'''
    if kind == "apply":
        return f'''<form class="lead-form" action="https://formsubmit.co/{EMAIL}" method="POST" enctype="multipart/form-data">
      <input type="hidden" name="_subject" value="[Application] New applicant from eccstaffing.com">{common}
      <div class="row">
        <div><label for="a-name">Your name</label><input id="a-name" name="name" required autocomplete="name"></div>
        <div><label for="a-phone">Phone</label><input id="a-phone" name="phone" type="tel" required autocomplete="tel"></div>
      </div>
      <div class="row">
        <div><label for="a-email">Email</label><input id="a-email" name="email" type="email" required autocomplete="email"></div>
        <div><label for="a-vertical">Field of work</label>
          <select id="a-vertical" name="vertical">
            <option value="">Choose one (optional)</option>
            <option value="healthcare">Healthcare</option>
            <option value="administrative">Administrative</option>
            <option value="light-industrial">Light Industrial</option>
            <option value="finance-accounting">Finance &amp; Accounting</option>
            <option value="technology">Technology</option>
          </select></div>
      </div>
      <div><label for="a-resume">Resume (optional, and no resume yet is fine)</label>
      <input id="a-resume" name="attachment" type="file" accept=".pdf,.doc,.docx,.txt,.rtf"></div>
      <button class="btn gold" type="submit">Apply Now</button>
      <p class="fine">Our service is always free to candidates. Employers pay us, never you.</p>
    </form>'''
    return f'''<form class="lead-form" action="https://formsubmit.co/{EMAIL}" method="POST">
      <input type="hidden" name="_subject" value="[Contact] New message from eccstaffing.com">{common}
      <div class="row">
        <div><label for="c-name">Your name</label><input id="c-name" name="name" required autocomplete="name"></div>
        <div><label for="c-email">Email</label><input id="c-email" name="email" type="email" required autocomplete="email"></div>
      </div>
      <div><label for="c-msg">How can we help?</label><textarea id="c-msg" name="message" rows="5" required></textarea></div>
      <button class="btn gold" type="submit">Send Message</button>
    </form>'''

TRUE_NORTH = f'''<section class="true-north"><div class="wrap">
  <div><h2>Let&rsquo;s find your true north</h2>
  <p>Hiring soon, or looking for your next role? Start the conversation today.</p></div>
  <a class="btn gold" href="/contact/">Contact ECC</a>
</div></section>'''

def jsonld():
    return ('<script type="application/ld+json">{'
            '"@context":"https://schema.org","@type":"EmploymentAgency",'
            '"name":"Elite Career Compass LLC","url":"' + SITE + '",'
            '"email":"' + EMAIL + '","telephone":"' + PHONE_TEL + '",'
            '"slogan":"Guiding Talent. Empowering Employers.",'
            '"areaServed":"US","logo":"' + SITE + '/assets/img/logo.png"}'
            '</script>')

NAV_CLIENT_MENU = '''<div class="menu">
      <a href="/clients/">Clients Overview</a>
      <p class="mh">Services</p>
      <a href="/clients/contract-staffing/">Contract Staffing</a>
      <a href="/clients/contract-to-hire/">Contract-to-Hire</a>
      <a href="/clients/direct-placement/">Direct Placement</a>
      <p class="mh">Industries</p>
      <a href="/industries/healthcare/">Healthcare</a>
      <a href="/industries/administrative/">Administrative</a>
      <a href="/industries/light-industrial/">Light Industrial</a>
      <a href="/industries/finance-accounting/">Finance &amp; Accounting</a>
      <a href="/industries/technology/">Technology</a>
    </div>'''
NAV_APPLICANT_MENU = '''<div class="menu">
      <a href="/applicants/">Applicants Overview</a>
      <a href="/applicants/how-it-works/">How It Works</a>
      <a href="/applicants/open-roles/">Open Roles</a>
      <a href="/apply/">Apply Now</a>
    </div>'''

def shell(path, title, desc, body, *, band=True, current="", head_extra=""):
    cur = lambda k: ' aria-current="true"' if k == current else ""
    page = f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(title)}</title>
<meta name="description" content="{html.escape(desc)}">
<link rel="canonical" href="{SITE}{path}">
<link rel="icon" type="image/png" href="/assets/img/favicon.png">
{FONT}
<link rel="stylesheet" href="/assets/css/site.css">
{head_extra}
</head>
<body>
<a class="skip-link" href="#main">Skip to content</a>
<div class="utility"><div class="wrap">
  <a href="tel:{PHONE_TEL}">{PHONE}</a>
  <a href="mailto:{EMAIL}">{EMAIL}</a>
</div></div>
<header class="site"><div class="wrap">
  <a class="brand" href="/">
    <img src="/assets/img/logo.png" alt="Elite Career Compass logo: a compass rose and quill over an open book" width="46" height="57">
    <span class="bn">Elite Career Compass<span class="bt">Staffing &amp; Recruiting</span></span>
  </a>
  <button class="nav-toggle" aria-expanded="false" aria-controls="primary-nav">Menu</button>
  <nav class="primary" id="primary-nav" aria-label="Primary">
    <div><a class="top" href="/clients/"{cur("clients")}>For Clients</a>{NAV_CLIENT_MENU}</div>
    <div><a class="top" href="/applicants/"{cur("applicants")}>For Applicants</a>{NAV_APPLICANT_MENU}</div>
    <div><a class="top" href="/insights/"{cur("insights")}>Insights</a></div>
    <div><a class="top" href="/about/"{cur("about")}>About ECC</a></div>
  </nav>
  <div class="hdr-ctas">
    <a class="btn dark" href="/request-talent/">Request Talent</a>
    <a class="btn outline" href="/applicants/open-roles/">Find Your Next Role</a>
  </div>
</div></header>
<main id="main">
{body}
</main>
{TRUE_NORTH if band else ""}
<footer class="site"><div class="wrap">
  <div class="cols">
    <div>
      <div class="fbrand"><img src="/assets/img/logo.png" alt="" width="44" height="55"><span>Elite Career Compass&nbsp;LLC</span></div>
      <p>Guiding talent. Empowering employers. A people-first staffing and recruiting partner built on direction, knowledge, and trust.</p>
    </div>
    <div><h4>For Clients</h4><ul>
      <li><a href="/clients/contract-staffing/">Contract Staffing</a></li>
      <li><a href="/clients/contract-to-hire/">Contract-to-Hire</a></li>
      <li><a href="/clients/direct-placement/">Direct Placement</a></li>
      <li><a href="/request-talent/">Request Talent</a></li>
    </ul></div>
    <div><h4>For Applicants</h4><ul>
      <li><a href="/applicants/how-it-works/">How It Works</a></li>
      <li><a href="/applicants/open-roles/">Open Roles</a></li>
      <li><a href="/apply/">Apply Now</a></li>
      <li><a href="/insights/">Insights</a></li>
    </ul></div>
    <div><h4>Contact</h4>
      <div class="contact-line"><a href="mailto:{EMAIL}">{EMAIL}</a></div>
      <div class="contact-line"><a href="tel:{PHONE_TEL}">{PHONE}</a></div>
      <div class="contact-line"><span>Serving clients nationwide</span></div>
    </div>
  </div>
  <div class="legal">
    <span>&copy; 2026 Elite Career Compass LLC. All rights reserved.</span>
    <ul><li><a href="/privacy/">Privacy</a></li><li><a href="/terms/">Terms</a></li><li><a href="/accessibility/">Accessibility</a></li></ul>
  </div>
</div></footer>
<script src="/assets/js/site.js"></script>
</body>
</html>'''
    out = ROOT / path.lstrip("/")
    if path.endswith("/"):
        out = out / "index.html"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(page, encoding="utf-8")
    return path

# ------------------------------------------------------------------- content

written = []

# ---- Home
written.append(shell("/", "Elite Career Compass | Staffing & Recruiting",
  "People-first staffing and recruiting across healthcare, administrative, light industrial, finance, and technology. A qualified slate in 48 hours, 92% placement retention.",
  f'''
<section class="hero"><div class="wrap">
  <div>
    {eyebrow("Elite Career Compass LLC")}
    <h1>Guiding Talent. Empowering Employers.</h1>
    <p class="lead">We place people with purpose &mdash; pairing employers with vetted professionals and giving candidates a clear bearing on their next move.</p>
    <div class="ctas">
      <a class="btn light" href="/clients/">For Clients</a>
      <a class="btn ghost-dark" href="/applicants/">For Applicants</a>
    </div>
  </div>
  <img class="photo" src="/assets/img/hero-team.jpg" alt="The kind of teams we help build: professionals gathered in a bright office lobby" width="1100" height="756">
</div></section>

<section class="band alt"><div class="wrap">{pillars()}</div></section>

<section class="band"><div class="wrap"><div class="split">
  <div>
    {eyebrow("How we work")}
    <h2>Staffing built on clarity, not volume</h2>
    <p>Every engagement starts with a discovery conversation and ends with a placement both sides are proud of. Contract, contract-to-hire, and direct placement across healthcare, administrative, light industrial, finance, and technology.</p>
    <div class="ctas" style="display:flex;gap:14px;flex-wrap:wrap;margin-top:8px">
      <a class="btn dark" href="/clients/">Explore staffing solutions</a>
      <a class="btn outline" href="/insights/">Read our insights</a>
    </div>
  </div>
  {stats_bar()}
</div></div></section>

<section class="band alt"><div class="wrap">
  {eyebrow("Core industries")}
  <h2>Five verticals, one standard of rigor</h2>
  <div class="grid c3" style="margin-top:26px">
    <a class="card linked" href="/industries/healthcare/"><h3 class="mt0">Healthcare</h3><p>Credentialed clinical and support staff, screened for compliance from day one.</p><span class="more">Healthcare staffing &rarr;</span></a>
    <a class="card linked" href="/industries/administrative/"><h3 class="mt0">Administrative</h3><p>Front-office and operations professionals who keep the business moving.</p><span class="more">Administrative staffing &rarr;</span></a>
    <a class="card linked" href="/industries/light-industrial/"><h3 class="mt0">Light Industrial</h3><p>Reliable warehouse, production, and logistics talent for every shift.</p><span class="more">Light industrial staffing &rarr;</span></a>
    <a class="card linked" href="/industries/finance-accounting/"><h3 class="mt0">Finance &amp; Accounting</h3><p>Accountants, analysts, and finance leads, from close crunch to permanent hires.</p><span class="more">Finance staffing &rarr;</span></a>
    <a class="card linked" href="/industries/technology/"><h3 class="mt0">Technology</h3><p>Engineers and IT professionals matched on stack, seniority, and team fit.</p><span class="more">Technology staffing &rarr;</span></a>
  </div>
</div></section>
''', band=True, current="", head_extra=jsonld()))

# ---- Clients hub
written.append(shell("/clients/", "Staffing Solutions for Employers | Elite Career Compass",
  "Contract, contract-to-hire, and direct placement staffing built on clarity, not volume. A qualified slate in 48 hours and a dedicated recruiter on every search.",
  f'''
<section class="hero short"><div class="wrap">
  {eyebrow("For Clients")}
  <h1>Staffing built on clarity, not volume</h1>
  <p class="lead">You don&rsquo;t need a stack of resumes. You need the right person, vetted and ready, with a recruiter who stays engaged well past day one.</p>
  <div class="ctas"><a class="btn gold" href="/request-talent/">Request Talent</a><a class="btn ghost-dark" href="tel:{PHONE_TEL}">Call {PHONE}</a></div>
</div></section>

<section class="band"><div class="wrap">{stats_bar()}</div></section>

<section class="band alt"><div class="wrap">
  {eyebrow("Engagement models")}
  <h2>Three ways to work with us</h2>
  <p>Every engagement starts with a discovery conversation about your roadmap. Then we match the model to your risk tolerance and timeline.</p>
  <div class="grid c3" style="margin-top:26px">
    <a class="card linked" href="/clients/contract-staffing/"><h3 class="mt0">Contract Staffing</h3><p>Vetted professionals on our payroll for surges, projects, and coverage. You get flexibility without the hiring admin.</p><span class="more">How contract works &rarr;</span></a>
    <a class="card linked" href="/clients/contract-to-hire/"><h3 class="mt0">Contract-to-Hire</h3><p>Work together first, commit when the fit is proven. The lowest-risk path to a permanent hire.</p><span class="more">How contract-to-hire works &rarr;</span></a>
    <a class="card linked" href="/clients/direct-placement/"><h3 class="mt0">Direct Placement</h3><p>A retained-quality search for permanent roles: benchmarked, screened, and guaranteed by our process.</p><span class="more">How direct placement works &rarr;</span></a>
  </div>
</div></section>

<section class="band"><div class="wrap"><div class="split">
  <div>
    {eyebrow("What clarity looks like")}
    <h2>The ECC process</h2>
    <ol class="steps">
      <li><h3>Discovery conversation</h3><p>We map the role to your roadmap: the outcomes it owns, the team it joins, the market it hires from.</p></li>
      <li><h3>A qualified slate in 48 hours</h3><p>Interviewed, screened, and reference-checked candidates, with compensation benchmarks instead of guesses.</p></li>
      <li><h3>Placement and follow-through</h3><p>Your dedicated recruiter stays with both sides well past day one. That&rsquo;s how retention reaches 92%.</p></li>
    </ol>
  </div>
  <div>
    {eyebrow("Why one recruiter matters")}
    <h2>1:1, not a queue</h2>
    <p>Every search gets one dedicated recruiter who learns your business once and carries that context through every conversation. No hand-offs, no re-explaining, no generic req list.</p>
    <p>That focus is why our first slate averages 48 hours, and why the people we place are still there a year later.</p>
    <a class="btn dark" href="/request-talent/">Request Talent</a>
  </div>
</div></div></section>
''', current="clients"))

# ---- Service pages
def service_page(slug, name, title, desc, lead, use_when, process_extra, risk):
    body = f'''
<section class="hero short"><div class="wrap">
  <p class="crumbs" style="color:var(--on-dark-muted)"><a href="/clients/" style="color:var(--on-dark-muted)">For Clients</a> / {name}</p>
  {eyebrow("Engagement model")}
  <h1>{title}</h1>
  <p class="lead">{lead}</p>
  <div class="ctas"><a class="btn gold" href="/request-talent/">Request Talent</a></div>
</div></section>
<section class="band"><div class="wrap"><div class="split">
  <div>
    <h2>When to use it</h2>
    <ul class="checklist">{use_when}</ul>
    <h2 style="margin-top:1.2em">How it works</h2>
    <ol class="steps">
      <li><h3>Discovery conversation</h3><p>We map the role to your roadmap: outcomes, team, market.</p></li>
      <li><h3>Qualified slate in 48 hours</h3><p>Interviewed, screened, reference-checked, benchmarked.</p></li>
      {process_extra}
    </ol>
  </div>
  <div>
    <h2>Your risk</h2>
    <p>{risk}</p>
    {stats_bar()}
    <div style="margin-top:22px"><a class="btn dark" href="/request-talent/">Request Talent</a></div>
  </div>
</div></div></section>'''
    return shell(f"/clients/{slug}/", f"{name} | Elite Career Compass", desc, body, current="clients")

written.append(service_page("contract-staffing", "Contract Staffing",
  "Contract staffing that flexes with your workload",
  "Contract staffing from Elite Career Compass: vetted professionals on our payroll for surges, projects, and coverage, without the hiring admin.",
  "Vetted professionals on our payroll, working on your team through surges, projects, leaves, and seasonal demand.",
  "<li>Workload is up but headcount is capped</li><li>A project needs skills you don&rsquo;t keep on staff</li><li>Coverage for leave or turnover, starting fast</li><li>You want output now and options later</li>",
  "<li><h3>Start, supported</h3><p>We handle payroll and the employment admin; your recruiter checks in with both sides through the assignment.</p></li>",
  "Minimal. Contractors are on our payroll, engagements flex with your demand, and you&rsquo;re never paying for a bench you don&rsquo;t need."))

written.append(service_page("contract-to-hire", "Contract-to-Hire",
  "Contract-to-hire: prove the fit before you commit",
  "Contract-to-hire staffing from Elite Career Compass: work together first, convert when the fit is proven. The lowest-risk path to a permanent hire.",
  "Work together first. Convert when the fit is proven. The lowest-risk path to a permanent hire.",
  "<li>The role is permanent but the budget or certainty isn&rsquo;t there yet</li><li>Culture fit matters as much as the skills list</li><li>A past bad hire made the team cautious</li><li>You want to see real work, not interview performance</li>",
  "<li><h3>Work together</h3><p>The candidate joins on contract; your recruiter gathers feedback from both sides at set milestones.</p></li><li><h3>Convert with confidence</h3><p>When it&rsquo;s working, conversion is simple and pre-agreed. No renegotiation surprises.</p></li>",
  "You evaluate real performance on real work before extending an offer. Most of the risk of a permanent hire is spent before you commit."))

written.append(service_page("direct-placement", "Direct Placement",
  "Direct placement search for permanent roles",
  "Direct placement recruiting from Elite Career Compass: a benchmarked, screened permanent-hire search with a dedicated recruiter. No placement, no fee.",
  "A focused search for the permanent hire your roadmap depends on. Benchmarked, screened, and delivered by one dedicated recruiter.",
  "<li>A permanent role that&rsquo;s core to the roadmap</li><li>A confidential search or a hard-to-find profile</li><li>Compensation needs market data, not guesswork</li><li>Your team doesn&rsquo;t have time to run a real search</li>",
  "<li><h3>Offer and land</h3><p>We manage offers with real compensation benchmarks and stay through onboarding. That&rsquo;s why 92% of our placements are still in seat past one year.</p></li>",
  "No placement, no fee. You pay when the right person accepts, and our follow-through past day one is why they stay."))

# ---- Industry pages
def industry_page(slug, name, title, desc, lead, points, roles):
    body = f'''
<section class="hero short"><div class="wrap">
  <p class="crumbs" style="color:var(--on-dark-muted)"><a href="/clients/" style="color:var(--on-dark-muted)">For Clients</a> / Industries / {name}</p>
  {eyebrow("Industries we serve")}
  <h1>{title}</h1>
  <p class="lead">{lead}</p>
  <div class="ctas"><a class="btn gold" href="/request-talent/">Request Talent</a><a class="btn ghost-dark" href="/apply/?vertical={slug}">Work in {name.lower()}? Apply</a></div>
</div></section>
<section class="band"><div class="wrap"><div class="split">
  <div>
    <h2>What we screen for</h2>
    <ul class="checklist">{points}</ul>
    <p>Contract, contract-to-hire, or direct placement, matched to how your team actually hires.</p>
  </div>
  <div>
    <h2>Roles we place</h2>
    <ul class="checklist">{roles}</ul>
    <div style="margin-top:18px"><a class="btn dark" href="/request-talent/">Request Talent</a></div>
  </div>
</div></div></section>'''
    return shell(f"/industries/{slug}/", f"{name} Staffing | Elite Career Compass", desc, body, current="clients")

written.append(industry_page("healthcare", "Healthcare",
  "Healthcare staffing with compliance built in",
  "Healthcare staffing from Elite Career Compass: credentialed clinical and support professionals, screened for licensure and compliance before you ever see them.",
  "Credentialed professionals for clinical and support roles. Licensure is verified and compliance screened before a resume ever reaches you.",
  "<li>Active licensure and certifications, verified</li><li>Immunization and background requirements met up front</li><li>Experience matched to your care setting and patient volume</li><li>Reliability references from clinical supervisors</li>",
  "<li>Medical assistants and patient care staff</li><li>Front-office, intake, and billing coordinators</li><li>Medical records and administrative support</li><li>Allied health and clinic operations roles</li>"))

written.append(industry_page("administrative", "Administrative",
  "Administrative professionals who run the office",
  "Administrative staffing from Elite Career Compass: executive assistants, office managers, and coordinators screened on the software and pace your office runs on.",
  "The front office is your first impression and your operational backbone. We staff it with people screened on the software, pace, and polish your business runs on.",
  "<li>Proficiency on your actual software: scheduling, CRM, office suites</li><li>Communication tested in writing and on the phone</li><li>Discretion and judgment references for executive support</li><li>Typing, data accuracy, and multi-tasking benchmarks</li>",
  "<li>Executive and administrative assistants</li><li>Office managers and coordinators</li><li>Receptionists and front-desk staff</li><li>Data entry and records specialists</li>"))

written.append(industry_page("light-industrial", "Light Industrial",
  "Light industrial staffing that shows up",
  "Light industrial staffing from Elite Career Compass: dependable warehouse, production, and logistics workers, safety-screened for every shift.",
  "Every unfilled shift costs you throughput. We place dependable warehouse, production, and logistics workers who are safety-screened and ready to work.",
  "<li>Safety training and equipment certifications verified</li><li>Attendance and reliability references checked</li><li>Physical requirements and shift fit confirmed honestly</li><li>Forklift and machine operation validated where required</li>",
  "<li>Warehouse associates and pickers/packers</li><li>Machine operators and assemblers</li><li>Forklift operators and material handlers</li><li>Shipping, receiving, and inventory staff</li>"))

written.append(industry_page("finance-accounting", "Finance & Accounting",
  "Finance &amp; accounting talent, benchmarked to market",
  "Finance and accounting staffing from Elite Career Compass: accountants, analysts, and finance leads for the close, the audit, and the permanent seat.",
  "From close crunch to a permanent controller, we place finance professionals vetted on the systems, standards, and deadlines your numbers depend on.",
  "<li>Systems experience verified (ERP, GL, reporting tools)</li><li>Technical screening against the actual work of the role</li><li>Confidentiality and controls awareness referenced</li><li>Compensation benchmarked with current market data</li>",
  "<li>Staff and senior accountants</li><li>AP/AR specialists and payroll</li><li>Financial analysts and FP&amp;A</li><li>Controllers and accounting managers</li>"))

written.append(industry_page("technology", "Technology",
  "Technology hires matched on stack and team fit",
  "Technology staffing from Elite Career Compass: engineers and IT professionals matched on stack, seniority, and how your team actually works.",
  "A resume keyword match isn&rsquo;t a fit. We match engineers and IT professionals on stack, seniority, and how your team actually builds.",
  "<li>Hands-on screening against your stack, not buzzwords</li><li>Seniority calibrated to the work, not the title</li><li>Team-fit signals from real references</li><li>Contract, contract-to-hire, or direct, matched to project risk</li>",
  "<li>Software engineers and developers</li><li>IT support and systems administrators</li><li>QA, data, and analytics roles</li><li>Project and product coordinators</li>"))

# ---- Request Talent
written.append(shell("/request-talent/", "Request Talent | Elite Career Compass",
  "Tell us who you need. A dedicated recruiter responds within one business day, and your first qualified slate averages 48 hours.",
  f'''
<section class="hero short"><div class="wrap">
  {eyebrow("For Clients")}
  <h1>Request Talent</h1>
  <p class="lead">Tell us who you need. One dedicated recruiter takes it from there.</p>
</div></section>
<section class="band"><div class="wrap"><div class="split">
  <div>
    {form("talent")}
  </div>
  <div>
    <div class="promise"><span aria-hidden="true">&#128337;</span><p><strong>A recruiter responds within one business day.</strong> Your first qualified slate averages 48 hours.</p></div>
    <div style="margin-top:22px">{stats_bar()}</div>
    <p style="margin-top:22px">Not sure which engagement model fits? Start with the <a href="/clients/">clients overview</a> or just describe the need above. Matching the model is our job.</p>
  </div>
</div></div></section>
''', band=False, current="clients"))

# ---- Applicants hub
written.append(shell("/applicants/", "For Applicants | Elite Career Compass",
  "A recruiting partner that works for you, free of charge: real recruiters, honest answers on pay, and roles that are never posted publicly.",
  f'''
<section class="hero short"><div class="wrap">
  {eyebrow("For Applicants")}
  <h1>A clear bearing on your next move</h1>
  <p class="lead">You&rsquo;re not a resume in a pile here. One recruiter, real conversations, honest answers about pay and fit. And it never costs you a thing.</p>
  <div class="ctas"><a class="btn gold" href="/apply/">Apply Now</a><a class="btn ghost-dark" href="/applicants/open-roles/">See Open Roles</a></div>
</div></section>
<section class="band"><div class="wrap">
  <div class="grid c3">
    <div class="card"><h3 class="mt0">Always free to you</h3><p>Employers pay our fee, never you. Your pay is your pay.</p></div>
    <div class="card"><h3 class="mt0">Roles you won&rsquo;t find posted</h3><p>Most of our placements are never advertised. Applying puts you in the room.</p></div>
    <div class="card"><h3 class="mt0">A human who stays</h3><p>Your recruiter sticks with you past day one, through the assignment and on to what&rsquo;s next.</p></div>
  </div>
</div></section>
<section class="band alt"><div class="wrap"><div class="split">
  <div>
    {eyebrow("Three steps")}
    <h2>How it works</h2>
    <ol class="steps">
      <li><h3>Apply in about 2 minutes</h3><p>Name, contact, field of work. Resume optional. No resume yet is fine.</p></li>
      <li><h3>Talk with your recruiter</h3><p>A real conversation within one business day: what you want, what you&rsquo;re great at, what pay looks like.</p></li>
      <li><h3>Get placed and stay supported</h3><p>Contract, contract-to-hire, or direct. Your recruiter stays with you well past day one.</p></li>
    </ol>
    <a class="btn dark" href="/applicants/how-it-works/">More about the process</a>
  </div>
  <div>
    {eyebrow("Where we place")}
    <h2>Five fields</h2>
    <ul class="checklist">
      <li><a href="/apply/?vertical=healthcare">Healthcare</a></li>
      <li><a href="/apply/?vertical=administrative">Administrative</a></li>
      <li><a href="/apply/?vertical=light-industrial">Light Industrial</a></li>
      <li><a href="/apply/?vertical=finance-accounting">Finance &amp; Accounting</a></li>
      <li><a href="/apply/?vertical=technology">Technology</a></li>
    </ul>
    <a class="btn gold" href="/apply/">Apply Now</a>
  </div>
</div></div></section>
''', current="applicants"))

# ---- How It Works (applicants)
written.append(shell("/applicants/how-it-works/", "How It Works for Applicants | Elite Career Compass",
  "Apply in about two minutes, talk with a dedicated recruiter within one business day, and get placed with support past day one. Always free to candidates.",
  f'''
<section class="hero short"><div class="wrap">
  <p class="crumbs" style="color:var(--on-dark-muted)"><a href="/applicants/" style="color:var(--on-dark-muted)">For Applicants</a> / How It Works</p>
  {eyebrow("For Applicants")}
  <h1>How working with ECC works</h1>
  <p class="lead">No black hole. No fees. No pretending a job is something it isn&rsquo;t.</p>
</div></section>
<section class="band"><div class="wrap"><div class="split">
  <div>
    <ol class="steps">
      <li><h3>Apply in about 2 minutes</h3><p>The form asks for your name, contact, and field of work. A resume helps but isn&rsquo;t required. Plenty of great candidates start without one.</p></li>
      <li><h3>Hear back within one business day</h3><p>A dedicated recruiter (one person, not a rotation) calls to talk about what you want, what you&rsquo;re strong at, and what pay honestly looks like in your market.</p></li>
      <li><h3>Interview for real matches</h3><p>We only put you forward for roles we&rsquo;d take seriously ourselves, with straight answers on pay, schedule, and start date before you say yes.</p></li>
      <li><h3>Start work, stay supported</h3><p>Your recruiter checks in past day one and stays your advocate on this assignment and the next move after it.</p></li>
    </ol>
  </div>
  <div>
    <h2>The straight answers</h2>
    <h3>Does this cost me anything?</h3>
    <p>No. Employers pay our fee, never you. Your pay is your pay.</p>
    <h3>Is staffing just dead-end temp work?</h3>
    <p>Contract-to-hire is one of the most reliable doors into a permanent role. You prove yourself on the job instead of in an interview.</p>
    <h3>Will I actually hear back?</h3>
    <p>Within one business day. If we can&rsquo;t help yet, we say so instead of going quiet.</p>
    <a class="btn gold" href="/apply/">Apply Now</a>
  </div>
</div></div></section>
''', current="applicants"))

# ---- Open Roles
written.append(shell("/applicants/open-roles/", "Open Roles | Elite Career Compass",
  "Browse the fields Elite Career Compass places in (healthcare, administrative, light industrial, finance, and technology) and apply in about two minutes.",
  f'''
<section class="hero short"><div class="wrap">
  <p class="crumbs" style="color:var(--on-dark-muted)"><a href="/applicants/" style="color:var(--on-dark-muted)">For Applicants</a> / Open Roles</p>
  {eyebrow("For Applicants")}
  <h1>Open Roles</h1>
  <p class="lead">Most of our placements are never posted publicly. Clients bring us searches directly. The fastest way in is to apply.</p>
</div></section>
<section class="band"><div class="wrap">
  <div class="roles-empty">
    <h2>New searches open every week</h2>
    <p style="margin-left:auto;margin-right:auto">Public postings appear here as clients approve them. Don&rsquo;t wait on a listing. When you apply, your recruiter matches you against every open search, posted or not.</p>
    <a class="btn gold" href="/apply/">Apply Now (about 2 minutes)</a>
  </div>
  <h2 style="margin-top:48px">Pick your field to get started</h2>
  <div class="grid c3" style="margin-top:20px">
    <a class="card linked" href="/apply/?vertical=healthcare"><h3 class="mt0">Healthcare</h3><p>Clinical support, front office, billing, records.</p><span class="more">Apply in healthcare &rarr;</span></a>
    <a class="card linked" href="/apply/?vertical=administrative"><h3 class="mt0">Administrative</h3><p>Executive assistants, office managers, coordinators.</p><span class="more">Apply in administrative &rarr;</span></a>
    <a class="card linked" href="/apply/?vertical=light-industrial"><h3 class="mt0">Light Industrial</h3><p>Warehouse, production, forklift, shipping &amp; receiving.</p><span class="more">Apply in light industrial &rarr;</span></a>
    <a class="card linked" href="/apply/?vertical=finance-accounting"><h3 class="mt0">Finance &amp; Accounting</h3><p>Accountants, AP/AR, analysts, controllers.</p><span class="more">Apply in finance &rarr;</span></a>
    <a class="card linked" href="/apply/?vertical=technology"><h3 class="mt0">Technology</h3><p>Engineers, IT support, QA, data roles.</p><span class="more">Apply in technology &rarr;</span></a>
  </div>
</div></section>
''', current="applicants"))

# ---- Apply
written.append(shell("/apply/", "Apply Now | Elite Career Compass",
  "Apply in about two minutes. Always free to candidates. A dedicated recruiter calls you back within one business day.",
  f'''
<section class="hero short"><div class="wrap">
  {eyebrow("For Applicants")}
  <h1>Apply Now</h1>
  <p class="lead">About two minutes. Always free. A real recruiter calls you back within one business day.</p>
</div></section>
<section class="band"><div class="wrap"><div class="split">
  <div>{form("apply")}</div>
  <div>
    <div class="promise"><span aria-hidden="true">&#128222;</span><p><strong>Your recruiter calls within one business day.</strong> If we can&rsquo;t help yet, we&rsquo;ll say so instead of going quiet.</p></div>
    <h3 style="margin-top:26px">What happens next</h3>
    <ul class="checklist">
      <li>A real conversation about what you want and what pay looks like</li>
      <li>Matching against every open search, posted or not</li>
      <li>Straight answers on pay, schedule, and start date before you commit</li>
    </ul>
    <p>Curious about the full process? Read <a href="/applicants/how-it-works/">how it works</a>.</p>
  </div>
</div></div></section>
''', band=False, current="applicants"))

# ---- About
written.append(shell("/about/", "About ECC | Elite Career Compass",
  "Why Elite Career Compass exists: a people-first staffing and recruiting partner built on direction, knowledge, and trust.",
  f'''
<section class="hero short"><div class="wrap">
  {eyebrow("About ECC")}
  <h1>Why the compass</h1>
  <p class="lead">Careers and companies both lose their way for the same reason: too much noise, not enough bearing. We started Elite Career Compass to be the steady point in between.</p>
</div></section>
<section class="band"><div class="wrap"><div class="split">
  <div>
    <h2>People-first, on purpose</h2>
    <p>Volume staffing treats candidates as inventory and clients as order numbers. We built ECC on the opposite premise: one dedicated recruiter per search, a discovery conversation before any resume moves, and follow-through that lasts well past day one.</p>
    <p>This is how we actually operate, and it shows in our numbers: first qualified slates in an average of 48 hours, and 92% of placements still in seat past one year.</p>
    <h2>What we stand on</h2>
    <p><strong>Direction.</strong> Search strategy shaped around your roadmap, not a generic req list.<br>
    <strong>Knowledge.</strong> Market data, compensation benchmarks, and screening rigor on every search.<br>
    <strong>Guidance.</strong> Real humans staying with candidates and clients well past day one.</p>
    <p>See the outcomes on our <a href="/about/results/">results page</a>.</p>
  </div>
  <div>
    {stats_bar()}
    <div class="note" style="margin-top:22px"><strong>Serving clients nationwide.</strong> Contract, contract-to-hire, and direct placement across healthcare, administrative, light industrial, finance, and technology.</div>
    <div style="display:flex;gap:12px;margin-top:22px;flex-wrap:wrap">
      <a class="btn dark" href="/request-talent/">Request Talent</a>
      <a class="btn outline" href="/apply/">Apply Now</a>
    </div>
  </div>
</div></div></section>
''', current="about"))

# ---- Results (testimonials to be added as they're collected)
written.append(shell("/about/results/", "Results | Elite Career Compass",
  "The numbers behind Elite Career Compass placements: 48-hour average first slates, 92% retention past one year, one dedicated recruiter per search.",
  f'''
<section class="hero short"><div class="wrap">
  <p class="crumbs" style="color:var(--on-dark-muted)"><a href="/about/" style="color:var(--on-dark-muted)">About ECC</a> / Results</p>
  {eyebrow("Proof")}
  <h1>Results we hold ourselves to</h1>
  <p class="lead">Staffing firms love adjectives. We prefer numbers.</p>
</div></section>
<section class="band"><div class="wrap">
  {stats_bar()}
  <div class="split" style="margin-top:44px">
    <div>
      <h2>What the numbers mean</h2>
      <p><strong>48 hours to a first qualified slate</strong> means vetted candidates, not a pile of resumes. Every candidate on a slate has been interviewed, screened, and reference-checked before you see them.</p>
      <p><strong>92% retention past one year</strong> is the number we&rsquo;re proudest of. Fast placements are easy; placements that last mean the match was right for both sides.</p>
      <p><strong>1:1</strong> means one dedicated recruiter owns your search end to end. Context never gets lost in a hand-off.</p>
    </div>
    <div>
      <h2>Client &amp; candidate stories</h2>
      <p>We&rsquo;re collecting stories from the employers and professionals we&rsquo;ve placed, with real names attached, because anonymous praise isn&rsquo;t proof. They&rsquo;ll appear here as they&rsquo;re approved.</p>
      <p>Worked with us? We&rsquo;d love to feature yours: <a href="mailto:{EMAIL}">{EMAIL}</a>.</p>
      <!-- Testimonial template (copy once per approved story):
      <blockquote class="card">
        <p>&ldquo;Quote.&rdquo;</p>
        <footer><strong>Full Name</strong>, Title, Company</footer>
      </blockquote>
      -->
    </div>
  </div>
</div></section>
''', current="about"))

# ---- Insights
written.append(shell("/insights/", "Insights | Elite Career Compass",
  "Practical guidance from Elite Career Compass for employers and candidates: engagement models, hiring clarity, and how to work with a recruiter.",
  f'''
<section class="hero short"><div class="wrap">
  {eyebrow("Insights")}
  <h1>Clarity, in writing</h1>
  <p class="lead">Short, useful reads for employers and job seekers.</p>
</div></section>
<section class="band"><div class="wrap">
  <div class="grid c2">
    <a class="card linked" href="/insights/contract-to-hire-vs-direct-placement/">
      <p class="eyebrow">For Clients</p>
      <h3 class="mt0">Contract-to-hire vs. direct placement: which fits your risk?</h3>
      <p>The two paths to a permanent hire, and how to pick based on certainty, budget, and how badly a mis-hire would hurt.</p>
      <span class="more">Read the guide &rarr;</span>
    </a>
    <a class="card linked" href="/insights/how-to-work-with-a-recruiter/">
      <p class="eyebrow">For Applicants</p>
      <h3 class="mt0">How to work with a recruiter (without getting ghosted)</h3>
      <p>What a good recruiter should do for you, the questions to ask up front, and the red flags that mean walk away.</p>
      <span class="more">Read the guide &rarr;</span>
    </a>
  </div>
  <p style="margin-top:30px">More guides are on the way. Have a question you want answered here? Tell us: <a href="mailto:{EMAIL}">{EMAIL}</a>.</p>
</div></section>
''', current="insights"))

POST_SHELL = '''
<section class="hero short"><div class="wrap">
  <p class="crumbs" style="color:var(--on-dark-muted)"><a href="/insights/" style="color:var(--on-dark-muted)">Insights</a> / {crumb}</p>
  {eyebrow}
  <h1>{h1}</h1>
</div></section>
<section class="band"><div class="wrap"><article class="post prose">
  <p class="post-meta">By Elite Career Compass</p>
  {body}
  <div style="margin-top:36px">{cta}</div>
</article></div></section>'''

written.append(shell("/insights/contract-to-hire-vs-direct-placement/",
  "Contract-to-Hire vs. Direct Placement | Elite Career Compass",
  "How to choose between contract-to-hire and direct placement for a permanent role, based on certainty, budget, and the cost of a mis-hire.",
  POST_SHELL.format(
    crumb="Contract-to-hire vs. direct placement",
    eyebrow=eyebrow("For Clients"),
    h1="Contract-to-hire vs. direct placement: which fits your risk?",
    body='''
<p>Both paths end in a permanent hire. The difference is when you commit, and what you know at that moment.</p>
<h2>Direct placement: commit on evidence gathered up front</h2>
<p>In a direct placement search, the vetting happens before the offer: structured interviews, reference checks, compensation benchmarks, and a recruiter who has screened for the real work of the role. You commit on day one, on strong but indirect evidence.</p>
<p>Choose it when the role is well-defined, the budget is certain, and speed to a committed hire matters. Think senior roles, confidential searches, and roles where asking someone to start on contract would shrink your candidate pool.</p>
<h2>Contract-to-hire: commit on evidence from the job itself</h2>
<p>Contract-to-hire moves the decision after weeks of real work. You see actual output, actual collaboration, actual reliability. The candidate sees the real job too. Conversion terms are agreed before the start, so there&rsquo;s no renegotiation cliff.</p>
<p>Choose it when certainty is the constraint: a new role you&rsquo;re still shaping, a team recovering from a mis-hire, or a budget that opens next quarter but work that starts now.</p>
<h2>A simple rule of thumb</h2>
<p>Ask what a mis-hire would cost you in money, momentum, and team trust. The higher that cost and the fuzzier the role, the more contract-to-hire earns its keep. The clearer the role and the more competitive the talent market, the more direct placement wins.</p>
<p>And if you&rsquo;re not sure, that&rsquo;s literally our job: describe the need, and we&rsquo;ll recommend the model.</p>''',
    cta='<a class="btn dark" href="/request-talent/">Request Talent</a>'),
  current="insights"))

written.append(shell("/insights/how-to-work-with-a-recruiter/",
  "How to Work with a Recruiter | Elite Career Compass",
  "What a good staffing recruiter should do for you, the questions to ask up front, and the red flags that mean you should walk away.",
  POST_SHELL.format(
    crumb="How to work with a recruiter",
    eyebrow=eyebrow("For Applicants"),
    h1="How to work with a recruiter (without getting ghosted)",
    body='''
<p>A good recruiter is a free advocate with access to jobs that never get posted. A bad one is a black hole with a LinkedIn account. Here&rsquo;s how to tell the difference and get the most from the good ones.</p>
<h2>First, know how the money works</h2>
<p>The employer pays the recruiting fee. Always. If anyone asks <em>you</em> to pay to be placed, walk away. Legitimate staffing doesn&rsquo;t work that way. Your pay is your pay.</p>
<h2>Questions to ask in the first call</h2>
<ul>
<li><strong>&ldquo;Will I work with you specifically?&rdquo;</strong> One consistent recruiter beats a rotating queue because context matters.</li>
<li><strong>&ldquo;What&rsquo;s the actual pay range?&rdquo;</strong> A straight answer is a green flag. &ldquo;Competitive&rdquo; is not an answer.</li>
<li><strong>&ldquo;When will I hear back, either way?&rdquo;</strong> Good recruiters give a timeframe and keep it, including for a no.</li>
<li><strong>&ldquo;Is this contract, contract-to-hire, or direct?&rdquo;</strong> Each is fine; not knowing which is not.</li>
</ul>
<h2>How to be the candidate recruiters fight for</h2>
<p>Be reachable, be honest about what you want (including pay), and tell your recruiter about every other process you&rsquo;re in. None of that hurts you. It lets them move faster and negotiate better on your behalf.</p>
<h2>The red flags</h2>
<p>Vague answers on pay. Pressure to accept on the spot. Radio silence after an interview they arranged. Any fee, ever. If you hit two of these, find a better advocate. Good ones exist, and they cost you nothing.</p>''',
    cta='<a class="btn gold" href="/apply/">Apply Now</a>'),
  current="insights"))

# ---- Contact
written.append(shell("/contact/", "Contact ECC | Elite Career Compass",
  "Contact Elite Career Compass: email info@eccstaffing.com, call (737) 423-3422, or send a message. Serving clients nationwide.",
  f'''
<section class="hero short"><div class="wrap">
  {eyebrow("Contact")}
  <h1>Start the conversation</h1>
  <p class="lead">Hiring soon, or looking for your next role? We answer within one business day.</p>
</div></section>
<section class="band"><div class="wrap"><div class="split">
  <div>{form("contact")}</div>
  <div>
    <h2>Reach us directly</h2>
    <ul class="checklist">
      <li>Email: <a href="mailto:{EMAIL}">{EMAIL}</a></li>
      <li>Phone: <a href="tel:{PHONE_TEL}">{PHONE}</a></li>
      <li>Serving clients nationwide</li>
    </ul>
    <div class="promise" style="margin-top:18px"><span aria-hidden="true">&#128337;</span><p><strong>We respond within one business day.</strong></p></div>
    <h3 style="margin-top:26px">In a hurry?</h3>
    <p>Hiring: go straight to <a href="/request-talent/">Request Talent</a>.<br>Job seeking: go straight to <a href="/apply/">Apply Now</a>.</p>
  </div>
</div></div></section>
''', band=False, current="", head_extra=jsonld()))

# ---- Thanks pages
def thanks(kind, h1, msg, links):
    return shell(f"/thanks/{kind}/", "Thank You | Elite Career Compass",
      "Your message is on its way to Elite Career Compass.",
      f'''
<section class="hero short"><div class="wrap">
  {eyebrow("Message sent")}
  <h1>{h1}</h1>
  <p class="lead">{msg}</p>
  <div class="ctas">{links}</div>
</div></section>''', band=False)

written.append(thanks("talent", "Your request is in",
  "A dedicated recruiter will respond within one business day, and your first qualified slate averages 48 hours. Need us sooner? Call " + PHONE + ".",
  '<a class="btn gold" href="/clients/">Explore engagement models</a><a class="btn ghost-dark" href="/about/results/">See our results</a>'))
written.append(thanks("apply", "Application received",
  "Your recruiter will call within one business day. In the meantime, see how the process works so you know exactly what to expect.",
  '<a class="btn gold" href="/applicants/how-it-works/">How it works</a><a class="btn ghost-dark" href="/insights/how-to-work-with-a-recruiter/">Working with a recruiter</a>'))
written.append(thanks("contact", "Message received",
  "We respond within one business day. If your question is about hiring or finding work, these will get you moving now.",
  '<a class="btn gold" href="/request-talent/">Request Talent</a><a class="btn ghost-dark" href="/apply/">Apply Now</a>'))

# ---- Legal / utility
LEGAL_NOTE = '<div class="note" style="margin-top:26px"><strong>Note to ECC:</strong> this page is a starting draft for launch. Have it reviewed by counsel and replace this notice before go-live.</div>'

written.append(shell("/privacy/", "Privacy Policy | Elite Career Compass",
  "How Elite Career Compass collects, uses, and protects the information you share through eccstaffing.com.",
  f'''
<section class="hero short"><div class="wrap">{eyebrow("Legal")}<h1>Privacy Policy</h1></div></section>
<section class="band"><div class="wrap"><div class="prose">
<p>Elite Career Compass LLC (&ldquo;ECC,&rdquo; &ldquo;we&rdquo;) collects the information you submit through this site (such as your name, contact details, and resume) solely to provide staffing and recruiting services: responding to your inquiry, matching candidates with roles, and communicating with you about them.</p>
<p>We do not sell your personal information. We share it only as needed to provide our services (for example, presenting a candidate&rsquo;s profile to a hiring client with the candidate&rsquo;s knowledge) or as required by law.</p>
<p>Form submissions from this site are delivered to <a href="mailto:{EMAIL}">{EMAIL}</a>. To ask what information we hold about you, or to request correction or deletion, email us at that address.</p>
{LEGAL_NOTE}
</div></div></section>''', band=False))

written.append(shell("/terms/", "Terms of Use | Elite Career Compass",
  "Terms of use for eccstaffing.com, the website of Elite Career Compass LLC.",
  f'''
<section class="hero short"><div class="wrap">{eyebrow("Legal")}<h1>Terms of Use</h1></div></section>
<section class="band"><div class="wrap"><div class="prose">
<p>By using eccstaffing.com you agree to use the site lawfully and to submit only information that is accurate and yours to share. Content on this site is provided for general information about our services and is not an offer of employment or a guarantee of placement.</p>
<p>All site content and branding are the property of Elite Career Compass LLC and may not be reused without permission. Questions about these terms: <a href="mailto:{EMAIL}">{EMAIL}</a>.</p>
{LEGAL_NOTE}
</div></div></section>''', band=False))

written.append(shell("/accessibility/", "Accessibility | Elite Career Compass",
  "Elite Career Compass is committed to a website that everyone can use. Report an accessibility barrier to info@eccstaffing.com.",
  f'''
<section class="hero short"><div class="wrap">{eyebrow("Accessibility")}<h1>Accessibility</h1></div></section>
<section class="band"><div class="wrap"><div class="prose">
<p>We want everyone to be able to use this site, including people using screen readers, keyboard navigation, or magnification. The site is built with semantic headings, labeled forms, visible focus states, and color contrast aimed at WCAG&nbsp;2.1&nbsp;AA.</p>
<p>If anything on this site is hard for you to use, tell us and we&rsquo;ll fix it: <a href="mailto:{EMAIL}">{EMAIL}</a> or <a href="tel:{PHONE_TEL}">{PHONE}</a>. If a form is a barrier, you can complete any request (hiring, applying, or general) entirely by phone or email.</p>
</div></div></section>''', band=False))

# ---- 404 (flat file for host config)
written.append(shell("/404.html", "Page Not Found | Elite Career Compass",
  "That page has wandered off the map. Find your bearing: hire talent, find a role, or contact Elite Career Compass.",
  f'''
<section class="hero short"><div class="wrap">
  {eyebrow("404")}
  <h1>Off the map</h1>
  <p class="lead">That page doesn&rsquo;t exist, but your bearing is easy to recover.</p>
  <div class="ctas">
    <a class="btn gold" href="/request-talent/">Request Talent</a>
    <a class="btn ghost-dark" href="/apply/">Apply Now</a>
    <a class="btn ghost-dark" href="/">Back to home</a>
  </div>
</div></section>''', band=False))

# ---- Admin console (unlinked from nav; noindex; see README for host-level protection)
written.append(shell("/admin/", "Owner Console | Elite Career Compass",
  "Management console for the eccstaffing.com owner: platform sign-ins and site tasks.",
  f'''
<section class="hero short"><div class="wrap">
  {eyebrow("Owner console")}
  <h1>Manage eccstaffing.com</h1>
  <p class="lead">Every platform that runs this site, in one place. Each link below goes to that platform&rsquo;s own secure sign-in. This page stores no passwords and grants no access by itself.</p>
</div></section>

<section class="band"><div class="wrap">
  <div class="note"><strong>Keep this page private.</strong> It isn&rsquo;t linked from the site and is excluded from search engines, but the real protection is at your host: enable password protection (Deployment Protection on Vercel, password protection on Netlify, or HTTP basic auth) for <code>/admin/</code>, or simply bookmark the platform links and delete this page.</div>

  <h2 style="margin-top:34px">Sign in to your platforms</h2>
  <div class="grid c3" style="margin-top:20px">
    <a class="card linked" href="https://mail.google.com/" rel="noopener"><h3 class="mt0">Lead inbox</h3><p>Every form on the site delivers to <strong>info@eccstaffing.com</strong>. Sign in to your mail provider to triage <code>[Talent Request]</code>, <code>[Application]</code>, and <code>[Contact]</code> messages.</p><span class="more">Open webmail &rarr;</span></a>
    <a class="card linked" href="https://formsubmit.co/" rel="noopener"><h3 class="mt0">Form delivery</h3><p>FormSubmit relays the three site forms to your inbox. Manage or reset the connection for info@eccstaffing.com here.</p><span class="more">Open FormSubmit &rarr;</span></a>
    <a class="card linked" href="https://vercel.com/login" rel="noopener"><h3 class="mt0">Hosting &amp; deploys</h3><p>Where the site is served. Redeploy, view traffic, set the custom domain, and turn on password protection for this page.</p><span class="more">Open hosting dashboard &rarr;</span></a>
    <a class="card linked" href="https://search.google.com/search-console" rel="noopener"><h3 class="mt0">Google Search Console</h3><p>How the site appears in Google. Submit <code>/sitemap.xml</code> once after launch, then watch queries and indexing here.</p><span class="more">Open Search Console &rarr;</span></a>
    <a class="card linked" href="https://business.google.com/" rel="noopener"><h3 class="mt0">Google Business Profile</h3><p>Your listing on Google Maps and local search, and where client reviews accumulate. Decide the Texas/Austin geo question here.</p><span class="more">Open Business Profile &rarr;</span></a>
    <a class="card linked" href="https://www.linkedin.com/company/setup/new/" rel="noopener"><h3 class="mt0">LinkedIn</h3><p>The channel where staffing clients actually look. Keep the company page pointing at eccstaffing.com.</p><span class="more">Open LinkedIn &rarr;</span></a>
  </div>

  <h2 style="margin-top:44px">Manage the site</h2>
  <div class="split" style="margin-top:20px">
    <div>
      <h3>Routine tasks</h3>
      <ul class="checklist">
        <li><strong>Test the forms monthly:</strong> submit <a href="/request-talent/">Request Talent</a>, <a href="/apply/">Apply</a>, and <a href="/contact/">Contact</a>, and confirm each lands at info@eccstaffing.com</li>
        <li><strong>Answer within the promise:</strong> the site tells clients one business day and candidates one business day, so inbox response time is the brand</li>
        <li><strong>Add real proof as it arrives:</strong> approved testimonials go into <a href="/about/results/">Results</a> (template is in the page&rsquo;s HTML comments)</li>
        <li><strong>Post roles when public:</strong> real openings replace the &ldquo;apply anyway&rdquo; state on <a href="/applicants/open-roles/">Open Roles</a></li>
      </ul>
    </div>
    <div>
      <h3>Editing pages</h3>
      <p>The site is plain HTML, so any web developer can edit it. Source of truth lives in the project repo; <code>_build/generate.py</code> regenerates every page and <code>_build/audit.py</code> re-verifies links, email routing, and accessibility before deploying.</p>
      <h3>Launch checklist</h3>
      <ul class="checklist">
        <li>info@eccstaffing.com mailbox live and monitored</li>
        <li>One test submission per form; FormSubmit activation email clicked</li>
        <li>Custom domain pointed at the host; HTTPS on</li>
        <li>Privacy &amp; Terms drafts reviewed by counsel</li>
        <li>Sitemap submitted in Search Console</li>
      </ul>
    </div>
  </div>
</div></section>
''', band=False, head_extra='<meta name="robots" content="noindex,nofollow">'))

# ---- sitemap + robots
pages_for_sitemap = [p for p in written if not p.endswith(".html") and not p.startswith(("/thanks/", "/admin/"))]
sm = ['<?xml version="1.0" encoding="UTF-8"?>',
      '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
for p in pages_for_sitemap:
    sm.append(f"  <url><loc>{SITE}{p}</loc></url>")
sm.append("</urlset>")
(ROOT / "sitemap.xml").write_text("\n".join(sm) + "\n", encoding="utf-8")
(ROOT / "robots.txt").write_text(f"User-agent: *\nAllow: /\nDisallow: /thanks/\nDisallow: /admin/\nSitemap: {SITE}/sitemap.xml\n", encoding="utf-8")

print(f"Generated {len(written)} pages + sitemap.xml + robots.txt")
for p in written: print("  ", p)
