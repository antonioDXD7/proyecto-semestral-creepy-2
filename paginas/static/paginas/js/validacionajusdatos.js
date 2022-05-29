//jquery//

$(document).ready(function () {

    $("#ajustedatoscuenta").submit(function (e) {

        e.preventDefault();
        let mensajesMostrar1 = "";
        let entrar1 = false;



        var cambionombres = $("#cambionombre").val();
        if (cambionombres.trim().length < 3 || cambionombres.trim().length > 9) {
            mensajesMostrar1 += "El nombre debe tener minimo 3 letras max 9 <br>"
            entrar1 = true;
        }

        //trim le quita los espacios en blanco//

        var letrainicial = cambionombres.charAt(0);
        if (!esMAYUSCULA(letrainicial)) {
            mensajesMostrar1 += "La primera letra del nombre es minuscula <br>"
            entrar1 = true;
        }

        var cambioapellido = $("#cambioapellido").val();
        if (cambioapellido.trim().length < 3 || cambioapellido.trim().length > 9) {
            mensajesMostrar1 += "El apellido debe tener minimo 3 letras max 9 <br>"
            entrar1 = true;
        }

        var letrainicial1 = cambioapellido.charAt(0);
        if (!esMAYUSCULA(letrainicial1)) {
            mensajesMostrar1 += "La primera letra del apellido es minuscula <br>"
            entrar1 = true;
        }

    

      

        var nuevocorreo = $("#nuevoscorreo").val();
        if (nuevocorreo.trim().length < 8) {
            mensajesMostrar1 += "El correo debe tener minimo 8 caracteres <br>"
            entrar1 = true;
        }


        
    
        var confirmarnuevocorreo = $("#confirmarnuevocorreo").val();
        if (confirmarnuevocorreo != nuevocorreo ){
           mensajesMostrar1 += "Los correos no coinciden <br>" 
           entrar1 = true;
        }


        var confirmarcontraseña2 = $("#ingresarcontraseña").val();
        if (confirmarcontraseña2.trim().length < 8) {
            mensajesMostrar1 += "la contraseña debe tener minimo 8 caracteres <br>"
            entrar1 = true;
        }

        var letrainicial3 = confirmarcontraseña2.charAt(0);
        if (!esMAYUSCULA(letrainicial3)) {
            mensajesMostrar1 += "la primera letra debe de ser una letra mayuscula<br>"
            entrar1 = true;
        }

        
    
        var contraseñaconfirmar3 = $("#confirmarconcontraseña").val();
        if (contraseñaconfirmar3 != confirmarcontraseña2 ){
           mensajesMostrar1 += "las contraseñas no coinciden <br>" 
           entrar1 = true;
        }













        if (entrar1) {
            $("#mensajes").html(mensajesMostrar1);
        }
        else {
            $("#mensajes").html("Formulario enviado y datos cambiados");
        }


    });


    function esMAYUSCULA(letra) {
        return letra == letra.toUpperCase()
    }

})