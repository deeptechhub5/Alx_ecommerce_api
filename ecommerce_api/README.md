# E-commerce Product API (Week 1)

## What this contains (Week 1)
- Django project scaffold
- accounts app: user registration
- products app: Product and Category models
- Product CRUD endpoints
- JWT authentication (Simple JWT) setup

## Quickstart (local)
1. python -m venv env
2. source env/bin/activate   # or env\\Scripts\\activate on Windows
3. pip install -r requirements.txt
4. python manage.py migrate
5. python manage.py runserver

## Endpoints
- POST /api/auth/register/       -> register new user
- POST /api/token/               -> obtain access & refresh tokens
- GET  /api/products/            -> list products
- POST /api/products/            -> create product (auth required)
- GET  /api/products/<id>/       -> retrieve product
- PUT  /api/products/<id>/       -> update product (auth required)
- DELETE /api/products/<id>/    -> delete product (auth required)

Week 2: Advanced Product Features (Ecommerce API)
Overview

In Week 2, the Ecommerce API was expanded with advanced product features to support a real-world online store. This week introduces category management, product improvements, and clean REST API endpoints with serializers and views.

📌 Features Implemented This Week
1. Category Management

Users (or admin) can now:

Create product categories

List all categories

Retrieve a single category

Update & delete categories

Endpoints added:

GET    /api/categories/
POST   /api/categories/
GET    /api/categories/<id>/
PUT    /api/categories/<id>/
DELETE /api/categories/<id>/

2. Advanced Product Model

The product model now includes:

Category relationship

Image URL

Automatic timestamps

Improved structure for ecommerce use

Fields:

name, description, price, stock, image_url, category, created_at, updated_at

3. Improved Serializers

The ProductSerializer now returns nested category data and supports writing via category_id.

Example JSON output:

{
  "id": 3,
  "name": "Laptop",
  "price": "2500.00",
  "stock": 10,
  "category": {
    "id": 1,
    "name": "Electronics"
  },
  "image_url": "https://example.com/img.jpg"
}

4. REST API Views & CRUD Endpoints

The following API endpoints were implemented:

Products
GET    /api/products/
POST   /api/products/
GET    /api/products/<id>/
PUT    /api/products/<id>/
DELETE /api/products/<id>/

Categories
GET    /api/categories/
POST   /api/categories/
GET    /api/categories/<id>/
PUT    /api/categories/<id>/
DELETE /api/categories/<id>/

### Week 3 – Extended Ecommerce Features

In this phase, the API was extended to include core ecommerce user interactions inspired by real-world platforms.

#### Added Features
- Wishlist system allowing users to save products
- Cart system with product quantities
- Secure access using JWT authentication
- Clean separation of concerns using an `orders` app

#### Key Endpoints
- `/api/wishlist/`
- `/api/cart/`
- `/api/cart/add/`
- `/api/cart/remove/{product_id}/`

These features bring the API closer to production-ready ecommerce functionality.

Deployment

This project is deployed using PythonAnywhere, a free cloud hosting platform suitable for Django applications. The deployment process involves configuring a virtual environment, installing dependencies, setting environment variables, running database migrations, collecting static files, and configuring the WSGI application.

Live URL
https://fiifidrillz.pythonanywhere.com/


Note: This is an API-only backend. Access specific endpoints such as /admin/ or /api/products/ to interact with the application.

Deployment Platform

Hosting Provider: PythonAnywhere

Python Version: 3.10

Framework: Django + Django REST Framework

Database: SQLite (development/early production)

Deployment Steps
1. Clone the Repository
git clone https://github.com/deeptechhub5/Alx_ecommerce_api.git
cd Alx_ecommerce_api/ecommerce_api

2. Create and Activate Virtual Environment
python3.10 -m venv venv
source venv/bin/activate

3. Install Dependencies
pip install -r requirements.txt

4. Environment Configuration

Update settings.py for production:

Set DEBUG = False

Add PythonAnywhere domain to ALLOWED_HOSTS

Configure STATIC_ROOT

DEBUG = False
ALLOWED_HOSTS = ["fiifidrillz.pythonanywhere.com"]
STATIC_ROOT = BASE_DIR / "staticfiles"

5. Apply Database Migrations
python manage.py makemigrations
python manage.py migrate

6. Collect Static Files
python manage.py collectstatic --noinput

7. Configure WSGI on PythonAnywhere

In the Web tab:

Set the source code path:

/home/fiifidrillz/Alx_ecommerce_api/ecommerce_api


Set the virtual environment path:

/home/fiifidrillz/Alx_ecommerce_api/ecommerce_api/venv


Use Django’s default wsgi.py file:

ecommerce_api/wsgi.py


Reload the web app after configuration.

Verifying Deployment

Visit the following URLs to confirm successful deployment:

Django Admin:

https://fiifidrillz.pythonanywhere.com/admin/


Products API:

https://fiifidrillz.pythonanywhere.com/api/products/


Categories API:

https://fiifidrillz.pythonanywhere.com/api/categories/

Continuous Updates

Changes made locally are pushed to GitHub and pulled into PythonAnywhere:

git pull


After pulling updates, reload the web app from the PythonAnywhere dashboard.

Known Limitations

SQLite is used for simplicity; PostgreSQL is recommended for large-scale production.

Image uploads are currently handled via URLs rather than file storage.