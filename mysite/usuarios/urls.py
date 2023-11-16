from django.urls import path
from . import views

urlpatterns = [
    path('', views.login, name='login'),
    path('usuario/', views.register, name="register"),
    path('forgot/', views.forgot, name="forgot"),
    path('nuevoUsuario/', views.nuevo_usuario),
    path('login/', views.pagLogin, name="pagLogin"),

    path('hangman/<str:nombre>/', views.hangman, name="hangman"),
    path('pong/<str:nombre>/', views.pong),
    path('tictactoe/<str:nombre>/', views.tictactoe, name="tictactoe"),
    path('menu/snake/', views.snake, name="snake"),
    path('menu/<str:nombre>/', views.menuC),

    path('menu/', views.backMenu, name="menu"),
]
