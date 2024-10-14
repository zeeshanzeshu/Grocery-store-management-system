
# Grocery Store Management System

A Grocery Store Management System built using Flask (Python framework) and MySQL as the database. This project allows users to manage grocery orders and products in a simple, intuitive interface. It supports creating new orders, updating orders, managing product inventory, and tracking customer details.




## Features

 - Order Management: Place new orders, update existing ones, and remove orders.
 - Product Management: Add new products, update stock and pricing, and remove products from the system.
 - Inventory Tracking: Automatically updates product stock after an order is placed.]
 - User-friendly Interface: A clean, easy-to-use interface for managing orders and products.


 ## Benefits

 - Automates Store Operations: Reduces the manual workload by automating product and order management.

 - Inventory Management: Automatically reduces stock when orders are placed, helping track product availability.

 - Order Tracking: Allows tracking customer orders and managing order updates or cancellations.

 - Efficiency: Increases operational efficiency by centralizing all store data, including orders and product inventory.


## Prerequisites

- Python 3.x
- MySQL Server: Set up and running with the correct database and table schema.
## Installation and setup

### step 1 : Clone the Repository

```bash
https://github.com/zeeshanzeshu/Grocery-Store-Managment-System.git

```



### step 2 : Create virtual envoirment

```bash
py -3 -m venv .venv

```


### step 3 : Activate the virtual envoirment

```bash

.venv\Scripts\activate

```

### step 3 : Install flask Library

```bash
pip install flask

```
### step 2 : Install pymsql library for database to connect

```bash
pip install pymysql

```

### step 2 : Set up mysql database

- Create a MySQL database named grocery_store.
- use database grocery_store
- Run the following SQL queries to create the necessary tables below

```bash

CREATE TABLE products (
  id INT AUTO_INCREMENT PRIMARY KEY,
  product_name VARCHAR(255),
  product_price DECIMAL(10, 2),
  product_stock INT
);

CREATE TABLE orders (
  id INT AUTO_INCREMENT PRIMARY KEY,
  customer_name VARCHAR(255),
  customer_contact VARCHAR(255),
  product_name VARCHAR(255),
  total_product INT,
  total_amount DECIMAL(10, 2),
  date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

```



### step 5 : Step 5: Configure the Database in app.py
- Ensure your database connection settings are correct in the connect_db() function inside app.py

```bash

def connect_db():
    return pymysql.connect(
        host="localhost",
        user="root",  # Your MySQL username
        password="your_password_here",  # Your MySQL password
        db="grocery_store",
        cursorclass=pymysql.cursors.DictCursor
    )





```


### step 6 : Run the application

```bash
python app.py


```
- The application will start on http://127.0.0.1:5000/ or localhost:5000. You can access the app through your browser.


## Usage
- Manage Products: Add, update, or remove products in the inventory. Track product prices and stock levels.

- New Order: Place a new order by selecting a product, quantity, and customer details. The stock will be automatically updated.

- Update Orders: Modify existing orders, including updating quantities, customer information, and total amount.

- Delete Orders: Remove unwanted orders from the system.


# Contributing

Feel free to fork this repository and submit pull requests. We welcome all contributions to improve this project!
