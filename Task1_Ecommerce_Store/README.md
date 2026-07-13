# CodeAlpha_Ecommerce_Store

A simple full-stack e-commerce store built with Django, HTML, CSS and vanilla JS.
Made for the CodeAlpha Full Stack Development internship (Task 1).

## Features
- Product listing with category filter and search
- Product detail page
- User registration and login
- Shopping cart (add/update/remove items)
- Checkout with order placement
- Order history for logged-in users
- Django admin for managing products, categories and orders

## Tech stack
- Backend: Django 4.2 (Python)
- Frontend: HTML, CSS, JavaScript (server-rendered templates)
- Database: SQLite (default, easy to swap for Postgres/MySQL)

## Setup

1. Create a virtual environment and install dependencies:
   ```
   python -m venv venv
   source venv/bin/activate   # venv\Scripts\activate on Windows
   pip install -r requirements.txt
   ```

2. Run migrations:
   ```
   python manage.py makemigrations
   python manage.py migrate
   ```

3. Create an admin account:
   ```
   python manage.py createsuperuser
   ```

4. (Optional) Load some sample products:
   ```
   python manage.py seed_data
   ```

5. Run the server:
   ```
   python manage.py runserver
   ```

Visit http://127.0.0.1:8000/ to see the store, and /admin/ to manage products.

## Project structure
```
CodeAlpha_Ecommerce_Store/
├── ecommerce/          # project settings, urls
├── store/              # main app: models, views, templates, static
├── templates/           # base template
├── manage.py
└── requirements.txt
```

## Notes
- Carts are tied to logged-in users (no guest checkout for now).
- Stock is reduced automatically when an order is placed.
- This was built as part of a learning project, so some things are kept
  simple on purpose (e.g. no payment gateway integration - order placement
  just records the order).
