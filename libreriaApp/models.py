from django.db import models


class autor(models.Model):
    id = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=50)
    nacionalidad = models.CharField(max_length=50)
    fechaNaci = models.DateField()
    biografia = models.TextField()
    imagen = models.ImageField(upload_to='media/', null=True, blank=True)
    def __str__(self):
        return str(self.id) + "" + self.nombre + "(nombre : " + str(self.nombre) + ")"


class libro(models.Model):
    id = models.IntegerField(primary_key=True)
    titulo = models.CharField(max_length=50)
    genero = models.CharField(max_length=50)
    fechaPubli = models.DateField()
    autor = models.ForeignKey(autor, on_delete=models.CASCADE)
    portada = models.ImageField(upload_to='media/', null=True, blank=True)
    def __str__(self):
        return str(self.id) + "" + self.titulo + "(titulo : " + str(self.titulo) + ")"

 


