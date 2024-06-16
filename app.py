from flask import Flask, request, jsonify
from Barcode.capture_barcode import capture_barcode
from Product.Required_JSON import call_api
from Product.Display_Product_Info import display_product_info
from Health_Score.Health_Score_Generator import evaluate_health

app = Flask(__name__)

# @app.route('/scan_barcode', methods=['GET'])
# def scan_barcode_server():
#     print("Scanning for barcode...")
#     barcode = capture_barcode()
#     print(type(barcode))
#     if barcode:
#         print(f"Barcode detected: {barcode}")
#         return jsonify({'barcode': barcode})
#     else:
#         return jsonify({'error': 'No barcode detected'}), 404

@app.route('/')
def start():
    return "The KYC Server is running"



@app.route('/get_product_info', methods=['POST'])
def get_product_info_server():
    barcode = request.get_json()['barcode']
    print("\nFetching product information...")
    response = call_api(barcode)
    if response:
        display_product_info(response)
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
        return jsonify({'error': 'No product information found'}), 404

