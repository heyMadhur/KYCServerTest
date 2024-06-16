from flask import Flask, request, jsonify
from flask_cors import CORS
from Product.Required_JSON import call_api
from Health_Score.Health_Score_Generator import evaluate_health

app = Flask(__name__)

@app.route("/")
def start():
    return "The KYC Server is Running"

@app.route("/get_product_info", methods=['GET'])
def get_product_info():
    barcode= request.args.get('barcode')
    if not barcode:
        return jsonify({'error': 'Barcode not provided'}), 400
    
    print("Fetching Product Info")
    response= call_api(barcode)
    print("WE ARE PRINTING")
    
    if response:
        Health_Score, eco_grade, explanation, def_nutri, suf_nutri, exc_nutri = evaluate_health(response)
        return jsonify({
            'Health Score': Health_Score,
            'Grade': eco_grade.capitalize(),
            'Nutrient Analysis': {
                'Deficient Nutrients': def_nutri,
                'Sufficient Nutrients': suf_nutri,
                'Excessive Nutrients': exc_nutri
            },
            'Inference': explanation
        })
    
    else:
        # This case should not occur because call_api handles the None case and returns a tuple with an error message
        return jsonify({'error': 'Unexpected error occurred'}), 500


