# Portfolio

A minimal, single-page AI/ML portfolio built with Streamlit.

## Run it locally

```bash
pip install -r requirements.txt
streamlit run app.py
```

## Before you deploy — edit these

1. **`app.py`** — top of the file, marked `EDIT THIS SECTION WITH YOUR OWN INFO`:
   - `EMAIL` — your real contact email
   - `LOCATION` — your city, or "Remote"
   - `RESUME_PATH` — make sure `assets/resume.pdf` exists (see below)
   - `EDUCATION` — confirm the internship entry (dates/company)

2. **`assets/resume.pdf`** — add your resume PDF here. The Download Resume button
   links to `assets/resume.pdf`.

3. **`data/projects.json`** — add, remove, or edit project cards. Each entry supports:
   - `title`, `description`, `tech` (list), `metric` (optional badge), `github`, `demo` (optional)

## Deploy

Push this folder to a GitHub repo and deploy for free on
[Streamlit Community Cloud](https://streamlit.io/cloud) — point it at `app.py`.

## Structure

```
portfolio/
├── app.py              # main app
├── style.css            # all styling
├── requirements.txt
├── data/
│   └── projects.json    # project content, edit freely
└── assets/
    └── resume.pdf        # add your resume here
```
"# Portfolio" 
