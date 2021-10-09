import os
 
import yagmail as yagmail
from flask import Flask, render_template, flash, request, redirect, url_for, jsonify
import utils
 
from message import mensajes
 
app = Flask( __name__ )
app.secret_key = os.urandom( 24 )
 
 
@app.route( '/' )
def index():
    return render_template( 'formulario.html' )
 
@app.route( '/register', methods=('GET', 'POST') )
def register():
    try:
        if request.method == 'POST':
            username = request.form['username']
            password = request.form['password']
            email = request.form['correo']
            error = None
 
            if not utils.isUsernameValid( username ):
                error = "El usuario debe ser alfanumerico o incluir solo '.','_','-'"
                flash( error )
                return render_template( 'formulario.html' )
 
            if not utils.isPasswordValid( password ):
                error = 'La contraseña debe contenir al menos una minúscula, una mayúscula, un número y 8 caracteres'
                flash( error )
                return render_template( 'formulario.html' )
 
            if not utils.isEmailValid( email ):
                error = 'Correo invalido'
                flash( error )
                return render_template( 'formulario.html' )
 
            # yag = yagmail.SMTP('micuenta@gmail.com', 'clave') #modificar con tu informacion personal
            # yag.send(to=email, subject='Activa tu cuenta',
            #        contents='Bienvenido, usa este link para activar tu cuenta ')
            flash( 'Revisa tu correo para activar tu cuenta' )
            return render_template( 'login.html' )
        return render_template( 'login.html' )
    except:
        return render_template( 'formulario.html' )
 
 
@app.route( '/login', methods=['get', 'post'])
def login():
 
    try:
        if request.method == 'POST':
            username = request.form['username']
            password = request.form['password']
 
            if not username:
                error = 'Debe ingresar el usuario'
                flash(error)
                return render_template('login.html')
 
            if not password:
                error = 'La contraseña es requerida'
                flash(error)
                return render_template('login.html')
 
            if username == 'Prueba' and password == 'Prueba123':
                return redirect('mensaje')
 
            else:
                error = 'El usuario o contraseña ingresado no son correctos'
                flash(error)
                return render_template('login.html')
 
        return render_template('login.html')
    except:
        return render_template('login.html')
 
@app.route('/mensaje')
def message():
    return jsonify({'Mensajes': mensajes})
 
@app.route( '/mensaje/<string:usuario>')
def getusuario(usuario):
    encontrado = [item for item in mensajes if item['usuario'] == usuario]
    if len(encontrado) > 0:
        return jsonify({'mensaje':encontrado[0]})
    return 'El usuario no exite'
 
 
if __name__ == '__main__':
    app.run(debug=True)