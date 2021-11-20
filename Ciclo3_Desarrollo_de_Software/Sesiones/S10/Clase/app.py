from flask import Flask, render_template
from flask_wtf import FlaskForm
from flask_wtf.recaptcha.fields import RecaptchaField
from wtforms import StringField, PasswordField
from wtforms.validators import InputRequired, Length, AnyOf

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secretkey'
app.config['RECAPTCHA_PUBLIC_KEY'] = '6LeGf7UcAAAAACatzblQovVOBNMtcopc2RvwIRIH'
app.config['RECAPTCHA_PRIVATE_KEY'] = '6LeGf7UcAAAAAKH8H4K44i7l8Qnay9KAe8Kz9JFf'

@app.route('/', methods=['GET', 'POST'])
def form():
    form = login_form()
    if form.validate_on_submit():
        return f"<h2>El usuario ingresado es: {form.username.data}. La contraseña es {form.password.data}</h2>"
    return render_template('formulario.html', form=form)

class login_form(FlaskForm):
    username = StringField('username', validators=[InputRequired('El usuario es requerido'), Length(min=5, max=15, message='El usuario debe tener entre 5 y 10 caracteres')])
    password = PasswordField('password', validators=[InputRequired('El Password es requerido'), AnyOf(values=['pass','secret','xxxxx'], message='Password no válido')])

    """ recaptcha = RecaptchaField() """

if __name__ == '__main__':
    app.run(debug=True)