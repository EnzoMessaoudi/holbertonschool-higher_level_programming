from flask import Flask, render_template, request
from helpers import read_json, read_csv
import json

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route("/items")
def items_page():
    with open("items.json") as f:
        data = json.load(f)
    items_list = data.get("items", [])

    return render_template("items.html", items=items_list)

@app.route("/products")
def products_page():
    source = request.args.get('source', '').lower()
    product_id = request.args.get('id', type=int)

    error = None
    products = []

    if source == 'json':
        products = read_json('products.json')
    elif source == 'csv':
        products = read_csv('products.csv')
    else:
        error = "Wrong source"

    if product_id and products:
        filtered = [p for p in products if p['id'] == product_id]
        if not filtered:
            error = "Product not found"
            products = []
        else:
            products = filtered

    return render_template('product_display.html', products=products, error=error)

if __name__ == '__main__':
    app.run(debug=True, port=5000)