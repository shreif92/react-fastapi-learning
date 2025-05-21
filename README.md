"# Product and Supplier Management API

A FastAPI-based REST API for managing products and suppliers with SQLite database backend.

## Features

- Product Management (CRUD operations)
  - Create new products with supplier information
  - List all products
  - Get product details
  - Update product information
  - Delete products
- Supplier Management (CRUD operations)
  - Create new suppliers
  - List all suppliers
  - Get supplier details
  - Update supplier information
  - Delete suppliers

## Technology Stack

- FastAPI
- SQLite
- Tortoise ORM
- Pydantic for data validation
- Uvicorn server

## Requirements

Python 3.11+ and the following packages:

```txt
fastapi
uvicorn
tortoise-orm
aiosqlite
pydantic
```

## Installation

1. Clone the repository
2. Create a virtual environment:
   ```bash
   python -m venv venv
   venv\Scripts\activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Running the Application

Start the server with:

```bash
uvicorn app:app --reload
```

The API will be available at `http://localhost:8000`

## API Documentation

Once the server is running, you can access:

- Interactive API documentation (Swagger UI): `http://localhost:8000/docs`
- Alternative API documentation (ReDoc): `http://localhost:8000/redoc`

### API Endpoints

#### Products

- `POST /product` - Create a new product
- `GET /products` - List all products
- `GET /product/{product_id}` - Get product details
- `PUT /update_product/{product_id}` - Update product
- `DELETE /delete_product/{product_id}` - Delete product

#### Suppliers

- `POST /supplier` - Create a new supplier
- `GET /suppliers` - List all suppliers
- `GET /supplier/{supplier_id}` - Get supplier details
- `PUT /update_supplier/{supplier_id}` - Update supplier
- `DELETE /delete_supplier/{supplier_id}` - Delete supplier

## Data Models

### Product

- id: Integer (Primary Key)
- name: String
- description: String (Optional)
- price: Decimal
- stock: Integer
- reveneue: Decimal
- created_at: DateTime
- updated_at: DateTime
- supplyed_by: Foreign Key (Supplier)

### Supplier

- id: Integer (Primary Key)
- name: String
- email: String
- phone_number: String
- address: Text
- created_at: DateTime
- updated_at: DateTime"
