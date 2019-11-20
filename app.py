from flask import Flask, request, jsonify, g
import sqlite3
from simulador import Simulador
from coordenada import Coordenada
from aeropuerto import Aeropuerto

DATABASE = './airports.db'

sim = Simulador()

app = Flask(__name__)

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
        db.row_factory = sqlite3.Row
    return db

def query_db(query, args=(), one=False):
    cur = get_db().cursor()
    cur.execute(query, args)
    rv = cur.fetchall()
    cur.close()
    return (rv[0] if rv else None) if one else rv

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

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

@app.route('/paises', methods=['GET'])
def paises():
    status = "200"
    message = []

    aero = Aeropuerto("", "", "", "", "", "", "", "", "", "", "")
    q = query_db(aero.countries_sql())

    for row in q:
        message.append(row['country'])

    return jsonify(status=status,
                   message=message)

@app.route('/aeropuertos/<string:pais>', methods=['GET'])
def aeropuerto(pais):
    status = "200"
    message = []

    aero = Aeropuerto("", "", "", "", "", "", "", "", "", "", "")
    q = query_db(aero.airports_in_country_sql(), (pais,))

    for row in q:
        aero = Aeropuerto(str(row['airport_id']), row['name'],
                    row['city'], row['country'],
                    row['iata'], row['icao'],
                    str(row['latitude']), str(row['longitude']),
                    str(row['altitude']), str(row['timezone']),
                    row['timezone_text'])
        dictionary = aero.to_dict()
        message.append(dictionary)

    return jsonify(status=status,
                   message=message)

if __name__ == "__main__":
    app.run(host="0.0.0.0")
