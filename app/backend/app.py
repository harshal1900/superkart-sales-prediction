import os
import joblib
import pandas as pd
from flask import Flask, request, jsonify

# Initialize Flask application
superkart_api = Flask(__name__)

# Load serialized machine learning model locally within the container
MODEL_PATH = "superkart_model.joblib"
model = joblib.load(MODEL_PATH)

@superkart_api.route("/", methods=["GET"])
def home():
    return jsonify({
        "message": "SuperKart Sales Prediction API is running!",
        "status": "success"
    })

@superkart_api.route("/predict", methods=["POST"])
def predict():
    try:
        data = request.get_json()
        df = pd.DataFrame([data])
        prediction = model.predict(df)
        return jsonify({
            "status": "success",
            "predicted_sales": float(prediction[0])
        })
    except Exception as e:
        return jsonify({
            "status": "error",
            "message": str(e)
        }), 400

if __name__ == "__main__":
    superkart_api.run(host="0.0.0.0", port=7860)
