from flask import Flask, request, jsonify
from flask_cors import CORS
from Product.Required_JSON import call_api
from Health_Score.Health_Score_Generator import evaluate_health
import json

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

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
    
    if response:
        return response
    
    else:
        # This case should not occur because call_api handles the None case and returns a tuple with an error message
        return jsonify({'error': 'Unexpected error occurred'}), 500
    
@app.route("/get_product_score", methods=['GET'])
def get_product_score():
    barcode= request.args.get('barcode')
    if not barcode:
        return jsonify({'error': 'Barcode not provided'}), 400
    
    print("Fetching Product Info")
    response= call_api(barcode)
    
    # print("---------------------------------------response---------------------------------------")
    # print(type(response))
    
    if not isinstance(response, tuple):
        # print("INDIE IF--------------------------------------------------")
        scores_data = evaluate_health(response)
        final_response= {**response, **scores_data}
        return jsonify(final_response)
        
    
    else:
        # This case should not occur because call_api handles the None case and returns a tuple with an error message
        return jsonify({'error': 'Unexpected error occurred'}), 500
    
if __name__ == '__main__':
    app.run(debug=True)