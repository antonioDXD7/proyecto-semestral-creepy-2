//jquery//

$(document).ready(function () {

    $("#ajustecontraseña").submit(function (e) {

        e.preventDefault();
        let mensajesMostrar = "";
        let entrar = false;


        var nuevacontraseña = $("#nuevacontraseña").val();
        if (nuevacontraseña.trim().length < 8) {
            mensajesMostrar += "La nueva contraseña debe tener minimo 8 caracteres <br>"
            entrar = true;
        }

        var letrainicial = nuevacontraseña.charAt(0);
        if (!esMAYUSCULA(letrainicial)) {
            mensajesMostrar += "La primera letra de la nueva debe de tener una mayuscula<br>"
            entrar = true;
        }

        
    
        var confirmarnuevacontraseña = $("#confirmarnuevacontraseña").val();
        if (confirmarnuevacontraseña != nuevacontraseña ){
           mensajesMostrar += "Las nuevas contraseñas no coinciden <br>" 
           entrar = true;
        }


        var contraseña = $("#contraseña2").val();
        if (contraseña.trim().length < 8) {
            mensajesMostrar += "La contraseña debe tener minimo 8 caracteres <br>"
            entrar = true;
        }

        var letrainicial1 = contraseña.charAt(0);
        if (!esMAYUSCULA(letrainicial1)) {
            mensajesMostrar += "La primera letra de la contraseña debe de ser una  mayuscula<br>"
            entrar = true;
        }

        
    
        var contraseñaconfirmar = $("#confirmarcontraseña").val();
        if (contraseñaconfirmar != contraseña ){
           mensajesMostrar += "Las contraseñas no coinciden <br>" 
           entrar = true;
        }
        


        












        if (entrar) {
            $("#mensajes").html(mensajesMostrar);
        }
        else {
            $("#mensajes").html("formulario enviado y contraseña cambiada");
        }


    });


    function esMAYUSCULA(letra) {
        return letra == letra.toUpperCase()
    }

})