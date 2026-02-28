# 🚀 Aman Varma — Professional Portfolio

[![Python](https://img.shields.io/badge/Python-3.11-3776AB?style=flat&logo=python&logoColor=white)](https://python.org)
[![Django](https://img.shields.io/badge/Django-5.0-092E20?style=flat&logo=django&logoColor=white)](https://djangoproject.com)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Deployed on Vercel](https://img.shields.io/badge/Deployed%20on-Vercel-black?style=flat&logo=vercel)](https://vercel.com)

> A professional portfolio website built with Django — **building high‑performance backends** and **scalable system architectures** with a focus on efficiency, reliability, and clean code. Features a glassmorphism dark UI, animated skill bars, project showcase, and a fully functional AJAX contact form with email notifications.

---

## ✨ Features

- 🎨 **Premium UI** — Dark glassmorphism design with smooth AOS animations and typewriter effect
- 📱 **Fully Responsive** — Mobile-first design using Bootstrap 5
- 💼 **Projects Showcase** — Dynamic project cards with tech stack badges
- 🛠️ **Skills Visualization** — Animated progress bars across Programming, Web & Infrastructure
- 📬 **Contact Form** — AJAX form with email notifications via Gmail SMTP
- 🌓 **Theme Toggle** — Persistent light/dark mode via localStorage
- 🔐 **Admin Panel** — Manage projects, experiences, and contact messages via Django Admin
- ⚡ **Whitenoise Static** — Compressed static files for fast delivery
- 📱 **Mobile App (PWA)** — Installable as a standalone app on Android/iOS/Desktop

---

## 🏗️ Project Structure

```
portfolio_project/
├── core/                    # Main Django app
│   ├── models.py            # Project, Experience, ContactMessage
│   ├── views.py             # All page views
│   ├── forms.py             # Contact & Project forms
│   ├── admin.py             # Admin panel configuration
│   └── urls.py              # App URL patterns
├── portfolio/               # Django project settings
│   ├── settings.py          # Configuration (env-based)
│   ├── urls.py              # Root URL configuration
│   └── wsgi.py              # WSGI entry point
├── Templates/               # HTML templates
│   ├── base.html            # Base layout (navbar, footer, scripts)
│   ├── home.html            # Hero + Skills + Projects + CTA
│   ├── about.html           # About + Education + Certifications
│   ├── projects.html        # Full project showcase
│   ├── experience.html      # Timeline work experience
│   ├── contact.html         # Contact form + social links
│   └── emails/              # Email notification templates
├── static/
│   ├── css/style.css        # Custom animations & utilities
│   ├── css/js/script.js     # Interactivity & form handling
│   └── images/              # Profile photo & assets
├── .env                     # Local environment variables (not in git)
├── .env.example             # Template for setting up .env
├── requirements.txt         # Python dependencies
├── Procfile                 # Heroku/Render deployment
├── vercel.json              # Vercel deployment config
└── runtime.txt              # Python version for deployment
```

---

## ⚙️ Local Setup

### Prerequisites
- Python 3.10+
- pip

### 1. Clone the repository
```bash
git clone https://github.com/Amanvarma2231/portfolio_project.git
cd portfolio_project
```

### 2. Create virtual environment
```bash
python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Configure environment variables
```bash
copy .env.example .env   # Windows
# cp .env.example .env   # macOS/Linux
```
Edit `.env` and fill in your values (see `.env.example` for guidance).

### 5. Run migrations
```bash
python manage.py migrate
```

### 6. Create superuser (for Admin panel)
```bash
python manage.py createsuperuser
```

### 7. Collect static files
```bash
python manage.py collectstatic --noinput
```

### 8. Start development server
```bash
python manage.py runserver
```

Visit: **http://127.0.0.1:8000**

---

## 📧 Email Setup (Gmail SMTP)

1. Enable **2-Step Verification** on your Google Account
2. Go to: **Google Account → Security → App Passwords**
3. Generate a new App Password for "Mail"
4. Set in `.env`:
   ```
   EMAIL_HOST_USER=your-email@gmail.com
   EMAIL_HOST_PASSWORD=your-16-char-app-password
   ```

---

## 🚀 Deployment

### Vercel (Recommended)
1. Push to GitHub
2. Import project on [vercel.com](https://vercel.com)
3. Add environment variables in Vercel dashboard (same as `.env` keys)
4. Set `DJANGO_DEBUG=False` in production

### Render / Railway
1. Connect your GitHub repo
2. Set build command: `pip install -r requirements.txt && python manage.py collectstatic --noinput`
3. Set start command: `gunicorn portfolio.wsgi:application`
4. Add all environment variables from `.env.example`

---

## 🛡️ Security Checklist (Production)

- [x] `DJANGO_DEBUG=False`
- [x] Strong `DJANGO_SECRET_KEY` (50+ chars random)
- [x] `ALLOWED_HOSTS` set to your actual domain
- [x] Security headers enabled (HSTS, XSS, CSRF)
- [x] `.env` not committed to git
- [x] Admin URL is `/admin/` (consider changing for extra security)

---

## 📞 Connect

| Platform | Link |
|----------|------|
| 🌐 Portfolio | [amanvarma.com](https://amanvarma.com) |
| 💼 LinkedIn | [linkedin.com/in/aman-v-697771345](https://www.linkedin.com/in/aman-v-697771345) |
| 🐙 GitHub | [github.com/Amanvarma2231](https://github.com/Amanvarma2231) |
| 📧 Email | [amangurauli@gmail.com](mailto:amangurauli@gmail.com) |

---

## 📄 License

This project is licensed under the **MIT License** — feel free to use it as a template for your own portfolio!

---

<p align="center">Made with ❤️ and Django by <strong>Aman Varma</strong></p>
