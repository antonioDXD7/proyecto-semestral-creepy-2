$(document).ready(function () {
  $("#formulario_comentario").submit(function (e) {
    let mensajesMostrar = "";
    console.log(e);
    let entrar = false;

    var comentario = $("#comentario").val();
    if (comentario) {
      let entrar = false;
    }
    console.log(comentario);

    if (entrar) {
      e.preventDefault();
    } else {
      $("#mensajes").html("formulario enviado");
    }
  });

  function esMAYUSCULA(letra) {
    return letra == letra.toUpperCase();
  }
});
