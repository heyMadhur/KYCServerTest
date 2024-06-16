'''
    1. Nutriments (40%): This category contributes the most to the health score as it provides detailed nutritional information.
    2. Ingredients (30%): The quality and types of ingredients used are crucial for determining the healthiness of the product.
    3. Nutrient Levels (15%): Balancing different nutrients is important for overall health.
    4. PNNS Groups (5%): Grouping products based on nutritional profiles provides context for assessing healthiness.
    5. Allergens (5%): Allergen information is essential for individuals with dietary restrictions.
    6. Ecoscore (3%): Considering environmental impact can be part of a holistic approach to healthiness.
    7. Packaging (2%): Sustainable packaging contributes to overall health and environmental well-being.
    8. Popularity (0%): Popularity metrics are not directly related to healthiness and are not included in the score.
'''

# Health Score = (Nutriments * 0.4) + (Ingredients * 0.3) + (Nutrient Levels * 0.15) + (PNNS Groups * 0.05) + (Allergens * 0.05) + (Ecoscore * 0.03) + (Packaging * 0.02)



from Models.Cohere.cohere_bot import agent_cohere
import json

def nutrient_score(product):
    nutrients= product.get("product_nutrients")
    try:
        response,explanation= agent_cohere(str(nutrients))
        response= json.loads(response)
        score= response.get("Score")
        return float(score), explanation, response
    except Exception as e:
        print("Error in Nutrient Score: ", e)
        return 0, "", {}

def calculate_eco_score(product):
    ecoscore=product.get("product_ecoscore")
    if ecoscore:
        grade= ecoscore.get("grade")
        score= ecoscore.get("score")
        try:
            return float(score), grade
        except (ValueError, TypeError):
            return 0, grade
    else:
        return 0, "N/A"
    


def evaluate_health(product):
    nutri_score, explanation, response= nutrient_score(product)
    def_nutri= response.get("Nutrients less than Sufficient Quantity")
    suf_nutri= response.get("Nutrients with Sufficient Quantity")
    exc_nutri= response.get("Nutrients with Excessive Quantity")
    
    print("Nutrients less than Sufficient Quantity", def_nutri)
    print("Nutrients with Sufficient Quantity", suf_nutri)
    print("Nutrients with Excessive Quantity", exc_nutri)
    
    eco_score, eco_grade= calculate_eco_score(product)
    
        # Ensure nutri_score and eco_score are numeric
    try:
        nutri_score = float(nutri_score)
    except (ValueError, TypeError):
        nutri_score = 0
    
    try:
        eco_score = float(eco_score)
    except (ValueError, TypeError):
        eco_score = 0
    
    Overall_Health_Score= 0.6*nutri_score + 0.4* eco_score
    
    return Overall_Health_Score, eco_grade, explanation, def_nutri, suf_nutri, exc_nutri
    
    
    
    
    
    
    
# evaluate_health({'product_code': '8901058904741', 'product_name': 0, 'product_brand': 'KitKat', 'product_category': 'Snacks, Sweet snacks, Biscuits and cakes, Biscuits, Wafers', 'product_popularity': 7, 'product_images': {'front': {'display': {'en': 'https://images.openfoodfacts.org/images/products/890/105/890/4741/front_en.3.400.jpg'}, 'small': {'en': 'https://images.openfoodfacts.org/images/products/890/105/890/4741/front_en.3.200.jpg'}, 'thumb': {'en': 'https://images.openfoodfacts.org/images/products/890/105/890/4741/front_en.3.100.jpg'}}, 'ingredients': {'display': {'en': 'https://images.openfoodfacts.org/images/products/890/105/890/4741/ingredients_en.7.400.jpg'}, 'small': {'en': 'https://images.openfoodfacts.org/images/products/890/105/890/4741/ingredients_en.7.200.jpg'}, 'thumb': {'en': 'https://images.openfoodfacts.org/images/products/890/105/890/4741/ingredients_en.7.100.jpg'}}, 'nutrition': {'display': {'en': 'https://images.openfoodfacts.org/images/products/890/105/890/4741/nutrition_en.5.400.jpg'}, 'small': {'en': 'https://images.openfoodfacts.org/images/products/890/105/890/4741/nutrition_en.5.200.jpg'}, 'thumb': {'en': 'https://images.openfoodfacts.org/images/products/890/105/890/4741/nutrition_en.5.100.jpg'}}, 'packaging': {'display': {'en': 'https://images.openfoodfacts.org/images/products/890/105/890/4741/packaging_en.9.400.jpg'}, 'small': {'en': 'https://images.openfoodfacts.org/images/products/890/105/890/4741/packaging_en.9.200.jpg'}, 'thumb': {'en': 'https://images.openfoodfacts.org/images/products/890/105/890/4741/packaging_en.9.100.jpg'}}}, 'product_nutrients': {'carbohydrates': 47.4, 'carbohydrates_100g': 47.4, 'carbohydrates_unit': 'g', 'carbohydrates_value': 47.4, 'energy': 0.448, 'energy-kcal': 448, 'energy-kcal_100g': 448, 'energy-kcal_unit': 'kcal', 'energy-kcal_value': 448, 'energy-kcal_value_computed': 447.8, 'energy-kj': 0.448, 'energy-kj_100g': 0.448, 'energy-kj_unit': 'kJ', 'energy-kj_value': 0.448, 'energy-kj_value_computed': 1870.9, 'energy_100g': 0.448, 'energy_unit': 'kJ', 'energy_value': 0.448, 'fat': 25.8, 'fat_100g': 25.8, 'fat_unit': 'g', 'fat_value': 25.8, 'fiber': 0, 'fiber_100g': 0, 'fiber_unit': 'g', 'fiber_value': 0, 'proteins': 6.5, 'proteins_100g': 6.5, 'proteins_unit': 'g', 'proteins_value': 6.5, 'saturated-fat': 23, 'saturated-fat_100g': 23, 'saturated-fat_unit': 'g', 'saturated-fat_value': 23, 'sugars': 37.8, 'sugars_100g': 37.8, 'sugars_unit': 'g', 'sugars_value': 37.8}, 'product_nutrient_level': {'fat': 'high', 'saturated-fat': 'high', 'sugars': 'high'}, 'product_ingredients': 0, 'product_pnns_g1': 'Sugary snacks', 'product_pnns_g2': 'Biscuits and cakes', 'product_allergens': '', 'product_allergens_from_ingredients': '', 'product_ecoscore': {'adjustments': {'origins_of_ingredients': {'aggregated_origins': [{'epi_score': '0', 'origin': 'en:unknown', 'percent': 100, 'transportation_score': None}], 'epi_score': 0, 'epi_value': -5, 'origins_from_categories': ['en:unknown'], 'origins_from_origins_field': ['en:unknown'], 'transportation_score': 0, 'transportation_scores': {'ad': 0, 'al': 0, 'at': 0, 'ax': 0, 'ba': 0, 'be': 0, 'bg': 0, 'ch': 0, 'cy': 0, 'cz': 0, 'de': 0, 'dk': 0, 'dz': 0, 'ee': 0, 'eg': 0, 'es': 0, 'fi': 0, 'fo': 0, 'fr': 0, 'gg': 0, 'gi': 0, 'gr': 0, 'hr': 0, 'hu': 0, 'ie': 0, 'il': 0, 'im': 0, 'is': 0, 'it': 0, 'je': 0, 'lb': 0, 'li': 0, 'lt': 0, 'lu': 0, 'lv': 0, 'ly': 0, 'ma': 0, 'mc': 0, 'md': 0, 'me': 0, 'mk': 0, 'mt': 0, 'nl': 0, 'no': 0, 'pl': 0, 'ps': 0, 'pt': 0, 'ro': 0, 'rs': 0, 'se': 0, 'si': 0, 'sj': 0, 'sk': 0, 'sm': 0, 'sy': 0, 'tn': 0, 'tr': 0, 'ua': 0, 'uk': 0, 'us': 0, 'va': 0, 'world': 0, 'xk': 0}, 'transportation_value': 0, 'transportation_values': {'ad': 0, 'al': 0, 'at': 0, 'ax': 0, 'ba': 0, 'be': 0, 'bg': 0, 'ch': 0, 'cy': 0, 'cz': 0, 'de': 0, 'dk': 0, 'dz': 0, 'ee': 0, 'eg': 0, 'es': 0, 'fi': 0, 'fo': 0, 'fr': 0, 'gg': 0, 'gi': 0, 'gr': 0, 'hr': 0, 'hu': 0, 'ie': 0, 'il': 0, 'im': 0, 'is': 0, 'it': 0, 'je': 0, 'lb': 0, 'li': 0, 'lt': 0, 'lu': 0, 'lv': 0, 'ly': 0, 'ma': 0, 'mc': 0, 'md': 0, 'me': 0, 'mk': 0, 'mt': 0, 'nl': 0, 'no': 0, 'pl': 0, 'ps': 0, 'pt': 0, 'ro': 0, 'rs': 0, 'se': 0, 'si': 0, 'sj': 0, 'sk': 0, 'sm': 0, 'sy': 0, 'tn': 0, 'tr': 0, 'ua': 0, 'uk': 0, 'us': 0, 'va': 0, 'world': 0, 'xk': 0}, 'value': -5, 'values': {'ad': -5, 'al': -5, 'at': -5, 'ax': -5, 'ba': -5, 'be': -5, 'bg': -5, 'ch': -5, 'cy': -5, 'cz': -5, 'de': -5, 'dk': -5, 'dz': -5, 'ee': -5, 'eg': -5, 'es': -5, 'fi': -5, 'fo': -5, 'fr': -5, 'gg': -5, 'gi': -5, 'gr': -5, 'hr': -5, 'hu': -5, 'ie': -5, 'il': -5, 'im': -5, 'is': -5, 'it': -5, 'je': -5, 'lb': -5, 'li': -5, 'lt': -5, 'lu': -5, 'lv': -5, 'ly': -5, 'ma': -5, 'mc': -5, 'md': -5, 'me': -5, 'mk': -5, 'mt': -5, 'nl': -5, 'no': -5, 'pl': -5, 'ps': -5, 'pt': -5, 'ro': -5, 'rs': -5, 'se': -5, 'si': -5, 'sj': -5, 'sk': -5, 'sm': -5, 'sy': -5, 'tn': -5, 'tr': -5, 'ua': -5, 'uk': -5, 'us': -5, 'va': -5, 'world': -5, 'xk': -5}, 'warning': 'origins_are_100_percent_unknown'}, 'packaging': {'non_recyclable_and_non_biodegradable_materials': 1, 'value': -15, 'warning': 'packaging_data_missing'}, 'production_system': {'labels': [], 'value': 0, 'warning': 'no_label'}, 'threatened_species': {'warning': 'ingredients_missing'}}, 'agribalyse': {'agribalyse_food_code': '23853', 'co2_agriculture': 1.8355522, 'co2_consumption': 0, 'co2_distribution': 0.019530673, 'co2_packaging': 0.2881877, 'co2_processing': 0.19596158, 'co2_total': 2.469517963, 'co2_transportation': 0.13028581, 'code': '23853', 'dqr': '2.13', 'ef_agriculture': 0.22360441, 'ef_consumption': 0, 'ef_distribution': 0.0048315303, 'ef_packaging': 0.018915614, 'ef_processing': 0.037274511, 'ef_total': 0.2951071423, 'ef_transportation': 0.010481077, 'is_beverage': 0, 'name_en': 'Wafer biscuit, crunchy (thin or dry), plain or with sugar, prepacked', 'name_fr': 'Gaufre croustillante (fine ou sèche), nature ou sucrée, préemballée', 'score': 77, 'version': '3.1'}, 'grade': 'c', 'grades': {'ad': 'c', 'al': 'c', 'at': 'c', 'ax': 'c', 'ba': 'c', 'be': 'c', 'bg': 'c', 'ch': 'c', 'cy': 'c', 'cz': 'c', 'de': 'c', 'dk': 'c', 'dz': 'c', 'ee': 'c', 'eg': 'c', 'es': 'c', 'fi': 'c', 'fo': 'c', 'fr': 'c', 'gg': 'c', 'gi': 'c', 'gr': 'c', 'hr': 'c', 'hu': 'c', 'ie': 'c', 'il': 'c', 'im': 'c', 'is': 'c', 'it': 'c', 'je': 'c', 'lb': 'c', 'li': 'c', 'lt': 'c', 'lu': 'c', 'lv': 'c', 'ly': 'c', 'ma': 'c', 'mc': 'c', 'md': 'c', 'me': 'c', 'mk': 'c', 'mt': 'c', 'nl': 'c', 'no': 'c', 'pl': 'c', 'ps': 'c', 'pt': 'c', 'ro': 'c', 'rs': 'c', 'se': 'c', 'si': 'c', 'sj': 'c', 'sk': 'c', 'sm': 'c', 'sy': 'c', 'tn': 'c', 'tr': 'c', 'ua': 'c', 'uk': 'c', 'us': 'c', 'va': 'c', 'world': 'c', 'xk': 'c'}, 'missing': {'ingredients': 1, 'labels': 1, 'origins': 1, 'packagings': 1}, 'missing_data_warning': 1, 'missing_key_data': 1, 'previous_data': {'agribalyse': {'warning': 'missing_agribalyse_match'}, 'grade': None, 'score': None}, 'score': 57, 'scores': {'ad': 57, 'al': 57, 'at': 57, 'ax': 57, 'ba': 57, 'be': 57, 'bg': 57, 'ch': 57, 'cy': 57, 'cz': 57, 'de': 57, 'dk': 57, 'dz': 57, 'ee': 57, 'eg': 57, 'es': 57, 'fi': 57, 'fo': 57, 'fr': 57, 'gg': 57, 'gi': 57, 'gr': 57, 'hr': 57, 'hu': 57, 'ie': 57, 'il': 57, 'im': 57, 'is': 57, 'it': 57, 'je': 57, 'lb': 57, 'li': 57, 'lt': 57, 'lu': 57, 'lv': 57, 'ly': 57, 'ma': 57, 'mc': 57, 'md': 57, 'me': 57, 'mk': 57, 'mt': 57, 'nl': 57, 'no': 57, 'pl': 57, 'ps': 57, 'pt': 57, 'ro': 57, 'rs': 57, 'se': 57, 'si': 57, 'sj': 57, 'sk': 57, 'sm': 57, 'sy': 57, 'tn': 57, 'tr': 57, 'ua': 57, 'uk': 57, 'us': 57, 'va': 57, 'world': 57, 'xk': 57}, 'status': 'known'}, 'product_packaging': []})