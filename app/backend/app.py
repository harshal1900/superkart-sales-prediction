import os
import joblib
import pandas as pd
from flask import Flask, request, jsonify

# Initialize Flask application
superkart_api = Flask(__name__)

# Load serialized machine learning model (full preprocessing + regressor pipeline)
MODEL_PATH = "superkart_model.joblib"
model = joblib.load(MODEL_PATH)


@superkart_api.route("/", methods=["GET"])
def home():
    return jsonify({
        "message": "SuperKart Sales Prediction API is running!",
        "status": "success"
    })


@superkart_api.route("/v1/predict", methods=["POST"])
def predict():
    try:
        data = request.get_json()
        df = pd.DataFrame([data])
        prediction = model.predict(df)
        return jsonify({
            "status": "success",
            "prediction": float(prediction[0])
        })
    except Exception as e:
        return jsonify({
            "status": "error",
            "message": str(e)
        }), 400


@superkart_api.route("/v1/predictbatch", methods=["POST"])
def predict_batch():
    try:
        if "file" not in request.files:
            return jsonify({
                "status": "error",
                "message": "No file part in the request. Expected form field 'file'."
            }), 400

        file = request.files["file"]
        input_df = pd.read_csv(file)
        predictions = model.predict(input_df)

        predictions_dict = {
            str(idx): float(pred) for idx, pred in zip(input_df.index, predictions)
        }
        return jsonify(predictions_dict)
    except Exception as e:
        return jsonify({
            "status": "error",
            "message": str(e)
        }), 400


if __name__ == "__main__":
    superkart_api.run(host="0.0.0.0", port=7860)
