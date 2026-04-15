document.getElementById("btn_iniciar-sesion").addEventListener("click", IniciarSesion);
document.getElementById("btn_registrarse").addEventListener("click", registro);
window.addEventListener("resize", anchoPagina);

//declaracion variables
var Contenedor_LoginRegistro = document.querySelector(".contenedor__login-registro");
    var formularioLogin = document.querySelector(".formulario__login");
    var formularioRegistro = document.querySelector(".formulario__Registro");
    var cajaIzquierdaLogin = document.querySelector(".caja__Izquierda-Login");
    var cajaDerechaRegistro = document.querySelector(".caja__Derecha-Registro");

    function anchoPagina(){
        if(window.innerWidth > 850){
            cajaIzquierdaLogin.style.display="block";
            cajaDerechaRegistro.style.display= "block";
        }
        else{
            cajaDerechaRegistro.style.display= "block";
            cajaDerechaRegistro.style.opacity= "1";
            cajaIzquierdaLogin.style.display="none";
            formularioLogin.style.display="block";
            formularioRegistro.style.display= "none";
            Contenedor_LoginRegistro.style.left= "0px";
        }
    }
anchoPagina();

    function IniciarSesion(){

        if(window.innerWidth > 850){
        formularioRegistro.style.display = "none";
        Contenedor_LoginRegistro.style.left = "10px";
        formularioLogin.style.display= "block";
        cajaDerechaRegistro.style.opacity = "1";
        cajaIzquierdaLogin.style.opacity = "0";
    }else{
        formularioRegistro.style.display = "none";
        Contenedor_LoginRegistro.style.left = "0px";
        formularioLogin.style.display= "block";
        cajaDerechaRegistro.style.display = "block";
        cajaIzquierdaLogin.style.display = "none";
    }
}
function registro(){
    if(window.innerWidth > 850){
    formularioRegistro.style.display = "block";
    Contenedor_LoginRegistro.style.left = "410px";
    formularioLogin.style.display= "none";
    cajaDerechaRegistro.style.opacity = "0";
    cajaIzquierdaLogin.style.opacity = "1";
}else{
        formularioRegistro.style.display = "block";
        Contenedor_LoginRegistro.style.left = "0px";
        formularioLogin.style.display= "none";
        cajaDerechaRegistro.style.display = "none";
        cajaIzquierdaLogin.style.display = "block";
        cajaIzquierdaLogin.style.opacity = "1";
    }
}