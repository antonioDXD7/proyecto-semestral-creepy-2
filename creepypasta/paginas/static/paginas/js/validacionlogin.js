$(document).ready(function () {

    $("#login1").submit(function (e) {

        e.preventDefault();
        let mensajesMostrar = "";
        let entrar = false;



        var contraseñalogin = $("#contraseñalogin").val();
        if (contraseñalogin.trim().length < 8) {
            mensajesMostrar += "La contraseña debe tener minimo 8 caracteres <br>"
            entrar = true;
        }

        var letrainicial = contraseñalogin.charAt(0);
        if (!esMAYUSCULA(letrainicial)) {
            mensajesMostrar += "La primera letra de la contraseña debe de ser  mayuscula<br>"
            entrar = true;
        }


        var logincorreo = $("#logincorreo").val();
        if (logincorreo.trim().length < 8) {
            mensajesMostrar += "El correo debe tener minimo 8 caracteres <br>"
            entrar = true;
        }

        var letrainicial2 = logincorreo.charAt(0);
        if (!esMAYUSCULA(letrainicial2)) {
            mensajesMostrar += "La primera letra del correo debe de ser una  mayuscula<br>"
            entrar = true;
        }

        

        


        












        if (entrar) {
            $("#mensajes").html(mensajesMostrar);
        }
        else {
            $("#mensajes").html("formulario enviado");
        }


    });


    function esMAYUSCULA(letra) {
        return letra == letra.toUpperCase()
    }

})