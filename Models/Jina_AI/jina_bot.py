import requests

url = 'https://api.jina.ai/v1/embeddings'

headers = {
  'Content-Type': 'application/json',
  'Authorization': 'Bearer jina_f18b25aabf7b44cbb86b6b7ef3c820b4U8mRjv3ewT_QvS-GtSgZWHxnqdSQ'
}

context= "You are a Strict Dietician. You will be given a list of nutrients name and their percentage in a packaged food. Based on that identify which nutrients are good and which are bad and give a number from 1 to 100 based on how healthy the food is. Greater Number means healthy food. IMPORTANT: Answer Strictly in given JSON Format: { Score: 'Score from 1 to 100', Nutrients with Sufficient Quantity: [List of nutrients], Nutrients less than Sufficient Quantity: [List of Nutrients], Nutrients with Excessive Quantity: {List of Nutrients] }"

ingr= "{'carbohydrates': 47.4, 'carbohydrates_100g': 47.4, 'carbohydrates_unit': 'g', 'carbohydrates_value': 47.4, 'energy': 0.448, 'energy-kcal': 448, 'energy-kcal_100g': 448, 'energy-kcal_unit': 'kcal', 'energy-kcal_value': 448, 'energy-kcal_value_computed': 447.8, 'energy-kj': 0.448, 'energy-kj_100g': 0.448, 'energy-kj_unit': 'kJ', 'energy-kj_value': 0.448, 'energy-kj_value_computed': 1870.9, 'energy_100g': 0.448, 'energy_unit': 'kJ', 'energy_value': 0.448, 'fat': 25.8, 'fat_100g': 25.8, 'fat_unit': 'g', 'fat_value': 25.8, 'fiber': 0, 'fiber_100g': 0, 'fiber_unit': 'g', 'fiber_value': 0, 'proteins': 6.5, 'proteins_100g': 6.5, 'proteins_unit': 'g', 'proteins_value': 6.5, 'saturated-fat': 23, 'saturated-fat_100g': 23, 'saturated-fat_unit': 'g', 'saturated-fat_value': 23, 'sugars': 37.8, 'sugars_100g': 37.8, 'sugars_unit': 'g', 'sugars_value': 37.8}"

data = {
#   'input': [context, ingr],
  'input': ["Your text string goes here", "You can send multiple texts"],
  'model': 'jina-embeddings-v2-base-en',
  'encoding_type': 'base64'
}

response = requests.post(url, headers=headers, json=data)
print(response.text)
