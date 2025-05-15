from flask import Flask, request, jsonify
from validators import validate_float, get_body_data
from recommendations import generate_basic_recommendation



app = Flask(__name__)


@app.route("/get-basic-recommendation", methods=["POST"])
def recibir_datos():
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
        "glucose_level_string": f"{glucose_level} mg/dL",
        "glucose_level": glucose_level,
        "recommendation": f"{recommendation}",
        "format": "json" if request.is_json else "form"
    }), 200
    
    
    
    
if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)