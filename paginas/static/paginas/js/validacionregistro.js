//jquery//

$(document).ready(function () {
  $("#registrof").submit(function (e) {
    let mensajesMostrar = "";
    let entrar = false;

    var nombre = $("#nombreregistro").val();
    if (nombre.trim().length < 3 || nombre.trim().length > 9) {
      mensajesMostrar +=
        "La longitud del nombre no es correcto(min 4 y max 9) <br>";
      entrar = true;
    }

    //trim le quita los espacios en blanco//

    var letrainicial = nombre.charAt(0);
    if (!esMAYUSCULA(letrainicial)) {
      mensajesMostrar += "La primera letra del nombre es minuscula <br>";
      entrar = true;
    }

    var apellido = $("#apellidoregistro").val();
    if (apellido.trim().length < 3 || apellido.trim().length > 9) {
      mensajesMostrar +=
        "La longitud del apellido no es la correcta(min 3 y max 12) <br>";
      entrar = true;
    }

    var letrainicial1 = apellido.charAt(0);
    if (!esMAYUSCULA(letrainicial1)) {
      mensajesMostrar += "La primera letra del apellido es minuscula <br>";
      entrar = true;
    }

    var correoderegistro = $("#registrocorreo").val();
    if (correoderegistro.trim().length < 8) {
      mensajesMostrar += "El correo debe tener minimo 8 caracteres <br>";
      entrar = true;
    }

    var contraseña = $("#contraseñaregistro").val();
    if (contraseña.trim().length < 8) {
      mensajesMostrar += "La contraseña debe tener minimo 8 caracteres <br>";
      entrar = true;
    }

    var letrainicial2 = contraseña.charAt(0);
    if (!esMAYUSCULA(letrainicial2)) {
      mensajesMostrar +=
        "La primera letra de la contraseña debe de ser una letra mayuscula<br>";
      entrar = true;
    }

    var contraseñaconfirmar = $("#confirmarcontraseñaregistro").val();
    if (contraseñaconfirmar != contraseña) {
      mensajesMostrar += "Las contraseñas no coinciden <br>";
      entrar = true;
    }

    if (entrar) {
      console.log("entrar");
      e.preventDefault();
      $("#mensajes").html(mensajesMostrar);
    } else {
      console.log("else");
      $("#mensajes").html("formulario enviado");
    }
  });

  function esMAYUSCULA(letra) {
    return letra == letra.toUpperCase();
  }
});
