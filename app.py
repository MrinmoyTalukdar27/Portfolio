import json
from pathlib import Path

import streamlit as st

# ============================================================
# EDIT THIS SECTION WITH YOUR OWN INFO
# ============================================================
NAME = "Mrinmoy Talukder"  # NOTE: your resume spells it "Talukder"; GitHub/LinkedIn use "Talukdar" — pick one and I'll match it everywhere
ROLE_LINE = "Data Scientist"
LOCATION = "Guwahati, Assam, India"
EMAIL = "mrinmoytalukdergcu@gmail.com"
GITHUB_URL = "https://github.com/MrinmoyTalukdar27"
LINKEDIN_URL = "https://www.linkedin.com/in/mrinmoy-talukdar-5867ab3b9"
MEDIUM_URL = "https://medium.com/@mrinmoytalukdargcu"
RESUME_PATH = "assets/resume.pdf"
STATUS_TAG = "OPEN TO DATA SCIENCE ROLES"

BIO = (
    "Data Scientist with two internships and a strong foundation in statistical analysis, "
    "machine learning, and data-driven decision making. Designed and deployed a hybrid "
    "NLP-based recommendation system, and built a fraud detection model that reached "
    "94.63% accuracy on 6.3M+ records. Pursuing an M.Sc. in AI & Data Science and "
    "passionate about turning raw data into actionable business insights."
)

EDUCATION = [
    {"year": "2025", "title": "B.Sc, Information Technology", "detail": "Gauhati University (2023 — 2025)"},
    {"year": "2027", "title": "M.Sc, AI & Data Science", "detail": "Girijananda Chowdhury University (2025— in progress)"},
    {"year": "Now", "title": "Open to data science / ML internships", "detail": ""},
]

SKILLS = [
    "Python", "SQL","Machine learning ","Deep Learning", "Pandas", "NumPy", "Scikit-learn",
    "Matplotlib", "Seaborn", "Sentence Transformers", "NLP", "KNN",
    "Streamlit", "Git", "GitHub", "Jupyter Notebook", "HTML/CSS",
]

EXPERIENCE = [
    {
        "title": "Data Science Intern — AI/ML Summer Intern",
        "company": "XopunTech (India) Pvt. Ltd.",
        "type": "Internship",
        "duration": "July 2026 – Aug 2026",
        "tech": ["Python", "NumPy","Pandas","Matplotlib", "Seaborn","Scikit-learn","Sentence Transformers", "KNN", "Streamlit"],
        "github": "https://github.com/MrinmoyTalukdar27/xopuntech_Internship",
        "points": [
            "Designed and deployed a hybrid Amazon product recommendation system using NLP and ML to deliver personalized suggestions based on semantic and numerical feature similarity.",
            "Applied Sentence Transformers for semantic embeddings and engineered hybrid feature vectors combining text embeddings with scaled numerical attributes (ratings, price, discount).",
            "Implemented KNN with cosine similarity for fast recommendations; deployed a production-ready web app using Streamlit.",
            "Executed the full data science pipeline: EDA, feature engineering, model training, and deployment.",
        ],
    },
    {
        "title": "Data Analysis Intern",
        "company": "Cognifyz IT Solutions Pvt. Ltd. (ISO 9001:2015 Certified) · Intern ID: CTI/A1/C348555",
        "type": "Internship",
        "duration": "May 2026 – June 2026",
        "tech": ["Python", "Pandas", "Matplotlib", "EDA"],
        "github": "https://github.com/MrinmoyTalukdar27/Cognifyz-internship-project", 
        "points": [
            "Performed EDA and statistical analysis on a multi-country restaurant dataset to extract business insights.",
            "Discovered delivery-enabled restaurants scored 31.4% higher ratings on average; performed geospatial analysis via latitude/longitude clustering to support market-expansion recommendations.",
            "Delivered insights through clean, well-documented Jupyter Notebook workflows using Python, Pandas, and Matplotlib.",
        ],
    },
]
# ============================================================


def load_css(path: str):
    css_path = Path(__file__).parent / path
    st.markdown(f"<style>{css_path.read_text()}</style>", unsafe_allow_html=True)


def load_projects():
    data_path = Path(__file__).parent / "data" / "projects.json"
    return json.loads(data_path.read_text())


st.set_page_config(page_title=f"{NAME} — Portfolio", page_icon="◆", layout="wide")
load_css("style.css")
projects = load_projects()

# ---------------- Nav ----------------
st.markdown(
    f"""
    <div class="pf-nav">
      <div class="pf-nav-inner">
        <div class="pf-nav-links">
          <a href="#about">About</a>
          <a href="#skills">Skills</a>
          <a href="#experience">Experience</a>
          <a href="#projects">Projects</a>
          <a href="#contact">Contact</a>
        </div>
      </div>
    </div>
    """,
    unsafe_allow_html=True,
)

st.markdown('<div class="pf-wrap">', unsafe_allow_html=True)

# ---------------- Hero ----------------
st.markdown(
    f"""
    <div id="home" class="pf-hero">
      <div class="pf-hero-card">
        <div class="pf-status-tag"><span class="pf-status-dot"></span>{STATUS_TAG}</div>
        <div class="pf-eyebrow">{ROLE_LINE}</div>
        <h1>Turning data into<br>decisions.</h1>
        <p class="lead">{BIO}</p>
        <div class="pf-hero-links">
          <a class="pf-btn pf-btn-secondary" href="{RESUME_PATH}" target="_blank">Download Resume</a>
          <a class="pf-btn pf-btn-secondary" href="{GITHUB_URL}" target="_blank">GitHub</a>
          <a class="pf-btn pf-btn-secondary" href="{LINKEDIN_URL}" target="_blank">LinkedIn</a>
          <a class="pf-btn pf-btn-secondary" href="{MEDIUM_URL}" target="_blank">Medium</a>
          <a class="pf-btn pf-btn-secondary" href="#contact">Let's Talk</a>
        </div>
      </div>
    </div>
    """,
    unsafe_allow_html=True,
)

# ---------------- About ----------------
timeline_html = "".join(
    f"""
    <div class="pf-timeline-item">
      <div class="pf-timeline-year">{item['year']}</div>
      <div class="pf-timeline-content">
        <strong>{item['title']}</strong>
        <span>{item['detail']}</span>
      </div>
    </div>
    """
    for item in EDUCATION
)

st.markdown(
    f"""
    <div id="about" class="pf-section">
      <div class="pf-section-label">01 / About</div>
      <div class="pf-section-title">A little about me</div>
      <div class="pf-about-card">
        <p class="pf-body-text" style="margin-bottom: 28px;">{BIO}</p>
        {timeline_html}
      </div>
    </div>
    """,
    unsafe_allow_html=True,
)

# ---------------- Skills ----------------
skills_html = "".join(f'<span class="pf-skill-pill">{s}</span>' for s in SKILLS)
st.markdown(
    f"""
    <div id="skills" class="pf-section">
      <div class="pf-section-label">02 / Skills</div>
      <div class="pf-section-title">Data science toolkit</div>
      <div class="pf-skill-grid">{skills_html}</div>
    </div>
    """,
    unsafe_allow_html=True,
)

# ---------------- Experience ----------------
st.markdown(
    """
    <div id="experience" class="pf-section">
      <div class="pf-section-label">03 / Experience</div>
      <div class="pf-section-title">Where I've worked</div>
    </div>
    """,
    unsafe_allow_html=True,
)

for exp in EXPERIENCE:
    points_html = "".join(f"<li>{point}</li>" for point in exp["points"])
    exp_tags_html = "".join(f'<span class="pf-tag">{t}</span>' for t in exp.get("tech", []))
    exp_github_html = (
        f'<div class="pf-exp-links"><a href="{exp["github"]}" target="_blank">GitHub Repository →</a></div>'
        if exp.get("github") else ""
    )
    st.markdown(
        f"""
        <div class="pf-exp-card" style="margin-bottom: 16px;">
          <div class="pf-exp-head">
            <h3>{exp['title']}</h3>
            <span class="pf-exp-duration">{exp['duration']}</span>
          </div>
          <div class="pf-exp-company">
            {exp['company']}
            <span class="pf-exp-type">{exp.get('type', '')}</span>
          </div>
          <ul class="pf-exp-list">{points_html}</ul>
          <div class="pf-tags">{exp_tags_html}</div>
          {exp_github_html}
        </div>
        """,
        unsafe_allow_html=True,
    )

# ---------------- Projects ----------------
st.markdown(
    """
    <div id="projects" class="pf-section">
      <div class="pf-section-label">04 / Projects</div>
      <div class="pf-section-title">Selected work</div>
    </div>
    """,
    unsafe_allow_html=True,
)

for p in projects:
    tags_html = "".join(f'<span class="pf-tag">{t}</span>' for t in p["tech"])
    metric_html = f'<span class="pf-metric">{p["metric"]}</span>' if p.get("metric") else ""
    demo_html = f'<a href="{p["demo"]}" target="_blank">Live Demo →</a>' if p.get("demo") else ""
    st.markdown(
        f"""
        <div class="pf-card">
          <div class="pf-card-top">
            <h3>{p['title']}</h3>
            {metric_html}
          </div>
          <p>{p['description']}</p>
          <div class="pf-tags">{tags_html}</div>
          <div class="pf-card-links">
            <a href="{p['github']}" target="_blank">GitHub →</a>
            {demo_html}
          </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

# ---------------- Contact ----------------
st.markdown(
    f"""
    <div id="contact" class="pf-section">
      <div class="pf-section-label">05 / Contact</div>
      <div class="pf-section-title">Let's talk</div>
      <p class="pf-body-text">
        I'm actively looking for data science opportunities{f" — based in {LOCATION}" if LOCATION else ""}.
        Reach out directly, or send a quick note below.
      </p>
      <div class="pf-contact-row">
        <a href="mailto:{EMAIL}">✉ {EMAIL}</a>
        <a href="{GITHUB_URL}" target="_blank">GitHub</a>
        <a href="{LINKEDIN_URL}" target="_blank">LinkedIn</a>
        {f'<a href="{MEDIUM_URL}" target="_blank">Medium</a>' if MEDIUM_URL else ''}
      </div>

      <div class="pf-contact-form">
        <input id="cf-name" class="pf-input" type="text" placeholder="Name">
        <input id="cf-email" class="pf-input" type="email" placeholder="Email">
        <textarea id="cf-msg" class="pf-input pf-textarea" placeholder="Message" rows="4"></textarea>
        <button class="pf-btn pf-btn-primary" style="border:none; cursor:pointer;"
          onclick="
            var n=document.getElementById('cf-name').value || 'there';
            var e=document.getElementById('cf-email').value || '';
            var m=document.getElementById('cf-msg').value || '';
            var subject=encodeURIComponent('Portfolio contact from ' + n);
            var body=encodeURIComponent(m + '\\n\\nFrom: ' + n + ' (' + e + ')');
            window.location.href='mailto:{EMAIL}?subject=' + subject + '&body=' + body;
          ">
          Send Message
        </button>
      </div>
    </div>

    <div class="pf-footer">
      {EDUCATION[1]['title']} · {EDUCATION[1]['detail']}<br>
      © {NAME} · {LOCATION}
    </div>
    """,
    unsafe_allow_html=True,
)

st.markdown("</div>", unsafe_allow_html=True)
