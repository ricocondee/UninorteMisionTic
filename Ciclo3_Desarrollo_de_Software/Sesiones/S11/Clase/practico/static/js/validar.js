/* function validateForm() {
    //1. Accedemos a los elementos del formulario.
    var user = document.getElementById('username');
    var email = document.getElementById('email');
    var password = document.getElementById('password');
    var message = "";

    //2. Alicar validaciones.
    if (!user.checkValidity()) {
        message += "Usuario requerido con longitud minima de 8 caracteres.";
    }

    if (!email.checkValidity()) {
        message += "Correo requerido con formato @gmail.com .";
    }

    if (!password.checkValidity()) {
        message += "Contraseña requerida con longitud minima de 8 caracteres.";
    }

    if (message == "") {
        message = "Todos los campos son validos.";
    }
    alert(message);
} */

function showPassword() {
    if (document.getElementById('btn').checked) {
        var obj = document.getElementById("password");
        obj.type = "text";
    }

    else{
            var obj = document.getElementById("password");
            obj.type = "password";
        }
}