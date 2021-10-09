import os
import yagmail as yagmail
from flask import Flask, render_template, flash, request
import utils
 
app = Flask(__name__)
app.secret_key = os.urandom(24)
 
@app.route('/')
def index():
    return render_template('formulario.html')
 
@app.route('/login')
def login():
    return render_template('login.html')
 
@app.route('/formRegistro', methods=('GET', 'POST'))
def formulario():
    try:
        if request.method == 'POST':
            username = request.form['username']
            password = request.form['password']
            email = request.form['correo']
            error = None
 
            if not utils.isUsernameValid(username):
                error = "El usuario debe ser alfanumerico"
                flash(error)
                return render_template('formulario.html')
 
            if not utils.isPasswordValid(password):
                error = 'La contraseña debe contener al menos una minúscula, una mayúscula, un número y 8 caracteres'
                flash(error)
                return render_template('formulario.html')
 
            if not utils.isEmailValid(email):
                error = 'Correo invalido'
                flash(error)
                return render_template('formulario.html')
 
            yag = yagmail.SMTP('earico@uninorte.edu.co','%Grupo6%')
            yag.send(to=email, subject='Activación de cuenta', contents='Bienvenido, usa este enlace para activar tu cuenta')
            flash('Revisa tu correo electrónico para activar tu cuenta')
 
        return render_template('login.html')          
    except:
        return render_template('formulario.html')