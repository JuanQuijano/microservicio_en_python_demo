from flask import Flask, request, jsonify
from flask_cors import CORS

def create_app():
    app = Flask(__name__)
    return app

app = create_app()
CORS(app)
app.run(port=5000)

def sumar(a, b):
    try:
        resultado = a + b
        return resultado
    except Exception as e:
        return f"Error al sumar: {str(e)}"

@app.route("/sumar", methods=["POST"])
def sumar_handler():
    try:
        data = request.get_json()
        cantidad1 = float(data["cantidad1"])
        cantidad2 = float(data["cantidad2"])
        resultado_suma = sumar(cantidad1, cantidad2)
        return jsonify({"resultado": resultado_suma})
    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == "__main__":
    app.run(debug=True)

