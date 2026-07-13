# CodeAlpha_Project_Management_Tool

A Trello/Asana-style project management tool built with Django, HTML, CSS
and vanilla JS. Made for the CodeAlpha Full Stack Development internship
(Task 3).

## Features
- User registration and login
- Create projects, add members by username
- Task board with To Do / In Progress / Done columns
- Create tasks, assign to project members, set due dates
- Move tasks between columns (updates instantly via a small fetch call)
- Comment on tasks
- In-app notifications (assigned to a task, added to a project, someone
  commented) with a polling-based "live" unread badge - see the Notes
  section below on the bonus real-time requirement

## Tech stack
- Backend: Django 4.2 (Python)
- Frontend: HTML, CSS, JavaScript (server-rendered templates + small
  fetch() calls for the status dropdown and notification badge)
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

Visit http://127.0.0.1:8000/ and register a couple of test accounts to
try out adding members and assigning tasks between them.

## Project structure
```
CodeAlpha_Project_Management_Tool/
├── pmtool/           # project settings, urls
├── projects/          # main app: models, views, templates, static
├── templates/          # base template
├── manage.py
└── requirements.txt
```

## Notes on the bonus (real-time updates)
The task brief mentions WebSockets as a bonus for real-time notifications.
I kept this app on plain Django (no Channels/ASGI server, no Redis) so it's
simple to set up and run anywhere. Instead, `notifications.js` polls a small
JSON endpoint every 15 seconds for the unread count, which gives a similar
live-update feel without the extra infrastructure. If you want true
WebSocket-based push notifications, the natural next step would be to add
`django-channels` with a Redis channel layer and swap the polling call in
`notifications.js` for a WebSocket connection - the models and notification
logic here (`_notify()` in views.py) would slot straight into that without
changes.
