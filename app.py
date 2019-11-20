from flask import Flask, request, jsonify, g
from simulador import Simulador
from coordenada import Coordenada

sim = Simulador()

app = Flask(__name__)

@app.route('/ping', methods=['GET'])
def ping():
    status = "200"
    message = "pong"

    return jsonify(status=status,
                   message=message)

@app.route('/ubicacion', methods=['GET'])
def ubicacion():
    status = "200"
    message = sim.ubicacion_actual()

    return jsonify(status=status,
                   message=message)

@app.route('/tiempo_de_vuelo_actual', methods=['GET'])
def tiempo_de_vuelo_actual():
    status = "200"
    message = sim.tiempo_transcurrido()

    return jsonify(status=status,
                   message=message)

@app.route('/tiempo_de_vuelo_restante', methods=['GET'])
def tiempo_de_vuelo_restante():
    status = "500"
    message = sim.tiempo_restante()

    return jsonify(status=status,
                   message=message)

@app.route('/temperatura_exterior', methods=['GET'])
def temperatura_exterior():
    status = "200"
    message = sim.temperatura_exterior()

    return jsonify(status=status,
                   message=message)

@app.route('/temperatura_interior', methods=['GET'])
def temperatura_interior():
    status = "200"
    message = sim.temperatura_interior()

    return jsonify(status=status,
                   message=message)

@app.route('/altitud', methods=['GET'])
def altitud():
    status = "200"
    message = sim.altitud()

    return jsonify(status=status,
                   message=message)

@app.route('/velocidad', methods=['GET'])
def velocidad():
    status = "200"
    message = sim.vel()

    return jsonify(status=status,
                   message=message)

@app.route('/iniciar_vuelo', methods=['POST'])
def iniciar_vuelo():
    content = request.get_json()
    origen = Coordenada(content["lat1"], content["lon1"])
    destino = Coordenada(content["lat2"], content["lon2"])
    sim.definir_coordenadas(origen, destino)
    sim.iniciar_vuelo()
    status = "200"
    message = "OK"

    return jsonify(status=status,
                   message=message)


if __name__ == "__main__":
    app.run(host="0.0.0.0")
