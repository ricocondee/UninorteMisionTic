import re
from flask import Flask, jsonify
from articulos import listaArticulos

app = Flask(__name__)

@app.route('/')
def api():
    return jsonify({'mensaje':'Hola mundo'})

@app.route('/articulos/')
def getArticulos():
    return jsonify({'lista de productos':listaArticulos})

@app.route('/articulos/<string:nombre_art>')
def getArticulo(nombre_art):
    encontrado = [item for item in listaArticulos if item['nombre'] == nombre_art]

    if len(encontrado) > 0:
        return jsonify({'Articulo':encontrado[0]})

    else:
        return jsonify({'message': 'Articulo no disponibe'})
