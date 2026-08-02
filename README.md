# Mrinmoy Talukder — Data Scientist Portfolio

A minimal, single-page data science portfolio built entirely with Streamlit and custom CSS.

**🔗 Live app:** [mrinmoy-portfolio.streamlit.app](https://mrinmoy-portfolio.streamlit.app/)

## About

This is my personal portfolio, built to showcase my work as a Data Scientist —
covering my background, technical skills, internship experience, and selected
data science / ML projects (including a fraud detection model at 94.63% accuracy
and a hybrid NLP-based product recommendation system). It includes a downloadable
resume and a direct way to get in touch.

## Tech Stack

- **Framework:** [Streamlit](https://streamlit.io/)
- **Styling:** Custom CSS (glassmorphism cards, dark theme, no component libraries)
- **Language:** Python 3
- **Deployment:** [Streamlit Community Cloud](https://streamlit.io/cloud)

## Sections

- **Hero** — name, role, short intro, and quick links (resume, GitHub, LinkedIn, contact)
- **About** — bio and education timeline
- **Skills** — core data science / ML toolkit
- **Experience** — internship history with role details, tech tags, and repo links
- **Projects** — selected end-to-end data science / ML projects
- **Contact** — direct email, socials, and a lightweight contact form

## Run it locally

\`\`\`bash
git clone https://github.com/MrinmoyTalukdar27/<this-repo>.git
cd <this-repo>
pip install -r requirements.txt
streamlit run app.py
\`\`\`

The app will open at `http://localhost:8501`.

## Project Structure

\`\`\`
portfolio/
├── app.py              # main app — layout, sections, and your info
├── style.css            # all styling (dark theme, cards, buttons)
├── requirements.txt
├── data/
│   └── projects.json    # project content — edit freely, no code changes needed
└── assets/
    └── resume.pdf        # downloadable resume
\`\`\`

## Customizing

- **Personal info** — edit the config block at the top of `app.py` (name, role,
  email, links, bio, education, skills, experience).
- **Projects** — add, remove, or edit entries in `data/projects.json`. Each entry
  supports: `title`, `description`, `tech` (list), `metric` (optional badge),
  `github`, `demo` (optional).
- **Resume** — replace `assets/resume.pdf` with your latest resume.
- **Styling** — all colors and layout live in `style.css` as CSS custom properties
  under `:root`.

## Deploy

Push this repo to GitHub and deploy for free on
[Streamlit Community Cloud](https://streamlit.io/cloud) — point it at `app.py`.