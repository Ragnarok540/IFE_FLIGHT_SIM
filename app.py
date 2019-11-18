from flask import Flask, jsonify
#from simulador import Simulador

app = Flask(__name__)

@app.route('/ping', methods=['GET'])
def ping():
    status = "200"
    message = "pong"

    return jsonify(status=status,
                   message=message)

@app.route('/ubicacion', methods=['GET'])
def ubicacion():
    status = "500"
    message = "No implementado"

    return jsonify(status=status,
                   message=message)

@app.route('/tiempo_de_vuelo_actual', methods=['GET'])
def tiempo_de_vuelo_actual():
    status = "500"
    message = "No implementado"

    return jsonify(status=status,
                   message=message)

@app.route('/tiempo_de_vuelo_restante', methods=['GET'])
def tiempo_de_vuelo_restante():
    status = "500"
    message = "No implementado"

    return jsonify(status=status,
                   message=message)

@app.route('/temperatura_exterior', methods=['GET'])
def temperatura_exterior():
    status = "500"
    message = "No implementado"

    return jsonify(status=status,
                   message=message)

@app.route('/temperatura_interior', methods=['GET'])
def temperatura_interior():
    status = "500"
    message = "No implementado"

    return jsonify(status=status,
                   message=message)

@app.route('/altitud', methods=['GET'])
def altitud():
    status = "500"
    message = "No implementado"

    return jsonify(status=status,
                   message=message)

@app.route('/velocidad', methods=['GET'])
def velocidad():
    status = "500"
    message = "No implementado"

    return jsonify(status=status,
                   message=message)

@app.route('/iniciar_vuelo', methods=['POST'])
def iniciar_vuelo():
    status = "500"
    message = "No implementado"

    return jsonify(status=status,
                   message=message)

@app.route('/terminar_vuelo', methods=['DELETE'])
def terminar_vuelo():
    status = "500"
    message = "No implementado"

    return jsonify(status=status,
                   message=message)

if __name__ == "__main__":
    app.run(host="0.0.0.0")
