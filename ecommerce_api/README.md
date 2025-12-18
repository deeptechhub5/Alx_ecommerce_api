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
