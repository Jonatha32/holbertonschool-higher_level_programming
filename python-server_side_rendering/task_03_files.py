from flask import Flask, render_template, request
import json
import csv

app = Flask(__name__)

def read_json():
    try:
        with open('products.json') as f:
            return json.load(f)
    except Exception as e:
        return []

def read_csv():
    try:
        with open('products.csv') as f:
            read = csv.DictReader(f)
            return [
                dict(
                    id=int(row['id']),
                    name=row['name'],
                    category=row['category'],
                    price=float(row['price']),
                )
                for row in read
            ]
    except Exception as e:
        return []

@app.route('/products')
def display_products():
    source = request.args.get('source')
    product_id = request.args.get('id', type=int)
    er = None
    prod = []
    
    if source == 'json':
        prod = read_json()
    elif source == 'csv':
        prod = read_csv()
    else:
        er = "Wrong source"
        return render_template('error.html', error=er)
    
    if product_id is not None:
        prod = [p for p in prod if p['id'] == product_id]
        if not prod:
            er = "Product not found"
    
    return render_template('products.html', products=prod, error=er)