"""libreriaev3 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.urls import include, path
from libreriaApp import views
from django.urls import path, include
from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register('autoresSerial', views.autorViewSets)
router.register('librosSerial', views.libroViewSets)


urlpatterns = [
    path('libroViews', include(router.urls)),
    path('autorViews', include(router.urls)),
    path('admin/', admin.site.urls),
    path('', views.index),
    path('autores/', views.listadoAutores),
    path('agregarAutor/', views.agregarAutor),
    path('libros/', views.listadoLibros),
    path('agregarLibro/', views.agregarLibro),
    path('eliminarAutor/<int:id>/', views.eliminarAutor, name='eliminar_autor'),
    path('actualizarAutor/<int:id>/', views.actualizarAutor, name='actualizar_autor'),
    path('libros/', views.listadoLibros, name='listado_libros'),
    path('eliminar_libro/<int:id>/', views.eliminar_libro, name='eliminar_libro'),
    path('actualizar_libro/<int:id>/', views.actualizar_libro, name='actualizar_libro'),


]



if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)