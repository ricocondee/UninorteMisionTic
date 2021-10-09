from flask import Flask, render_template, request, redirect, url_for, flash
import sqlite3

app = Flask(__name__)

app.secret_key = 'secretkey'


def sql_connection():
    con = sqlite3.connect('agenda.db')
    return con


@app.route("/")
def index():
    con = sql_connection()
    cur = con.cursor()
    cur.execute('SELECT * FROM contactos')
    data = cur.fetchall()
    print(data)
    return render_template('index.html', data=data )


@app.route("/add", methods=['POST'])
def add_contact():
    if request.method == 'POST':
        fullname = request.form['fullname']
        email = request.form['email']
        phone = request.form['phone']
        con = sql_connection()
        cur = con.cursor()
        consulta = 'INSERT INTO contactos (fullname, email, phone) VALUES (?,?,?)'
        cur.execute(consulta, [fullname, email, phone])
        con.commit()
        flash('Contact Added Successfully')
    return redirect(url_for('index'))


@app.route("/edit")
def edit_contact():
    return 'editar contacto'


@app.route("/delete")
def delete_contact():
    return 'eliminar contacto'
