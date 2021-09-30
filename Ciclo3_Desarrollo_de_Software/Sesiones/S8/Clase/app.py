from flask import Flask

app = Flask(__name__)

@app.route('/')

def saludo():
    return "Hola mundo Flask"