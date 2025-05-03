from flask import Flask

from flask import request, jsonify

app = Flask(__name__)


# =========================
# PRUEBAS BASICAS
# =========================


@app.route("/")
def hello():
    return "Hola Flask"


# Path variables
@app.route("/user/<nombre>")
def user(nombre):
    return f"Hola {nombre}"



# Query params
@app.route("/products")
def products():
    search = request.args.get("search")
    todos = request.args.to_dict()
    return f"{todos}"


# Body Form
@app.route("/formulario", methods=["POST"])
def formulario():
    nombre = request.form.get("nombre")
    return f"{nombre}"


# Body params (json)
@app.route("/json", methods=["POST"])
def json():
    data = request.get_json()
    nombre = data.get("nombre")
    return jsonify({"status": "success", "message": f"{nombre}", "data": data})


# Body both
@app.route("/datos", methods=["POST"])
def recibir_datos():
    if request.is_json:
        data = request.get_json()
    else:
        data = request.form.to_dict()
    
    nombre = data.get("nombre", "Desconocido")
    edad = data.get("edad", "No especificada")

    return jsonify({
        "mensaje": f"Hola {nombre}, edad: {edad}",
        "formato": "json" if request.is_json else "form"
    })




if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)