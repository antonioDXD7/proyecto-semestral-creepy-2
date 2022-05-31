$(document).ready(function () {
  $("#login1").submit(function (e) {
    let mensajesMostrar = "";
    let entrar = false;

    var contraseñalogin = $("#contraseñalogin").val();
    if (contraseñalogin.trim().length < 8) {
      mensajesMostrar += "La contraseña debe tener minimo 8 caracteres <br>";
      entrar = true;
    }

    var letrainicial = contraseñalogin.charAt(0);

    var logincorreo = $("#logincorreo").val();
    if (logincorreo.trim().length < 8) {
      mensajesMostrar += "El correo debe tener minimo 8 caracteres <br>";
      entrar = true;
    }

    var letrainicial2 = logincorreo.charAt(0);

    if (entrar) {
      $("#mensajes").html(mensajesMostrar);
      e.preventDefault();
    } else {
      $("#mensajes").html("formulario enviado");
    }
  });

  function esMAYUSCULA(letra) {
    return letra == letra.toUpperCase();
  }
});
