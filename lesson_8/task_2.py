from flask import Flask
from flask import render_template, request
import sqlite3

"""
Создать страницу для администратора, через которую он может добавлять
новые товары и категории.
"""

app = Flask(__name__)


@app.route('/')
def start():
    return render_template('admin_index.html')


@app.route('/admin', methods=['POST'])
def add_category():
    category = request.form['category']
    conn = sqlite3.connect('products_base.db')
    cursor = conn.cursor()
    res = cursor.execute("""
                        INSERT INTO category (name)
                        VALUES (?)                        
                        """, [category])
    conn.commit()
    res.close()
    return render_template('admin_products.html')


@app.route('/products', methods=['POST'])
def new_products():
    product = request.form['product']
    price = int(request.form['price'])
    quantity = int(request.form['quantity'])
    in_stock = int(request.form['in_stock'])
    type_ = int(request.form['type_'])
    conn = sqlite3.connect('products_base.db')
    cursor = conn.cursor()
    res = cursor.execute("""
                        INSERT INTO list (product, price, quantity, in_stock, type)
                        VALUES (?, ?, ?, ?, ?)
                        """, [product, price, quantity, in_stock, type_])
    conn.commit()
    res.close()
    return 'Product was added'


app.run(debug=True)


