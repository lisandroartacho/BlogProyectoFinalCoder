from django.urls import path
from AppBlog import views
from .views import *
from django.contrib.auth.views import LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.conf.urls.static import static




urlpatterns = [
  
  path('', views.inicio, name = 'inicio'),
  path('posts/', PostsList.as_view(), name='posts_lista'),
  path('posts/<pk>', PostDetail.as_view(), name='posts_detalle'),
  path('posts/editar/<pk>', PostUpdate.as_view(), name='posts_editar'),
  path('posts/nuevo/', PostCreate.as_view(), name='posts_crear'),
  path('posts/borrar/<pk>', PostDelete.as_view(), name='posts_borrar'),

  path('autores/', AutoresList.as_view(), name = 'autores_lista'),
  path('autores/<pk>', AutoresDetail.as_view(), name='autores_detalle'),
  path('autores/editar/<pk>', AutoresUpdate.as_view(), name='autores_editar'),
  path('autores/nuevo/', AutoresCreate.as_view(), name='autores_crear'),
  path('autores/borrar/<pk>', AutoresDelete.as_view(), name='autores_borrar'),

  path('nosotras/',views.nosotras, name = 'nosotras'),
 
  path('login/', views.login_request, name = 'Login'),
  path('registro', views.registro, name = 'Registro'),
  path('logout', LogoutView.as_view(template_name='AppBlog/logout.html'), name = 'Logout'),

  path('editarPerfil', views.editarPerfil, name = 'editar_perfil'), 
  path('perfil/', views.perfil, name="perfil"),
  path('perfil_detail', views.perfil_detail, name = 'perfil_detail'),
  
  
  

]

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
        urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

else:
        urlpatterns += staticfiles_urlpatterns()   



   
