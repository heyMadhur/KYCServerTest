'''
Code
Product Name
Brand
Category 
Popularity
Images
Nutrients 
Ingredients 
Nutrient Levels
PNNS Groups
Allergens 
Ecoscore 
Packaging 
'''

import requests
from Health_Score.Health_Score_Generator import evaluate_health




api_url="https://world.openfoodfacts.org/api/v0/product/"

def get_required_json(product_info):
    if product_info['status'] == 1:
        product= product_info['product']
        return {
            'product_code': product.get('_id', 0),      
            'product_name': product.get('product_name', 0),     # Nope
            'product_brand': product.get('brands', 0),      
            'product_category': product.get('categories', 0),   
            'product_popularity': product.get('popularity_key', 0), 
            'product_images': product.get('selected_images', 0),    
            'product_nutrients': product.get('nutriments', 0),  
            'product_nutrient_level': product.get('nutrient_levels', 0),    
            'product_ingredients': product.get('ingredients_text', 0),  # Nope
            'product_pnns_g1': product.get('pnns_groups_1', 0),
            'product_pnns_g2': product.get('pnns_groups_2', 0),
            'product_allergens': product.get('allergens', 0),
            'product_allergens_from_ingredients': product.get('allergens_from_ingredients', 0),
            'product_ecoscore': product.get('ecoscore_score', 0),
            'product_ecograde': product.get('ecoscore_grade', 0),            
            'product_packaging': product.get('packagings', 0),
        }
    else:
        print("Product info not Found in database")
        return None


def call_api(barcode):
    response = requests.get(api_url+barcode+".json", verify=True)
    print("------------------------------------CALL API---------------------------------")
    print(response)
    if response.status_code == 200:
        product_info = response.json()
        # print(response)
        req_json= get_required_json(product_info)
        if req_json:
            return req_json
        else:
            return {'error': 'No product information found'}, 404
    else:
        print(f"Error fetching product information: {response.status_code}")
        return {'error': f"Error fetching product information: {response.status_code}"}, response.status_code       


            



