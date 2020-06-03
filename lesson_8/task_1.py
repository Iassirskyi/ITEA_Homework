from flask import Flask
import sqlite3
from flask import render_template

"""
Создать базу данных товаров, у товара есть: Категория (связанная
таблица), название, есть ли товар в продаже или на складе, цена, кол-во
единиц.Создать html страницу. На первой странице выводить ссылки на все
категории, при переходе на категорию получать список всех товаров в
наличии ссылками, при клике на товар выводить его цену, полное описание и
кол-во единиц в наличии.
"""

app = Flask(__name__)


@app.route('/')
def start():
    conn = sqlite3.connect('products_base.db')
    cursor = conn.cursor()
    res = cursor.execute("SELECT * FROM category")
    product_category = dict(res.fetchall())
    res.close()
    return render_template('index_1.html', product_category=product_category)


@app.route('/<product_category>/')
def category(product_category):

    conn = sqlite3.connect('products_base.db')
    cursor = conn.cursor()
    res = cursor.execute("""
                            SELECT list.id, product FROM list
                            INNER JOIN category
                            ON list.type = category.id
                            WHERE in_stock = 1 and category.name == ?
                        
                        """, [product_category])
    category = dict(res.fetchall())
    res.close()
    return render_template('product.html', category=category)


@app.route('/<product_category>/<product_name>')
def info(product_category, product_name):
    conn = sqlite3.connect('products_base.db')
    cursor = conn.cursor()
    res = cursor.execute("""
                            SELECT product, price, quantity FROM list
                            INNER JOIN category
                            ON list.type = category.id
                            WHERE category.name = ? and product = ?                      
                        """, [product_category, product_name])
    product_info = res.fetchone()
    res.close()
    return render_template('name_product.html',
                           product_info=product_info,
                           info=product_info[0],
                           price=product_info[1],
                           quantity=product_info[2])


if __name__ == '__main__':
    app.run(debug=True)
