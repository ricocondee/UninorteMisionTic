#importaciones
from flask import Flask, render_template, request, redirect, url_for, flash
import sqlite3

app = Flask(__name__)

app.secret_key = 'secretkey'


def sql_connection():#funcion para conectar conla base de datos
    con = sqlite3.connect('agenda.db')#conexion con la base de datos
    return con


@app.route("/")#ruta raiz 
def index():#su funcion
    con = sql_connection()#llamado de la funcion que conecta la base de datos
    cur = con.cursor()
    cur.execute('SELECT * FROM contactos')#query consult
    data = cur.fetchall()#traer todo
    print(data)
    return render_template('index.html', data=data )


@app.route("/add", methods=['POST'])#ruta para agregar contacto
def add_contact():#su funcion
    if request.method == 'POST':#si el metodo es post haz lo siguiente 
        fullname = request.form['fullname']#trae el valor ingresado en el campo fullname
        email = request.form['email']#------" " " " "  "  "      "  "" "" "   " email
        phone = request.form['phone']#------" " " " "  "  "      "  "" "" "   " Phone
        con = sql_connection()
        cur = con.cursor()
        sqlrt = 'INSERT INTO contactos (fullname, email, phone) VALUES (?,?,?)'#query consult
        cur.execute(sqlrt, [fullname, email, phone])#execute query
        con.commit()#Guarda los cambios
        flash('Contact Added Successfully')#mensaje al usuario
    return redirect(url_for('index'))


@app.route("/edit/<int:id>", methods=['POST', 'GET'])#funcion para agregar contacto
def edit_contact(id):#su funcion
    con = sql_connection()
    cur = con.cursor()
    sqlrt = 'SELECT * FROM contactos WHERE id = ?'
    cur.execute(sqlrt, [id])
    con.commit()
    data = cur.fetchone()
    return render_template('edit.html', data=data)

@app.route("/update/<int:id>", methods=['POST','GET'])#ruta para actuaizar contacto
def update_contact(id):#su funcion
    if request.method == 'POST':
        con = sql_connection()
        fullname = request.form['fullname']
        email = request.form['email']
        phone = request.form['phone']
        cur = con.cursor()
        sqlrt = 'UPDATE contactos SET fullname = ?, email = ?, phone = ? WHERE id = ?'
        cur.execute(sqlrt, [fullname, email, phone, id])
        con.commit()
        flash('contact updated succesfully')
    return redirect(url_for('index'))




@app.route("/delete/<int:id>", methods=['POST', 'GET'])#ruta para eliminar contacto
def delete_contact(id):#su funcion
    con = sql_connection()
    cur = con.cursor()
    cur.execute(f'DELETE FROM contactos WHERE id = {id}')
    con.commit()
    flash('Contact Deleted Succesfully')
    return redirect(url_for('index'))
