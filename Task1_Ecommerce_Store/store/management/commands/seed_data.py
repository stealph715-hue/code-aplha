"""
Quick script to populate the DB with a few sample categories and products
so the store isn't empty when you first run it.

Usage: python manage.py seed_data
"""
from django.core.management.base import BaseCommand
from store.models import Category, Product


class Command(BaseCommand):
    help = 'Seeds the database with sample categories and products'

    def handle(self, *args, **options):
        categories = {
            'electronics': 'Electronics',
            'clothing': 'Clothing',
            'books': 'Books',
        }

        cat_objs = {}
        for slug, name in categories.items():
            cat, _ = Category.objects.get_or_create(slug=slug, defaults={'name': name})
            cat_objs[slug] = cat

        products = [
            ('Wireless Headphones', 'electronics', 1999.00, 15, 'Over-ear headphones with noise cancellation.'),
            ('Smartwatch', 'electronics', 3499.00, 8, 'Fitness tracking smartwatch with heart rate monitor.'),
            ('Cotton T-Shirt', 'clothing', 499.00, 40, 'Comfortable everyday cotton t-shirt.'),
            ('Denim Jacket', 'clothing', 1799.00, 12, 'Classic blue denim jacket.'),
            ('Python Crash Course', 'books', 899.00, 20, 'A beginner-friendly guide to Python programming.'),
            ('The Pragmatic Programmer', 'books', 1099.00, 0, 'Classic book on software craftsmanship.'),
        ]

        for name, cat_slug, price, stock, desc in products:
            slug = name.lower().replace(' ', '-')
            Product.objects.get_or_create(
                slug=slug,
                defaults={
                    'name': name,
                    'category': cat_objs[cat_slug],
                    'price': price,
                    'stock': stock,
                    'description': desc,
                }
            )

        self.stdout.write(self.style.SUCCESS('Sample data added successfully.'))
