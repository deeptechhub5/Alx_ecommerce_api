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
