from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *

class PostsFormulario(forms.Form):

    titulo = forms.CharField(max_length=40)
    subtitulo = forms.CharField(max_length=40)
    cuerpo = forms.CharField(max_length=1000)
    autor = forms.CharField(max_length=40)
    fecha = forms.DateField(widget=forms.widgets.DateInput(attrs={'type': 'date'}))
    imagen = forms.ImageField()
    class Meta: #Esto es para que el formulario sepa que campos tiene que mostrar
      model = Posts
      fields = ['titulo', 'subtitulo', 'cuerpo', 'autor', 'fecha', 'imagen']

class AutoresFormulario(forms.Form):   
    nombre= forms.CharField(max_length=30)
    apellido= forms.CharField(max_length=30)
    email= forms.EmailField()    
    imagen = forms.ImageField()
    class Meta: #Esto es para que el formulario sepa que campos tiene que mostrar
      model = Autores
      fields = ['nombre', 'apellido', 'email', 'imagen']




class UserRegistrationForm(UserCreationForm):
  username = forms.CharField()
  email = forms.EmailField(required=True)
  password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
  password2 = forms.CharField(label="Confirmar contraseña", widget=forms.PasswordInput)

  last_name = forms.CharField()
  first_name = forms.CharField()
  class Meta: #Esto es para que el formulario sepa que campos tiene que mostrar
    model = User
    fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']
    help_texts={k:"" for k in fields} #Esto es para que el formulario no muestre los mensajes de ayuda

class UserEditForm(UserCreationForm):
  email = forms.EmailField(required=True)
  password1 = forms.CharField(label="Modificar Contraseña", widget=forms.PasswordInput, required=False)
  password2 = forms.CharField(label="Confirmar contraseña", widget=forms.PasswordInput, required=False)
  first_name = forms.CharField(label="Modificar Nombre")
  last_name = forms.CharField(label="Modificar Apellido") 
  

  class Meta: #Esto es para que el formulario sepa que campos tiene que mostrar
    model = User
    fields = ['email', 'password1', 'password2', 'first_name', 'last_name']
    help_texts={k:"" for k in fields} #Esto es para que el formulario no muestre los mensajes de ayuda    


class Perfil(forms.Form):   
    username = models.OneToOneField(User, on_delete=models.CASCADE)
    email= forms.EmailField()    
    
    class Meta: #Esto es para que el formulario sepa que campos tiene que mostrar
      model = User
      fields = ['first_name', 'last_name', 'email']   