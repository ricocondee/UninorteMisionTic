from flask import Flask
from flask.templating import render_template

app = Flask(__name__)

@app.route('/')
def saludo():
    return "Buenos dias, ya estamos en el tercer trimestre"

@app.route('/articulos/')
def articulos():
    return "lista de articulos en promocion  "

@app.route('/articulos/<int:id>')
def verArticulos(id):
    return f"Estamos viendo el articulo con el id {id}."

@app.route('/productos/<string:ref>')
def productos(ref):
    dic = {'p1':'calzado', 'p2':'camisas', 'p3':'pantalones'}
    return f"El producto seleccionado es {dic[ref]}"

@app.route('/saludo/')
@app.route('/saludo/<string:name>')
@app.route('/saludo/<string:name>/<int:age>')
def saludos(age = None, name = None):
    if name and age:
        return f"Hola, {name} tienes {age} años."
    elif name:
        return f"Hola {name}."
    else:
        return f"Hola."

if __name__ == "__main__":
    app.run(debug=True)