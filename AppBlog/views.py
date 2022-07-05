from django.shortcuts import render, HttpResponse
from django.template import loader
from django.http import HttpResponse
from .models import *
from django.views.generic import ListView, TemplateView
from AppBlog.forms import *
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from .forms import *

# Login
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib import messages


# Create your views here.



def inicio(request):
    posts = Posts.objects.all
    return render(request, "AppBlog/inicio.html", {"posts": posts}) 


def posts(request):
    return render(request, "AppBlog/posts.html", {"posts": posts})


def autores(request):
    return render(request, "AppBlog/autores.html", {"autores": autores})

def nosotras(request):

    return render(request, "AppBlog/nosotras.html")    



#Acá viene el LOGIN Y REGISTRO    

def login_request(request):
  if  request.method == "POST":
    form = AuthenticationForm(request, data=request.POST)
    if form.is_valid():
      username = form.cleaned_data.get("username")
      password = form.cleaned_data.get("password")
      usuario = authenticate(username=username, password=password)
      if usuario is not None:
        login(request, usuario)
        messages.success(request, f"Bienvenido {username}")
        login(request, usuario)
        return redirect('inicio')
      else:
        messages.error(request, "Los datos son incorrectos")
    else:
      messages.error(request, "Los datos son incorrectos")


  form = AuthenticationForm()
  return render(request, 'AppBlog/login.html', {'form': form})



def registro(request):
  data ={
      'form' : UserRegistrationForm()
  }
  if request.method == 'POST': # Si es POST, entonces es un formulario que viene lleno
    form = UserRegistrationForm(request.POST)
    if form.is_valid():
      #username = form.cleaned_data['username']
      form.save()
      usuario = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password1'])
      login(request, usuario)
      messages.success(request, f'{usuario} Te has registrado correctamente')
      return redirect(to='inicio')
    data['form'] = form
  return render(request,'AppBlog/registro.html', data)


@login_required()
def editarPerfil(request):

    usuario = request.user

    if request.method == "POST":
        form = UserEditForm(request.POST)

        if form.is_valid():
            data = form.cleaned_data
            usuario.first_name = data["first_name"]
            usuario.last_name=data["last_name"]
            usuario.email = data["email"]
            usuario.password1 = data["password1"]
            usuario.password2 = data["password2"]
            usuario.save()
            return redirect("inicio")
            messages.success(request, "El perfil fue editado correctamente")
        else:
           
         
          form = UserEditForm(initial={"email":usuario.email})
        return render(request, 'AppBlog/editar_perfil.html', {"title": "Editar usuario", "message": "Editar usuario", "form": form, "errors": ["Datos inválidos"]}) 
    
    else:
        form = UserEditForm(initial={"email":usuario.email})
        return render(request, 'AppBlog/editar_perfil.html', {"title": "Editar usuario", "message": "Editar usuario", "form": form})

""" @login_required()
def perfil(request):
    perfil_list = Perfil.objects.all
    return render(request, 'AppBlog/perfil.html', {'perfil': perfil_list}) """

def perfil(request):
    return render(request, 'AppBlog/perfil.html')    

def perfil_detail(request):
    return render(request, "AppBlog/perfil_detail.html")



  #CRUD

  
class PostsList(ListView):

    model = Posts
    template_name = "AppBlog/posts_list.html"
    


class PostDetail(DetailView):

    model = Posts
    template_name = "AppBlog/posts_detail.html"


class PostCreate(LoginRequiredMixin, CreateView):

    model = Posts
    success_url = reverse_lazy('posts_lista')  # Redirecciono a la vista de posts luego de crear un post
    fields = ['titulo', 'subtitulo', 'cuerpo', 'autor', 'fecha', 'imagen']


class PostUpdate(LoginRequiredMixin, UpdateView):

    model = Posts
    success_url = reverse_lazy('posts_lista')
    fields = ['titulo', 'subtitulo', 'cuerpo']

  

class PostDelete(LoginRequiredMixin, DeleteView):

    model = Posts
    success_url = reverse_lazy('posts_lista')
   
       


class AutoresList(ListView):

    model = Autores
    template_name = "AppBlog/autores_list.html"

class AutoresDetail(DetailView):

    model = Autores
    template_name = "AppBlog/autores_detail.html"

class AutoresCreate(LoginRequiredMixin, CreateView):

    model = Autores
    success_url = reverse_lazy('autores_lista') # Redirecciono a la vista de autores luego de crear un autor
    
    fields = ['nombre', 'apellido', 'email', 'imagen']

class AutoresUpdate(LoginRequiredMixin, UpdateView):

    model = Autores
    success_url = reverse_lazy('autores_lista')
    fields = ['nombre', 'apellido', 'email']

class AutoresDelete(LoginRequiredMixin, DeleteView):

    model = Autores
    success_url = reverse_lazy('autores_lista')    