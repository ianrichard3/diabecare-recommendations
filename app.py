from flask import Flask, request, jsonify
from validators import validate_glucose_state, validate_user_state, get_body_data, validate_glucose_trend



app = Flask(__name__)


@app.route('/recommendation', methods=["POST"])
def generate_recommendation():
    data = get_body_data(request)

    user_state = data.get("user_state")
    glucose_state = data.get("glucose_state")
    glucose_trend = data.get("glucose_trend")

    missing_fields = []
    if user_state is None:
        missing_fields.append("user_state")
    if glucose_state is None:
        missing_fields.append("glucose_state")
    if glucose_trend is None:
        missing_fields.append("glucose_trend")

    if missing_fields:
        return jsonify({"error": f"Missing required field(s): {', '.join(missing_fields)}"}), 400

    if not validate_user_state(user_state):
        return jsonify({"error": f"Invalid value for user_state: {user_state}"}), 400
    if not validate_glucose_state(glucose_state):
        return jsonify({"error": f"Invalid value for glucose_state: {glucose_state}"}), 400
    if not validate_glucose_trend(glucose_trend):
        return jsonify({"error": f"Invalid value for glucose_trend: {glucose_trend}"}), 400

    return jsonify({
        "status": "success",
        "states": f"Glucose: {glucose_state} - User: {user_state} - Trend: {glucose_trend}",
        "format": "json",
        "recommendation": {
            "activity": "N/A",
            "insulin": "N/A",
            "food": "N/A"
        }
    }), 200





if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)