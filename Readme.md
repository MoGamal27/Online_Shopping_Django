# Online Shopping Django Application

This is an online shopping application built with Django, providing functionalities for managing products, orders, and users.

## Features

- User authentication and management
- Product listing and details
- Order creation and management
- Filtering and searching for products
- Caching for improved performance


## API Endpoints

- **Products**
  - `GET /products/` - List all products
  - `POST /products/` - Create a new product
  - `GET /products/info/` - Get product information (count, max price)
  - `GET /products/<int:product_id>/` - Retrieve, update, or delete a product by ID

- **Users**
  - `GET /users/` - List all users
  - `POST /users/` - Create a new user (requires authentication)
  - `GET /users/<int:user_id>/` - Retrieve, update, or delete a user by ID (requires authentication)
  - `POST /api/token/` - Obtain a new access and refresh token
  - `POST /api/token/refresh/` - Refresh the access token using the refresh token

- **Orders**
  - `GET /orders/` - List all orders
  - `POST /orders/` - Create a new order
  - `GET /orders/<int:order_id>/` - Retrieve, update, or delete an order by ID


