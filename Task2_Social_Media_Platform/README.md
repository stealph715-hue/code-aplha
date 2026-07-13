# CodeAlpha_Social_Media_Platform

A mini social media app built with Django, HTML, CSS and vanilla JS.
Made for the CodeAlpha Full Stack Development internship (Task 2).

## Features
- User registration and login (with auto-created profile)
- Create posts (text + optional image)
- Like / unlike posts
- Comment on posts
- Follow / unfollow other users
- Personalized feed (posts from people you follow)
- Explore page (discover other users' posts)
- Editable profile with bio and avatar

## Tech stack
- Backend: Django 4.2 (Python)
- Frontend: HTML, CSS, JavaScript (server-rendered templates)
- Database: SQLite

## Setup

1. Create a virtual environment and install dependencies:
   ```
   python -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

2. Run migrations:
   ```
   python manage.py makemigrations
   python manage.py migrate
   ```

3. Create a superuser:
   ```
   python manage.py createsuperuser
   ```

4. Run the server:
   ```
   python manage.py runserver
   ```

Visit http://127.0.0.1:8000/ - you'll be redirected to login/register first.

## Project structure
```
CodeAlpha_Social_Media_Platform/
├── socialapp/       # project settings, urls
├── social/          # main app: models, views, templates, static, signals
├── templates/        # base template
├── manage.py
└── requirements.txt
```

## Notes
- A Profile is auto-created for every new User via a signal (see social/signals.py).
- The feed only shows posts from users you follow (plus your own) - go to
  Explore to find people to follow first.
- Kept the feature set close to the brief: profiles, posts, comments, likes,
  follows. No DMs or notifications for this task.
