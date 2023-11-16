from django.contrib import messages
from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.template import loader
from .models import Usuario, Juegos

# Create your views here.

def login(request):
    template = loader.get_template("usuarios/login.html")
    context = {}
    return HttpResponse(template.render(context, request))

def register(request):
    template = loader.get_template("usuarios/register.html")
    context = {}
    return HttpResponse(template.render(context, request))

def forgot(request):
    template = loader.get_template("usuarios/Forgot.html")
    context = {}
    return HttpResponse(template.render(context, request))

def hangman(request,nombre):
    usuario = Juegos.objects.get(username=nombre)
    return render(request, "usuarios/hangman.html", {"user": usuario})

def pong(request,nombre):
    usuario = Juegos.objects.get(username=nombre)
    return render(request, "usuarios/pong.html", {"user": usuario})

def tictactoe(request,nombre):
    usuario = Juegos.objects.get(username=nombre)
    return render(request, "usuarios/tictactoe.html", {"user": usuario})

def snake(request):
    template = loader.get_template("usuarios/snake.html")
    context = {}
    return HttpResponse(template.render(context, request))

def menuC(request,nombre):
    if request.method == "POST":
        
        puntajeH = request.POST['hangmanScore']
        puntajeP = request.POST['pongScore']

        usuario = Juegos.objects.get(username=nombre)

        #Pong
        if puntajeP == '':
            #return render(request, "usuarios/menu.html", {"user":usuario}) 
            puntajePn = usuario.pongScore 
        else:
            if int(puntajeP) > usuario.pongScore:
                puntajePn = int(puntajeP)
            else:
                puntajePn = usuario.pongScore    

        #Hangman        
        if puntajeH == '':
            puntajeHn = usuario.hangmanScore
        else:
            puntajeHn = int(puntajeH)
              
        #usuario.username = nombre
        #usuario.snakeScore = 0
        #usuario.tictacX = 0
        #usuario.tictac0 = 0
        usuario.pongScore = puntajePn
        usuario.hangmanScore = puntajeHn

        usuario.save()
        return render(request, "usuarios/menu.html", {"user":usuario})    
    else:
        return render(request, "usuarios/pong.html")


def backMenu(request):
    template = loader.get_template("usuarios/menu.html")
    context = {}
    return HttpResponse(template.render(context, request))       

def nuevo_usuario(request):
    if request.method == "POST":
        usuario = request.POST['username']
        email =  request.POST['email']
        contrasena = request.POST['password']
        usuarioU = Usuario(username=usuario,email=email,password=contrasena)
        usuarioU.save()

        usuarioPlay = Juegos(username=usuario,snakeScore=0,tictacX=0,tictac0=0,pongScore=0,hangmanScore=0)
        usuarioPlay.save()
        return HttpResponseRedirect('/')
    else: 
        return render(request, "usuarios/register.html")
    
def pagLogin(request):
    if request.method == "POST":
        try:
            xusuario = Usuario.objects.get(username=request.POST['username'], password=request.POST['password'])
            xuser = Juegos.objects.get(username=request.POST['username'])
            print("Usuario=", xusuario)
            #request.session['username'] = xusuario.username
            #request.session['password'] = xusuario.password
            
            return render(request, "usuarios/menu.html", {"user": xuser})

        except Usuario.DoesNotExist as e:
            messages.success(request, 'Credenciales incorrectas, intentalo denuevo!')
    template = loader.get_template("usuarios/login.html")
    context = {}
    return HttpResponse(template.render(context, request))    

