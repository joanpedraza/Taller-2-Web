const nombre=document.getElementById("name");
const apellidos=document.getElementById("apellidos");
const direccion=document.getElementById("direccion");
const telefono=document.getElementById("telefono");
const email=document.getElementById("email");
const usuario=document.getElementById("nusuario");
const password=document.getElementById("password");
const Vpassword=document.getElementById("Vpassword");
const form=document.getElementById("form");
const parrafo=document.getElementById("warnings");

const numeroBarra = document.getElementById(`numeroBarra`);
const numeroMuestra = document.getElementById(`numeroMuestra`);

form.addEventListener("submit", e => {
    e.preventDefault();
    let warnings=" ";
    let RegexEmail=/^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/;
    let entrar=false;
    let tieneMayusculas = /[A-Z]/.test(password.value);
    let tieneNumeros = /[0-9]/.test(password.value);
    let tieneLetras = /[a-zA-Z]/.test(password.value);
    let tieneCaracteresEspeciales = /[#%&/]/.test(password.value);
    let SoloNumeros = /^\d+$/;

    parrafo.innerHTML=" ";

    if (nombre.value.length <= 6) {
       warnings+='El nombre no es válido.<br>';
       entrar=true;
    }
    if (apellidos.value.length <= 6) {
        warnings+='El apellido no es válido.<br>';
        entrar=true;
     }

     if (
        !(
          direccion.value.startsWith('cll') ||
          direccion.value.startsWith('cra') ||
          direccion.value.startsWith('av')  ||
          direccion.value.startsWith('anv') ||
          direccion.value.startsWith('trans')
        )
        ){
        warnings += 'La dirección debe comenzar con al menos "cll, cra, av, anv, trans".<br>';
        entrar = true;
      }
     

    if(!SoloNumeros.test(telefono.value) && (telefono.value<10)){
        warnings+='El numero no es válido,tiene que contener solo numeros.<br>';
        entrar=true;
    }

    switch (true) {
        case !SoloNumeros.test(telefono.value):
            warnings+='El telefono tiene que contener solo numeros.<br>';
          break;
        case telefono.value.length < 10:
            warnings+='El telefono tiene que contener 10 digitos.<br>';
          break;
      }

    if(!RegexEmail.test(email.value)){
    warnings+='El email no es válido.<br>';
    entrar=true;
    }
    if(usuario.value.length<10){
        warnings+='el usuario es muy corto.<br>';
        entrar=true;
    }
    if(/[^a-zA-Z0-9]+/.test(usuario.value)){
        warnings+='el usuario no debe contener letras especiales. <br>';
        entrar=true;
    }
    if (!(tieneMayusculas && tieneNumeros && tieneLetras && tieneCaracteresEspeciales)) {
        switch (true) {
            case !tieneMayusculas:
                warnings += 'La contraseña  Debe contener al menos una letra mayúscula.<br>';
            case !tieneNumeros:
                warnings += 'La contraseña  Debe contener al menos un número.<br>';
                
            case !tieneLetras:
                warnings += 'La contraseña  Debe contener al menos una letra.<br>';
               
            case !tieneCaracteresEspeciales:
                warnings += 'La contraseña  Debe contener al menos un carácter especial (#, %, /, &).<br>';
             
            default:
                warnings += 'La contraseña no es válida.<br>';
        }
    
        entrar = true;
    }
    if(password.value.length < 15){
        warnings += 'La contraseña tiene que tener al menos 15 letras.<br>';
        entrar=true;
    }
    if(password.value!==Vpassword.value){
        warnings+='las contraseñas tienen que ser iguales. <br>'
        entrar=true;
    }

    if(entrar==true){
        parrafo.innerHTML=warnings;
    }
});

function disable(){
    document.getElementById("gustoscolor").disabled = true;
    document.getElementById("gustosmarca").disabled = true;
    document.getElementById("gustosestilo").disabled = true;
    document.getElementById("gustosmodelo").disabled = true;
}

function colordisable(){
    var a=document.getElementsByClassName("gustos");
	a[0].style.backgroundColor="#c7b68c";
}

function able(){
    document.getElementById("gustoscolor").disabled = false;
    document.getElementById("gustosmarca").disabled = false;
    document.getElementById("gustosestilo").disabled = false;
    document.getElementById("gustosmodelo").disabled = false;
}

function colorable(){
    var a=document.getElementsByClassName("gustos");
	a[0].style.backgroundColor="#ffe3b3";
}

window.onload = function () {
    slideOne();
    slideTwo();
  };
  

//Barras  
let sliderOne = document.getElementById("slider-1");
let sliderTwo = document.getElementById("slider-2");
let displayValOne = document.getElementById("range1");
let displayValTwo = document.getElementById("range2");
let minGap = 0;
let sliderTrack = document.querySelector(".slider-track");
let sliderMaxValue = document.getElementById("slider-1").max;
  
function slideOne() {
    if (parseInt(sliderTwo.value) - parseInt(sliderOne.value) <= minGap) {
    sliderOne.value = parseInt(sliderTwo.value) - minGap;
    }
    displayValOne.textContent = sliderOne.value;
    fillColor();
}
function slideTwo() {
    if (parseInt(sliderTwo.value) - parseInt(sliderOne.value) <= minGap) {
    sliderTwo.value = parseInt(sliderOne.value) + minGap;
    }
    displayValTwo.textContent = sliderTwo.value;
    fillColor();
}
function fillColor() {
    percent1 = (sliderOne.value / sliderMaxValue) * 100;
    percent2 = (sliderTwo.value / sliderMaxValue) * 100;
    sliderTrack.style.background = `linear-gradient(to right, #dadae5 ${percent1}% , #3264fe ${percent1}% , #3264fe ${percent2}%, #dadae5 ${percent2}%)`;
  }
  