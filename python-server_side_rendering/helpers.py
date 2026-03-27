import json
import csv

def read_json(file_path):
    try:
        with open(file_path, 'r') as f:
            data = json.load(f)
        return data.get('products', [])
    except Exception as e:
        print("Error reading JSON:", e)
        return []

def read_csv(file_path):
    products = []
    try:
        with open(file_path, newline='') as f:
            reader = csv.DictReader(f)
            for row in reader:
                # Convert price to number if needed
                row['price'] = float(row['price'])
                row['id'] = int(row['id'])
                products.append(row)
        return products
    except Exception as e:
        print("Error reading CSV:", e)
        return []