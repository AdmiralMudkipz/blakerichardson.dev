# blakerichardson.dev

Personal portfolio and campaign website built with Django, HTMX, and Tailwind CSS.

**Live at:** [portfolio.blakerichardson.dev](https://portfolio.blakerichardson.dev) · [campaign.blakerichardson.dev](https://campaign.blakerichardson.dev)

## Features

- **Portfolio site** — Project showcases with detail pages, skill-based filtering, work experience, responsive design, and smooth scroll animations
- **Campaign site** — Policy platform pages with a shared base template
- **Subdomain routing** — Django view routes requests to the correct app based on the subdomain
- **HTMX** — Dynamic UI interactions without heavy JavaScript frameworks
- **Tailwind CSS** — Utility-first styling loaded via CDN

## Tech Stack

- Python / Django
- HTMX
- Tailwind CSS (CDN)
- SQLite
- Deployed on a Linux server

## Setup

1. **Clone this repository:**
   ```bash
   git clone https://github.com/AdmiralMudkipz/blakerichardson.dev.git
   cd blakerichardson.dev
   ```

2. **Create and activate a virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate        # Mac/Linux
   venv/Scripts/activate            # Windows (git-bash)
   ```

3. **Install dependencies:**
   ```bash
   pip install django
   ```

4. **Run migrations:**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Run the development server:**
   ```bash
   python manage.py runserver
   ```

6. **Visit:**
   - Portfolio: [http://localhost:8000/portfolio/homepage/](http://localhost:8000/portfolio/homepage/)
   - Campaign: [http://localhost:8000/campaign/homepage/](http://localhost:8000/campaign/homepage/)
