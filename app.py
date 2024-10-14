from flask import Flask, render_template, request, redirect
import pymysql

app = Flask(__name__)

# Database connection
def connect_db():
    return pymysql.connect(
        host="localhost",
        user="root",
        password="24242424cwa.A",
        db="grocery_store",
        cursorclass=pymysql.cursors.DictCursor
    )

# Main Page - Display Orders
@app.route('/')
def index():
    conn = connect_db()
    with conn.cursor() as cursor:
        cursor.execute("SELECT * FROM orders")
        orders = cursor.fetchall()
    conn.close()
    return render_template('index.html', orders=orders)

# New Order Page
@app.route('/templates/order.html')
def new_order():
    return render_template('order.html')

# Submit New Order
@app.route('/submit_order', methods=['POST'])
def submit_order():
    customer_name = request.form['customer_name']
    customer_contact = request.form['customer_contact']
    product_name = request.form['product_name']
    total_product = request.form['total_product']
    total_amount = request.form['total_amount']

    conn = connect_db()
    with conn.cursor() as cursor:
        sql = "INSERT INTO orders (customer_name, customer_contact, product_name, total_product, total_amount) VALUES (%s, %s, %s, %s, %s)"
        cursor.execute(sql, (customer_name, customer_contact, product_name, total_product, total_amount))
        conn.commit()
    conn.close()
    return redirect('/')

# Update Order
@app.route('/update_order/<int:id>', methods=['GET', 'POST'])
def update_order(id):
    conn = connect_db()

    if request.method == 'POST':
        customer_name = request.form['customer_name']
        customer_contact = request.form['customer_contact']
        product_name = request.form['product_name']
        total_product = request.form['total_product']
        total_amount = request.form['total_amount']

        with conn.cursor() as cursor:
            # Update the order in the database
            sql = """
                UPDATE orders 
                SET customer_name=%s, customer_contact=%s, product_name=%s, total_product=%s, total_amount=%s 
                WHERE id=%s
            """
            cursor.execute(sql, (customer_name, customer_contact, product_name, total_product, total_amount, id))
            conn.commit()
        conn.close()
        return redirect('/')
    
    # Fetch existing data for the order to be updated
    with conn.cursor() as cursor:
        cursor.execute("SELECT * FROM orders WHERE id=%s", (id,))
        order = cursor.fetchone()
    conn.close()
    return render_template('update_order.html', order=order)

# Delete Order
@app.route('/delete_order/<int:id>', methods=['POST'])
def delete_order(id):
    conn = connect_db()
    with conn.cursor() as cursor:
        cursor.execute("DELETE FROM orders WHERE id=%s", (id,))
        conn.commit()
    conn.close()
    return redirect('/')

# Manage Products Page
@app.route('/templates/manage_product.html')
def manage_product():
    conn = connect_db()
    with conn.cursor() as cursor:
        cursor.execute("SELECT * FROM products")
        products = cursor.fetchall()
    conn.close()
    return render_template('manage_product.html', products=products)

# Submit New Product
@app.route('/submit_product', methods=['POST'])
def submit_product():
    product_name = request.form['product_name']
    product_price = request.form['product_price']
    product_stock = request.form['product_stock']

    conn = connect_db()
    with conn.cursor() as cursor:
        sql = "INSERT INTO products (product_name, product_price, product_stock) VALUES (%s, %s, %s)"
        cursor.execute(sql, (product_name, product_price, product_stock))
        conn.commit()
    conn.close()
    return redirect('/templates/manage_product.html')

# Delete Product
@app.route('/delete_product/<int:id>', methods=['POST'])
def delete_product(id):
    conn = connect_db()
    with conn.cursor() as cursor:
        cursor.execute("DELETE FROM products WHERE id=%s", (id,))
        conn.commit()
    conn.close()
    return redirect('/templates/manage_product.html')

# Update Product
@app.route('/update_product/<int:id>', methods=['GET', 'POST'])
def update_product(id):
    conn = connect_db()

    if request.method == 'POST':
        product_name = request.form['product_name']
        product_price = request.form['product_price']
        product_stock = request.form['product_stock']

        with conn.cursor() as cursor:
            sql = """
                UPDATE products 
                SET product_name=%s, product_price=%s, product_stock=%s 
                WHERE id=%s
            """
            cursor.execute(sql, (product_name, product_price, product_stock, id))
            conn.commit()
        conn.close()
        return redirect('/templates/manage_product.html')

    # Fetch existing data for the product
    with conn.cursor() as cursor:
        cursor.execute("SELECT * FROM products WHERE id=%s", (id,))
        product = cursor.fetchone()
    conn.close()
    return render_template('manage_product.html', product=product, update=True)

if __name__ == '__main__':
    app.run(debug=True)
