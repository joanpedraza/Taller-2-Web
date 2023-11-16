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

def snake(request,nombre):
    usuario = Juegos.objects.get(username=nombre)
    return render(request, "usuarios/snake.html", {"user": usuario})

def menuC(request,nombre):
    if request.method == "POST":
        
        puntajeH = request.POST['hangmanScore']
        puntajeP = request.POST['pongScore']
        puntajeX = request.POST['ticXScore']
        puntajeO = request.POST['tic0Score']
        puntajeS = request.POST['snakeScore']

        usuario = Juegos.objects.get(username=nombre)

        #Pong
        if puntajeP == '':
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
            puntajeHn = int(puntajeH) + usuario.hangmanScore
            
        #TictacToe
        if puntajeX == '':
            puntajeX = usuario.tictacX
        else:
            puntajeX = int(puntajeX) + usuario.tictacX
            
        if puntajeO == '':
            puntajeO = usuario.tictac0
        else:
            puntajeO = int(puntajeO) + usuario.tictac0   
            
        #Snake     
        if puntajeS == '':
            puntajeS = usuario.snakeScore
        else:
            if int(puntajeS) > usuario.snakeScore:
                puntajeS = int(puntajeS)
            else:
                puntajeS = usuario.snakeScore    
              
        #usuario.username = nombre
        usuario.snakeScore = puntajeS
        usuario.tictacX = puntajeX
        usuario.tictac0 = puntajeO
        usuario.pongScore = puntajePn
        usuario.hangmanScore = puntajeHn

        usuario.save()
        
        return render(request, "usuarios/menu.html", {"user":usuario})    
    else:
        return render(request, "usuarios/menu.html")


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

