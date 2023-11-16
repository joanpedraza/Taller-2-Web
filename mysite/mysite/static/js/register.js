/**
 * Initializes the registration page.
 * @function
 */
$(function(){
    // Agregar evento de escucha al formulario de registro
    $("#login").click(function(){
        
        var data = {
            name: $('#name').val(),
            email: $('#email').val(),
            password: $('#password').val(),
            confirm_password: $('#confirm_password').val()  
        };

        
        if (data.name === '' || data.email === '' || data.password === '') {
            alert('Por favor, complete todos los campos.');
            return;
        }

        if (!isValidEmail(data.email)) {
            alert('Por favor, ingrese un correo electrónico válido.');
            return;
        }
        if (password !== confirm_password) {
            alert('Las contraseñas no coinciden. Por favor, inténtelo de nuevo.');
            return;
        }

        // Enviar los datos a la base de datos utilizando AJAX
        $.ajax({
            url: 'url_de_la_base_de_datos',
            type: 'POST',
            data: JSON.stringify(data),
            contentType: 'application/json',
            success: function(response) {
                // Enviar una respuesta al usuario indicando si la operación fue exitosa o no
                alert('Registro exitoso!');
            },
            error: function(error) {
                alert('Error al registrar. Por favor, inténtelo de nuevo más tarde.');
            }
        });
    });

    // Función para verificar si un correo electrónico es válido
    function isValidEmail(email) {
        // Expresión regular para verificar si el correo electrónico es válido
        var emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        return emailRegex.test(email);
    }
});  
