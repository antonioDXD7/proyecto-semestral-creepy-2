//jquery//

$(document).ready(function () {

    $("#subirmensaje").submit(function (e) {

        
        let mensajesMostrar = "";
        let entrar = false;



        var mensajecreepy1 = $("#motivocreepycrear").val();
        if (mensajecreepy1.trim().length < 4 || mensajecreepy1.trim().length > 20) {
            mensajesMostrar += "El motivo debe tener minimo 4 letras max 20 <br>"
            entrar = true;
        }

        var letrainicial2 = mensajecreepy1.charAt(0);
        if (!esMAYUSCULA(letrainicial2)) {
            mensajesMostrar += "La primera letra del nombre debe de ser una  mayuscula<br>"
            entrar = true;
        }

        


        var motivocreepy = $("#mensajecreepy").val();
        if (motivocreepy.trim().length < 20 || motivocreepy.trim().length > 150) {
            mensajesMostrar += "El mensaje debe tener minimo 20 letras max 150 <br> "
            +"sin repetir bastante una palabras tipo :aaaaaaaaa o palapalapalapala "
            +"si un admi ve esto su historia sera inmediatamente eliminada<br>"
            entrar = true;
        }

        //trim le quita los espacios en blanco//

        var letrainicial = motivocreepy.charAt(0);
        if (!esMAYUSCULA(letrainicial)) {
            mensajesMostrar += "La primera letra del mensaje  es minuscula <br>"
            entrar = true;
        }
        

    













        if (entrar) {
            $("#mensajesc").html(mensajesMostrar);
            e.preventDefault();
        }
        else {
            $("#mensajesc").html("creepypasta enviado");
        }


    });


    function esMAYUSCULA(letra) {
        return letra == letra.toUpperCase()
    }

})