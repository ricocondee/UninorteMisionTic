import os
from werkzeug.utils import redirect
import yagmail as yagmail
from flask import Flask, render_template, flash, request, jsonify, session, url_for, g
import utils
import functools
from message import mensajes
from db import getDb
from werkzeug.security import generate_password_hash, check_password_hash 
from formulario import Contactenos

app = Flask(__name__)
app.secret_key = os.urandom(24)


@app.route('/')
def index():
    return render_template('formulario.html')


@app.route('/register', methods=('GET', 'POST'))
def register():
    try:
        error = None
        if request.method == 'POST':
            name = request.form['name']
            users = request.form['username']
            passw = request.form['password']
            eMail = request.form['email']
            if not utils.isUsernameValid(users):
                error = "El usuario debe ser alfanumerico."
                flash(error)
                print("error 1")
                return render_template('formulario.html')
            if not utils.isEmailValid(eMail):
                error = "El email no es valido"
                flash(error)
                print("error 2")
                return render_template('formulario.html')

            if not utils.isPasswordValid(passw):
                error = "La contraseña debe tener por lo menos un numero, una mayuscula, minusculas y un caracter especial"
                flash(error)
                print("error 3")
                return render_template('formulario.html')

            """ yag = yagmail.SMTP("correofalso@gmail.com","contraseñaDeCorreoFalso")
            yag.send(to=eMail, subject="Activate succesfully")
            flash("Revisa tu correo para activar tu cuenta") """


            passw = generate_password_hash(passw)
            db = getDb()
            cur = db.cursor()
            cur.executescript("INSERT INTO usuario (nombre, usuario, correo, contraseña) VALUES('%s', '%s', '%s', '%s')" % (name, users, eMail, passw))
            db.commit()

        return render_template('login.html')
    except:
        return render_template('formulario.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    try:
        if request.method == 'POST':
            username = request.form['username']
            password = request.form['password']

            if not username and not password:
                error = "Debe llenar ambos campos"
                flash(error)
                return render_template('login.html')

            elif not username:
                error = "Debe ingresar un usuario"
                flash(error)
                return render_template('login.html')

            elif not password:
                error = "Debe ingresar una contraseña"
                flash(error)
                return render_template('login.html')

            db = getDb()
            cur = db.cursor()
            cur.execute(
                'SELECT * FROM usuario WHERE usuario = ?', (username))
            cur = cur.fetchone()

            if cur is None:
                error = "Usuario o Contraseña invalidas"

            else:
                if check_password_hash(cur[4], password):
                    session.clear()
                    session['user_id'] = cur[0]
                    return redirect(url_for('message'))
                else:
                    error = 'contraseña invalida'
                    
            flash(error)
            return render_template('login.html')
        return render_template('login.html')
    except:
        return render_template('login.html')


@app.route('/mensaje/', methods=['GET', 'POST'])
def message():
    return jsonify({'mensaje': mensajes})

def loginRequired(f):
    functools.wraps(f)
    def auth():
        if g.user is None:
            return redirect(url_for('login'))
        return f
    return auth()

@app.route('/send', methods=['GET', 'POST'])
@loginRequired
def send():
    if request.method == 'POST':
        form_id = g.user['id']
        to_username = request.form['for']
        subject = request.form['subject']
        body = request.form['message']

        if not to_username or not subject or not body:
            error = "campos requeridos"
            flash(error)
            return render_template('send.html')




@app.route('/user/<string:user>')
def getUser(user):
    finded = [item for item in mensajes if item['usuario'] == user]
    if len(finded) > 0:
        return jsonify({'usuario': finded[0]})
    else:
        return "El usuario no existe"

@app.route('/contactos', methods=['GET', 'POST'])
def contactos():
    form = Contactenos()
    return render_template('contacto.html')

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login'))
