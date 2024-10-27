### 65 ###
# API data

import requests as req
import json

base_url = "https://fakestoreapi.com"

# All Products
def get_products():
    res = req.get(f"{base_url}/products")

    if res.status_code == 200:
        data = res.json()

        formatted_data = json.dumps(data, indent=4)

        return formatted_data
    else:
        return f"Failed to retrieve date: {res.status_code}"

# products = get_products()
# print(products)

# Single Product
def get_single_product(id):
    res = req.get(f"{base_url}/products/{id}")

    if res.status_code == 200:
        data = res.json()

        formatted_data = json.dumps(data, indent=4)

        return formatted_data
    else:
        return f"Failed to retrieve date: {res.status_code}"
    
single_product = get_single_product(1)
print(single_product)