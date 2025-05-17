# Flask Blog Application

A lightweight, container-ready blog application built with Flask. This project supports user profiles, blog posts, and comments, rendered with HTML templates and styled with a custom CSS layout. It is preconfigured with demo content and can be run locally or inside a Docker container.

## Features

- User registration (pre-populated with sample users)
- Blog post creation with metadata (title, content, timestamp)
- Comments associated with specific users and posts
- Page views tracking for individual blog posts
- Dynamic pages: user profiles, all users, post details, all posts
- Pre-loaded SQLite database for demonstration and development

## Technology Stack

- Python 3.9+
- Flask with Jinja2 templates and SQLAlchemy ORM
- SQLite for data persistence
- HTML/CSS for front-end rendering
- Docker support for containerized deployment

## Getting Started

### Clone the Repository

```
git clone https://github.com/yourusername/dragosh29-flask_blog_app.git
cd dragosh29-flask_blog_app
```

### Run Locally

Install dependencies:

```
pip install -r requirements.txt
```

Create and populate the database:

```
python db_creator.py
```

Start the application:

```
python run.py
```

Access it at `http://localhost:5000`

### Run with Docker

This project includes a Dockerfile for simplified deployment in containerized environments.

> **Note:** This deployment uses Flask’s built-in development server and is suitable for demonstration, testing, or lightweight production use. For full production deployments, integration with Gunicorn or uWSGI is recommended.

Ensure Docker is installed and run:

```
docker build -t flask-blog-app .
docker run -p 5000:5000 flask-blog-app
```

## Directory Overview

- `app/` — Flask application (routes, models, templates, static files)
- `templates/` — HTML templates for dynamic pages
- `static/style.css` — Base styling for UI
- `db_creator.py` — Initializes and seeds the SQLite database
- `Dockerfile` — Container setup for demonstration or lightweight production deployment

## License

This project is licensed under the MIT License.
