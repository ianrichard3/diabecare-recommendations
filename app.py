from flask import Flask, request, jsonify
from validators import validate_float, get_body_data
from recommendations import generate_basic_recommendation

app = Flask(__name__)

@app.route("/get-basic-recommendation", methods=["POST"])
def get_basic_recommendation():
    data = get_body_data(request)

    if not validate_float(data.get("glucose_level")):
        return jsonify({
          "message": "Invalid glucose level",
          "format": "json" if request.is_json else "form"
        }), 400

    glucose_level = data.get("glucose_level")
    recommendation = generate_basic_recommendation(glucose_level)

    return jsonify({
        "status": "success",
        "glucose_level": f"{glucose_level} mg/dL",
        "recommendation": f"{recommendation}",
        "format": "json" if request.is_json else "form",
    }), 200





from recommendations import generate_recommendations
from datetime import datetime
# Multi criteria recommendation
@app.route("/get-recommendations", methods=["POST"])
def get_recommendations():
    data = get_body_data(request)

    if not validate_float(data.get("glucose_level")):
        return jsonify({
          "message": "Invalid glucose level",
          "format": "json" if request.is_json else "form"
        }), 400

    glucose_level = data.get("glucose_level")
    recommendation = generate_recommendations(glucose_level)

    return jsonify({
    "status": "success",
    "glucose_level": f"{glucose_level} mg/dL",
    "current_time": f"{datetime.now()}",
    "recommendations": {
        "intake_recommendation": recommendation.get("intake", ""),
        "insulin_recommendation": recommendation.get("insulin", ""),
        "activity_recommendation": recommendation.get("activity", ""),
    },
    "format": "json" if request.is_json else "form",
}), 200





if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)