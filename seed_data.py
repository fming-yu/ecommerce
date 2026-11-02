"""
Sample Database Seeder Script for CSC 413 E-Commerce Store
Run after migrations: python seed_data.py
"""
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myshop.settings')
django.setup()

from shop.models import Category, Product

def seed():
    print("Seeding database with sample e-commerce data...")
    
    cat_elec, _ = Category.objects.get_or_create(name="Electronics", slug="electronics")
    cat_books, _ = Category.objects.get_or_create(name="Books", slug="books")
    cat_app, _ = Category.objects.get_or_create(name="Apparel", slug="apparel")

    products = [
        {"category": cat_elec, "name": "Wireless Noise-Canceling Headphones", "slug": "wireless-headphones", "price": 149.99, "description": "High-quality wireless audio with active noise cancellation."},
        {"category": cat_elec, "name": "Mechanical Gaming Keyboard", "slug": "mechanical-keyboard", "price": 89.50, "description": "Tactile RGB mechanical switches with customizable backlighting."},
        {"category": cat_elec, "name": "USB-C Multi-Port Adapter Hub", "slug": "usbc-adapter-hub", "price": 29.99, "description": "7-in-1 hub featuring HDMI, USB 3.0, and SD card readers."},
        {"category": cat_books, "name": "Django for Beginners (5th Edition)", "slug": "django-for-beginners", "price": 39.99, "description": "Build web applications from scratch with Python and Django."},
        {"category": cat_books, "name": "Django 5 by Example", "slug": "django-5-by-example", "price": 49.99, "description": "Build powerful real-world web applications with modern Django."},
        {"category": cat_app, "name": "CSC 413 Application Dev T-Shirt", "slug": "csc413-tshirt", "price": 19.99, "description": "100% cotton developer tee featuring the Python logo."},
    ]

    for pdata in products:
        p, created = Product.objects.get_or_create(
            slug=pdata["slug"],
            defaults=pdata
        )
        if created:
            print(f"Created Product: {p.name}")
        else:
            print(f"Product already exists: {p.name}")

    print("\nSeeding complete! Start the server with: python manage.py runserver")

if __name__ == "__main__":
    seed()
