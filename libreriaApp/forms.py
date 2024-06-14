from django import forms
from libreriaApp.models import *

class FormLibro(forms.ModelForm):
    
    class Meta:
        model = libro
        fields = '__all__'

class FormAutor(forms.ModelForm):
    
    class Meta:
        model = autor
        fields = '__all__'