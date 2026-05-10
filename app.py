# ============================================================
#  Muhammad Ahmed Ali — Portfolio  |  app.py
#  Run:  streamlit run app.py
#  Deps: pip install streamlit streamlit-option-menu
# ============================================================

import streamlit as st

# ── Page config ──────────────────────────────────────────────
st.set_page_config(
    page_title="Muhammad Ahmed Ali | Portfolio",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ── Global CSS ───────────────────────────────────────────────
st.markdown("""
<style>
/* ── Google Font ── */
@import url('https://fonts.googleapis.com/css2?family=Syne:wght@400;600;700;800&family=DM+Sans:ital,wght@0,300;0,400;0,500;1,300&display=swap');

/* ── Root tokens ── */
:root {
    --bg:         #0a0c12;
    --surface:    #111420;
    --glass:      rgba(255,255,255,0.04);
    --glass-b:    rgba(255,255,255,0.10);
    --accent:     #4f9cf9;
    --accent2:    #a78bfa;
    --accent3:    #34d399;
    --danger:     #f87171;
    --text:       #e2e8f0;
    --muted:      #64748b;
    --border:     rgba(255,255,255,0.07);
    --shadow:     0 8px 32px rgba(0,0,0,0.5);
    --radius:     16px;
    --radius-sm:  10px;
}

/* ── Global reset ── */
html, body, [class*="css"], .stApp {
    background-color: var(--bg) !important;
    color: var(--text) !important;
    font-family: 'DM Sans', sans-serif !important;
}

/* Hide Streamlit chrome */
#MainMenu, footer, header { visibility: hidden; }
.block-container { padding: 2rem 3rem !important; max-width: 1200px !important; }

/* ── Sidebar ── */
[data-testid="stSidebar"] {
    background: var(--surface) !important;
    border-right: 1px solid var(--border);
}
[data-testid="stSidebar"] * { color: var(--text) !important; }

/* ── Headings ── */
h1, h2, h3, h4 { font-family: 'Syne', sans-serif !important; }

/* ── Hero section ── */
.hero-wrapper {
    position: relative;
    padding: 4rem 3.5rem;
    border-radius: 24px;
    background: linear-gradient(135deg,
        rgba(79,156,249,0.08) 0%,
        rgba(167,139,250,0.06) 50%,
        rgba(52,211,153,0.06) 100%);
    border: 1px solid var(--border);
    overflow: hidden;
    margin-bottom: 2.5rem;
}
.hero-wrapper::before {
    content: "";
    position: absolute; inset: 0;
    background: radial-gradient(ellipse 80% 60% at 10% 30%,
        rgba(79,156,249,0.12) 0%, transparent 70%);
    pointer-events: none;
}
.hero-wrapper::after {
    content: "";
    position: absolute; top: -120px; right: -80px;
    width: 420px; height: 420px;
    background: radial-gradient(circle,
        rgba(167,139,250,0.15) 0%, transparent 70%);
    pointer-events: none;
}
.badge-pill {
    display: inline-block;
    background: rgba(79,156,249,0.15);
    color: var(--accent) !important;
    border: 1px solid rgba(79,156,249,0.3);
    border-radius: 50px;
    padding: 4px 16px;
    font-size: 0.78rem;
    font-weight: 500;
    letter-spacing: 0.08em;
    text-transform: uppercase;
    margin-bottom: 1rem;
}
.hero-name {
    font-family: 'Syne', sans-serif;
    font-size: clamp(2.4rem, 5vw, 4rem);
    font-weight: 800;
    line-height: 1.1;
    margin: 0 0 0.5rem;
    background: linear-gradient(135deg, #e2e8f0 30%, var(--accent) 75%, var(--accent2) 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
}
.hero-title {
    font-size: 1.1rem;
    color: var(--muted) !important;
    margin: 0 0 1.2rem;
    font-weight: 400;
}
.hero-bio {
    font-size: 1rem;
    line-height: 1.75;
    color: #94a3b8 !important;
    max-width: 620px;
    margin-bottom: 2rem;
}

/* ── Social buttons ── */
.btn-row { display: flex; gap: 12px; flex-wrap: wrap; }
.btn-social {
    display: inline-flex; align-items: center; gap: 8px;
    padding: 10px 22px;
    border-radius: 50px;
    font-size: 0.9rem; font-weight: 500;
    text-decoration: none !important;
    transition: all 0.25s ease;
    cursor: pointer;
}
.btn-github {
    background: rgba(255,255,255,0.06);
    border: 1px solid rgba(255,255,255,0.12);
    color: var(--text) !important;
}
.btn-github:hover { background: rgba(255,255,255,0.12); transform: translateY(-2px); }
.btn-linkedin {
    background: rgba(10,102,194,0.2);
    border: 1px solid rgba(10,102,194,0.4);
    color: #60a5fa !important;
}
.btn-linkedin:hover { background: rgba(10,102,194,0.35); transform: translateY(-2px); }
.btn-email {
    background: rgba(52,211,153,0.12);
    border: 1px solid rgba(52,211,153,0.3);
    color: var(--accent3) !important;
}
.btn-email:hover { background: rgba(52,211,153,0.22); transform: translateY(-2px); }

/* ── Section heading ── */
.section-label {
    font-size: 0.72rem;
    font-weight: 600;
    letter-spacing: 0.18em;
    text-transform: uppercase;
    color: var(--accent) !important;
    margin-bottom: 0.4rem;
}
.section-title {
    font-family: 'Syne', sans-serif;
    font-size: 2rem;
    font-weight: 700;
    margin: 0 0 2rem;
}

/* ── Divider ── */
.divider {
    height: 1px;
    background: linear-gradient(90deg, transparent, var(--border), transparent);
    margin: 2.5rem 0;
}

/* ── Glass card ── */
.card {
    background: var(--glass);
    border: 1px solid var(--border);
    border-radius: var(--radius);
    padding: 1.8rem;
    height: 100%;
    transition: border-color 0.3s, transform 0.3s, box-shadow 0.3s;
    position: relative;
    overflow: hidden;
}
.card::before {
    content: "";
    position: absolute; top: 0; left: 0; right: 0; height: 1px;
    background: linear-gradient(90deg, transparent, var(--glass-b), transparent);
}
.card:hover {
    border-color: rgba(79,156,249,0.3);
    transform: translateY(-4px);
    box-shadow: 0 20px 48px rgba(79,156,249,0.1);
}
.card-icon {
    font-size: 2.4rem;
    margin-bottom: 1rem;
    display: block;
}
.card-title {
    font-family: 'Syne', sans-serif;
    font-size: 1.2rem;
    font-weight: 700;
    margin-bottom: 0.6rem;
    color: var(--text) !important;
}
.card-desc {
    font-size: 0.9rem;
    line-height: 1.7;
    color: #94a3b8 !important;
    margin-bottom: 1.2rem;
}
.tag {
    display: inline-block;
    background: rgba(79,156,249,0.1);
    color: var(--accent) !important;
    border: 1px solid rgba(79,156,249,0.2);
    border-radius: 6px;
    padding: 3px 10px;
    font-size: 0.75rem;
    font-weight: 500;
    margin: 3px 3px 0 0;
}
.tag-purple {
    background: rgba(167,139,250,0.1);
    color: var(--accent2) !important;
    border-color: rgba(167,139,250,0.2);
}
.tag-green {
    background: rgba(52,211,153,0.1);
    color: var(--accent3) !important;
    border-color: rgba(52,211,153,0.2);
}
.card-link {
    display: inline-flex; align-items: center; gap: 6px;
    color: var(--accent) !important;
    font-size: 0.85rem; font-weight: 500;
    text-decoration: none;
    margin-top: 1rem;
    transition: gap 0.2s;
}
.card-link:hover { gap: 10px; }

/* ── Stat card ── */
.stat-card {
    background: var(--glass);
    border: 1px solid var(--border);
    border-radius: var(--radius-sm);
    padding: 1.4rem 1.6rem;
    text-align: center;
}
.stat-num {
    font-family: 'Syne', sans-serif;
    font-size: 2.2rem;
    font-weight: 800;
    background: linear-gradient(135deg, var(--accent), var(--accent2));
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
}
.stat-label { font-size: 0.82rem; color: var(--muted) !important; margin-top: 4px; }

/* ── Progress bars ── */
.skill-row { margin-bottom: 1.4rem; }
.skill-header { display: flex; justify-content: space-between; margin-bottom: 6px; }
.skill-name { font-size: 0.9rem; font-weight: 500; }
.skill-pct  { font-size: 0.85rem; color: var(--muted) !important; }
.progress-track {
    height: 6px;
    background: rgba(255,255,255,0.06);
    border-radius: 99px;
    overflow: hidden;
}
.progress-fill {
    height: 100%;
    border-radius: 99px;
    background: linear-gradient(90deg, var(--accent), var(--accent2));
}

/* ── Contact form ── */
.contact-card {
    background: var(--glass);
    border: 1px solid var(--border);
    border-radius: var(--radius);
    padding: 2rem 2.2rem;
}
.stTextInput > div > div > input,
.stTextArea > div > div > textarea {
    background: rgba(255,255,255,0.04) !important;
    border: 1px solid var(--border) !important;
    border-radius: var(--radius-sm) !important;
    color: var(--text) !important;
    font-family: 'DM Sans', sans-serif !important;
}
.stTextInput > div > div > input:focus,
.stTextArea > div > div > textarea:focus {
    border-color: var(--accent) !important;
    box-shadow: 0 0 0 2px rgba(79,156,249,0.15) !important;
}
.stTextInput label, .stTextArea label {
    color: #94a3b8 !important;
    font-size: 0.85rem !important;
}

/* ── Submit button ── */
.stButton > button {
    background: linear-gradient(135deg, var(--accent), #3b82f6) !important;
    color: #fff !important;
    border: none !important;
    border-radius: 50px !important;
    padding: 0.55rem 2.2rem !important;
    font-family: 'Syne', sans-serif !important;
    font-weight: 600 !important;
    font-size: 0.95rem !important;
    letter-spacing: 0.02em !important;
    transition: opacity 0.2s, transform 0.2s !important;
}
.stButton > button:hover { opacity: 0.88 !important; transform: translateY(-2px) !important; }

/* ── Footer ── */
.footer {
    text-align: center;
    color: var(--muted) !important;
    font-size: 0.8rem;
    padding: 2rem 0 1rem;
    border-top: 1px solid var(--border);
    margin-top: 3rem;
}

/* ── Sidebar nav overrides ── */
.nav-link { border-radius: 10px !important; }
.nav-link-selected {
    background: linear-gradient(135deg, rgba(79,156,249,0.2), rgba(167,139,250,0.15)) !important;
    color: var(--accent) !important;
}
</style>
""", unsafe_allow_html=True)

# ── Sidebar nav ─────────────────────────────────────────────
try:
    from streamlit_option_menu import option_menu
    with st.sidebar:
        st.markdown("""
        <div style='text-align:center; padding: 1.2rem 0 1.8rem;'>
            <div style='font-size:3rem; margin-bottom:.5rem;'>⚡</div>
            <div style='font-family:Syne,sans-serif; font-weight:700; font-size:1rem;
                        background:linear-gradient(135deg,#4f9cf9,#a78bfa);
                        -webkit-background-clip:text; -webkit-text-fill-color:transparent;'>
                M. Ahmed Ali
            </div>
            <div style='font-size:.75rem; color:#64748b; margin-top:4px;'>Python Developer</div>
        </div>
        """, unsafe_allow_html=True)

        page = option_menu(
            menu_title=None,
            options=["Home", "Projects", "Skills", "Contact"],
            icons=["house-fill", "code-slash", "bar-chart-fill", "envelope-fill"],
            default_index=0,
            styles={
                "container":          {"padding": "0", "background": "transparent"},
                "icon":               {"color": "#4f9cf9", "font-size": "1rem"},
                "nav-link":           {"font-size": ".9rem", "color": "#94a3b8",
                                       "padding": ".65rem 1rem", "margin": "2px 0"},
                "nav-link-selected":  {"background": "rgba(79,156,249,.15)",
                                       "color": "#4f9cf9", "font-weight": "600"},
            },
        )
        st.markdown("<div class='divider'></div>", unsafe_allow_html=True)
        st.markdown("""
        <div style='padding: 0 .5rem; font-size:.78rem; color:#475569; line-height:1.8;'>
            <div>📧 muhammadahmedali607@gmail.com</div>
            <div style='margin-top:.4rem;'>🌐 Available for freelance</div>
        </div>
        """, unsafe_allow_html=True)

except ImportError:
    st.sidebar.markdown("### Navigation")
    page = st.sidebar.radio("", ["Home", "Projects", "Skills", "Contact"])


# ╔══════════════════════════════════════════════════════════╗
# ║  PAGE: HOME                                              ║
# ╚══════════════════════════════════════════════════════════╝
if page == "Home":

    # ── Hero ────────────────────────────────────────────────
    st.markdown("""
    <div class="hero-wrapper">
        <span class="badge-pill">✦ Open to Opportunities</span>
        <h1 class="hero-name">Muhammad<br>Ahmed Ali</h1>
        <p class="hero-title">Python Developer &nbsp;·&nbsp; Automation &amp; Inventory Systems Expert</p>
        <p class="hero-bio">
            I build robust, high-performance Python applications that solve real-world business
            problems — from end-to-end inventory management systems to portable, compiler-free
            desktop tools. Passionate about clean architecture, smart automation, and elegant UX.
        </p>
        <div class="btn-row">
            <a class="btn-social btn-github"
               href="https://github.com/ahmar26" target="_blank">
               🐙 &nbsp;GitHub
            </a>
            <a class="btn-social btn-linkedin"
               href="https://www.linkedin.com/in/muhammad-ahmed-ali-123125406" target="_blank">
               💼 &nbsp;LinkedIn
            </a>
            <a class="btn-social btn-email"
               href="mailto:muhammadahmedali607@gmail.com">
               ✉️ &nbsp;Email Me
            </a>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # ── Stats row ───────────────────────────────────────────
    c1, c2, c3, c4 = st.columns(4)
    stats = [
        ("2+",  "Years Experience"),
        ("10+", "Projects Shipped"),
        ("4",   "Core Skill Domains"),
        ("∞",   "Lines of Python"),
    ]
    for col, (num, label) in zip([c1, c2, c3, c4], stats):
        with col:
            st.markdown(f"""
            <div class="stat-card">
                <div class="stat-num">{num}</div>
                <div class="stat-label">{label}</div>
            </div>
            """, unsafe_allow_html=True)

    st.markdown("<div class='divider'></div>", unsafe_allow_html=True)

    # ── About snapshot ──────────────────────────────────────
    st.markdown("""
    <p class="section-label">About Me</p>
    <h2 class="section-title">Turning Ideas Into<br>Reliable Software</h2>
    """, unsafe_allow_html=True)

    col_a, col_b = st.columns([3, 2], gap="large")
    with col_a:
        st.markdown("""
        <div style='color:#94a3b8; line-height:1.85; font-size:.97rem;'>
            I'm a Python developer with hands-on experience building automation pipelines,
            inventory tracking systems, and portable desktop applications. My work spans the
            full lifecycle — from architecture and data modelling to packaging and deployment.
        </div>
        <br>
        <div style='color:#94a3b8; line-height:1.85; font-size:.97rem;'>
            I believe great software is invisible: it does exactly what the user needs,
            stays out of the way, and never breaks. Whether it's a
            <span style='color:#4f9cf9;'>shop management suite</span> or a
            <span style='color:#a78bfa;'>zero-install executable</span>,
            I obsess over reliability and user experience.
        </div>
        """, unsafe_allow_html=True)

    with col_b:
        highlights = [
            ("🐍", "Python", "Expert"),
            ("⚙️", "Automation", "Advanced"),
            ("📦", "PyInstaller / Packaging", "Advanced"),
            ("📊", "Inventory Systems", "Expert"),
        ]
        for icon, skill, level in highlights:
            st.markdown(f"""
            <div style='display:flex; align-items:center; gap:12px;
                        background:var(--glass); border:1px solid var(--border);
                        border-radius:10px; padding:12px 16px; margin-bottom:10px;'>
                <span style='font-size:1.4rem;'>{icon}</span>
                <div>
                    <div style='font-weight:500; font-size:.9rem;'>{skill}</div>
                    <div style='font-size:.75rem; color:var(--accent);'>{level}</div>
                </div>
            </div>
            """, unsafe_allow_html=True)


# ╔══════════════════════════════════════════════════════════╗
# ║  PAGE: PROJECTS                                          ║
# ╚══════════════════════════════════════════════════════════╝
elif page == "Projects":
    st.markdown("""
    <p class="section-label">Portfolio</p>
    <h2 class="section-title">Featured Projects</h2>
    """, unsafe_allow_html=True)

    projects = [
        {
            "icon": "🏪",
            "title": "Mobile Phone Inventory System",
            "desc": (
                "A full-featured shop management system built in Python. Tracks product stock, "
                "records every sale & purchase, computes daily/monthly profit-and-loss reports, "
                "and manages supplier expenses — all from a clean, intuitive interface. "
                "Designed for real mobile-phone retail environments."
            ),
            "tags": [
                ("Python",            ""),
                ("SQLite",            "purple"),
                ("Tkinter / PyQt",    ""),
                ("Inventory Mgmt",    "green"),
                ("Reporting",         "purple"),
            ],
            "link": "https://github.com/ahmar26",
            "link_label": "View on GitHub →",
            "accent": "#4f9cf9",
        },
        {
            "icon": "📦",
            "title": "Direct Executable Mobile Shop App",
            "desc": (
                "A portable, single-file Python application that runs on any Windows machine "
                "without requiring a Python installation or compiler. Built using PyInstaller, "
                "it bundles all dependencies into one self-contained executable — ideal for "
                "shop owners who need instant deployment with zero setup friction."
            ),
            "tags": [
                ("PyInstaller",       ""),
                ("Python",            ""),
                ("Portable App",      "green"),
                ("Zero-Install",      "purple"),
                ("Windows",           ""),
            ],
            "link": "https://github.com/ahmar26",
            "link_label": "View on GitHub →",
            "accent": "#a78bfa",
        },
    ]

    col1, col2 = st.columns(2, gap="large")
    for col, proj in zip([col1, col2], projects):
        with col:
            tags_html = "".join(
                f'<span class="tag {"tag-"+c if c else ""}">{t}</span>'
                for t, c in proj["tags"]
            )
            st.markdown(f"""
            <div class="card">
                <span class="card-icon">{proj['icon']}</span>
                <div class="card-title">{proj['title']}</div>
                <div class="card-desc">{proj['desc']}</div>
                <div>{tags_html}</div>
                <a class="card-link" href="{proj['link']}" target="_blank">
                    {proj['link_label']}
                </a>
            </div>
            """, unsafe_allow_html=True)

    st.markdown("<div class='divider'></div>", unsafe_allow_html=True)

    # ── More projects teaser ─────────────────────────────────
    st.markdown("""
    <div style='text-align:center; padding:1.5rem;
                background:var(--glass); border:1px solid var(--border);
                border-radius:var(--radius);'>
        <div style='font-size:1.6rem; margin-bottom:.6rem;'>🚀</div>
        <div style='font-family:Syne,sans-serif; font-weight:700; font-size:1.1rem;
                    margin-bottom:.5rem;'>More Projects on GitHub</div>
        <div style='color:#64748b; font-size:.9rem; margin-bottom:1rem;'>
            Explore the full repository for automation scripts,
            utilities, and experiments.
        </div>
        <a href="https://github.com/ahmar26" target="_blank"
           style='color:#4f9cf9; font-size:.9rem; font-weight:500;
                  text-decoration:none;'>
            github.com/ahmar26 →
        </a>
    </div>
    """, unsafe_allow_html=True)


# ╔══════════════════════════════════════════════════════════╗
# ║  PAGE: SKILLS                                            ║
# ╚══════════════════════════════════════════════════════════╝
elif page == "Skills":
    st.markdown("""
    <p class="section-label">Expertise</p>
    <h2 class="section-title">Skills &amp; Technologies</h2>
    """, unsafe_allow_html=True)

    left, right = st.columns(2, gap="large")

    # ── Progress bars (left) ─────────────────────────────────
    with left:
        st.markdown("<h4 style='font-family:Syne,sans-serif; margin-bottom:1.4rem;'>Core Competencies</h4>",
                    unsafe_allow_html=True)
        skills = [
            ("Python Programming",      95),
            ("Inventory System Design", 90),
            ("Desktop App Development", 85),
            ("Automation & Scripting",  88),
            ("Database (SQLite/SQL)",   80),
            ("Executable Packaging",    85),
            ("UI/UX (Tkinter/PyQt)",    75),
            ("Data Analysis (Pandas)",  72),
        ]
        for name, pct in skills:
            st.markdown(f"""
            <div class="skill-row">
                <div class="skill-header">
                    <span class="skill-name">{name}</span>
                    <span class="skill-pct">{pct}%</span>
                </div>
                <div class="progress-track">
                    <div class="progress-fill" style="width:{pct}%"></div>
                </div>
            </div>
            """, unsafe_allow_html=True)

    # ── Badges (right) ───────────────────────────────────────
    with right:
        st.markdown("<h4 style='font-family:Syne,sans-serif; margin-bottom:1.4rem;'>Tools &amp; Technologies</h4>",
                    unsafe_allow_html=True)

        categories = {
            "🐍  Languages": [
                ("Python 3.x", ""), ("SQL", "purple"), ("Bash/Shell", "green"),
            ],
            "🛠️  Libraries & Frameworks": [
                ("Pandas", ""), ("NumPy", "purple"), ("Tkinter", "green"),
                ("PyQt5", ""), ("Streamlit", "purple"), ("Openpyxl", "green"),
            ],
            "📦  Packaging & Deployment": [
                ("PyInstaller", ""), ("cx_Freeze", "purple"), ("NSIS", "green"),
                ("Virtual Env", ""),
            ],
            "🗄️  Databases & Storage": [
                ("SQLite", ""), ("MySQL", "purple"), ("CSV / Excel", "green"),
            ],
            "⚙️  Dev Tools": [
                ("Git & GitHub", ""), ("VS Code", "purple"),
                ("PyCharm", "green"), ("Windows OS", ""),
            ],
        }

        for cat, badges in categories.items():
            st.markdown(f"""
            <div style='margin-bottom:1.4rem;'>
                <div style='font-size:.78rem; letter-spacing:.1em; text-transform:uppercase;
                            color:#64748b; margin-bottom:.6rem; font-weight:600;'>{cat}</div>
                <div>
                {"".join(f'<span class="tag {"tag-"+c if c else ""}" style="margin:3px;">{b}</span>' for b, c in badges)}
                </div>
            </div>
            """, unsafe_allow_html=True)

    st.markdown("<div class='divider'></div>", unsafe_allow_html=True)

    # ── Certifications / learning snapshot ───────────────────
    st.markdown("<h4 style='font-family:Syne,sans-serif; margin-bottom:1.2rem;'>Continuous Learning</h4>",
                unsafe_allow_html=True)
    c1, c2, c3 = st.columns(3)
    certs = [
        ("📜", "Python for Everybody", "Self-Directed", "#4f9cf9"),
        ("🏆", "Automation with Python", "Project-Based", "#a78bfa"),
        ("🎯", "Desktop GUI Development", "Hands-On", "#34d399"),
    ]
    for col, (icon, title, source, color) in zip([c1, c2, c3], certs):
        with col:
            st.markdown(f"""
            <div style='background:var(--glass); border:1px solid var(--border);
                        border-radius:var(--radius-sm); padding:1.2rem; text-align:center;'>
                <div style='font-size:2rem; margin-bottom:.5rem;'>{icon}</div>
                <div style='font-weight:600; font-size:.9rem; margin-bottom:.3rem;
                            font-family:Syne,sans-serif;'>{title}</div>
                <div style='font-size:.78rem; color:{color};'>{source}</div>
            </div>
            """, unsafe_allow_html=True)


# ╔══════════════════════════════════════════════════════════╗
# ║  PAGE: CONTACT                                           ║
# ╚══════════════════════════════════════════════════════════╝
elif page == "Contact":
    st.markdown("""
    <p class="section-label">Get In Touch</p>
    <h2 class="section-title">Let's Work Together</h2>
    """, unsafe_allow_html=True)

    form_col, info_col = st.columns([3, 2], gap="large")

    # ── Contact form ─────────────────────────────────────────
    with form_col:
        st.markdown('<div class="contact-card">', unsafe_allow_html=True)
        st.markdown("<h4 style='font-family:Syne,sans-serif; margin-bottom:1.2rem;'>Send a Message</h4>",
                    unsafe_allow_html=True)

        c1, c2 = st.columns(2)
        with c1:
            name = st.text_input("Your Name", placeholder="Jane Smith")
        with c2:
            email = st.text_input("Your Email", placeholder="jane@example.com")

        subject = st.text_input("Subject", placeholder="Project inquiry / Collaboration")
        message = st.text_area("Message", placeholder="Tell me about your project...",
                               height=150)

        if st.button("⚡  Send Message"):
            if name and email and message:
                st.success(f"✅ Message received, {name.split()[0]}! I'll reply within 24 hours.")
            else:
                st.warning("⚠️ Please fill in Name, Email, and Message.")

        st.markdown('</div>', unsafe_allow_html=True)

    # ── Contact info ─────────────────────────────────────────
    with info_col:
        contacts = [
            ("📧", "Email",    "muhammadahmedali607@gmail.com",
             "mailto:muhammadahmedali607@gmail.com", "#34d399"),
            ("🐙", "GitHub",   "github.com/ahmar26",
             "https://github.com/ahmar26", "#e2e8f0"),
            ("💼", "LinkedIn", "muhammad-ahmed-ali",
             "https://www.linkedin.com/in/muhammad-ahmed-ali-123125406", "#60a5fa"),
        ]
        for icon, label, display, href, color in contacts:
            st.markdown(f"""
            <a href="{href}" target="_blank" style="text-decoration:none; display:block; margin-bottom:12px;">
                <div style='background:var(--glass); border:1px solid var(--border);
                            border-radius:var(--radius-sm); padding:1rem 1.2rem;
                            display:flex; align-items:center; gap:14px;
                            transition:border-color .3s;'>
                    <span style='font-size:1.6rem;'>{icon}</span>
                    <div>
                        <div style='font-size:.75rem; color:#64748b; text-transform:uppercase;
                                    letter-spacing:.08em; margin-bottom:3px;'>{label}</div>
                        <div style='font-weight:500; font-size:.9rem; color:{color};'>{display}</div>
                    </div>
                </div>
            </a>
            """, unsafe_allow_html=True)

        st.markdown("""
        <div style='background:linear-gradient(135deg,rgba(79,156,249,.1),rgba(167,139,250,.1));
                    border:1px solid rgba(79,156,249,.2); border-radius:var(--radius-sm);
                    padding:1.2rem; margin-top:1rem; text-align:center;'>
            <div style='font-size:1.4rem; margin-bottom:.4rem;'>⏰</div>
            <div style='font-size:.85rem; font-weight:600; margin-bottom:.3rem;'>Response Time</div>
            <div style='font-size:.8rem; color:#64748b;'>Usually within 24 hours</div>
        </div>
        """, unsafe_allow_html=True)


# ── Footer (all pages) ───────────────────────────────────────
st.markdown("""
<div class="footer">
    Crafted with ❤️ &amp; Python by
    <span style='color:#4f9cf9; font-weight:600;'>Muhammad Ahmed Ali</span>
    &nbsp;·&nbsp; 2025
    &nbsp;·&nbsp;
    <a href="https://github.com/ahmar26" target="_blank"
       style='color:#64748b; text-decoration:none;'>GitHub</a>
    &nbsp;·&nbsp;
    <a href="https://www.linkedin.com/in/muhammad-ahmed-ali-123125406" target="_blank"
       style='color:#64748b; text-decoration:none;'>LinkedIn</a>
</div>
""", unsafe_allow_html=True)
