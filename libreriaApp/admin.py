from django.contrib import admin

from libreriaApp.models import autor, libro

class autorMod(admin.ModelAdmin):
    
    list_display = ['nombre', 'nacionalidad', 'fechaNaci', 'biografia', 'imagen']

class libroMod(admin.ModelAdmin):
    
    list_display = ['titulo', 'genero', 'fechaPubli', 'autor', 'portada']

# Register your models here.
admin.site.register(autor, autorMod)
admin.site.register(libro, libroMod)
