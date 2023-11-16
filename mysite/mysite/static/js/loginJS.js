$(function(){
    $("#login").click(function(){
        var username = $("#username").val();
        var password = $("#password").val();
        if(username == "" || password == ""){
            alert("¡El nombre de usuario o la contraseña no pueden estar vacíos!");
        }else{
            $.ajax({
                type: "POST",
                url: "/login",
                data: {
                    "username": username,
                    "password": password
                },
                dataType: "json",
                success: function(data){
                    if(data.status == 200){
                        window.location.href = "/index";
                    }else{
                        alert(data.msg);
                    }
                },
                error: function(jqXHR){
                    alert("Ocurrió un error:" + jqXHR.status);
                }
            })
        }
    })

})