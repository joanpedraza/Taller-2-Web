from django import forms
from .models import Usuario

"""
"""

class usuarioRegister(forms.ModelForm):

    class Meta:
        model = Usuario

        fields = [
            'username',
            'email',
            'password',
        ]
        labels = {
            'username':'Usuario',
            'email':'Email',
            'password':'Contraseña',
        }
        widgets = {
            'username': forms.TextInput(attrs={'class':'form_control','required':''}),
            'email': forms.TextInput(attrs={'class':'form_control','required':''}),
            'password': forms.TextInput(attrs={'class':'form_control','required':''}),
        }