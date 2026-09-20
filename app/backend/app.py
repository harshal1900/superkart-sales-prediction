import os
import joblib
import pandas as pd
from flask import Flask, request, jsonify

# Initialize Flask application
superkart_api = Flask(__name__)

# Load serialized machine learning model relative to backend location
MODEL_PATH = os.path.join(os.path.dirname(__file__), "../../models/superkart_model.joblib")
model = joblib.load(MODEL_PATH)


@superkart_api.route("/", methods=["GET"])
def home():
    """Health check endpoint."""
    return jsonify({
        "status": "success",
        "message": "SuperKart Sales Prediction API is running!"
    }), 200


@superkart_api.route("/v1/predict", methods=["POST"])
def predict():
    """Online inference endpoint for single product sales prediction."""
    try:
        data = request.get_json(force=True)
        input_df = pd.DataFrame([data])
        prediction = model.predict(input_df)[0]
        return jsonify({
            "status": "success",
            "prediction": float(prediction)
        }), 200
    except Exception as e:
        return jsonify({
            "status": "error",
            "message": str(e)
        }), 400


@superkart_api.route("/v1/predictbatch", methods=["POST"])
def predict_batch():
    """Batch inference endpoint accepting CSV file upload."""
    try:
        if "file" not in request.files:
            return jsonify({"status": "error", "message": "No file uploaded"}), 400

        file = request.files["file"]
        input_df = pd.read_csv(file)
        predictions = model.predict(input_df)

        results = {int(idx): float(pred) for idx, pred in enumerate(predictions)}
        return jsonify(results), 200
    except Exception as e:
        return jsonify({
            "status": "error",
            "message": str(e)
        }), 400


if __name__ == "__main__":
    superkart_api.run(host="0.0.0.0", port=7860, debug=True)
