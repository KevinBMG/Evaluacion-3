from django.shortcuts import redirect, render
from libreriaApp.forms import FormAutor
from libreriaApp.forms import FormLibro
from libreriaApp.models import autor, libro
from libreriaApp.serializers import autorSerializer, libroSerializer
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework import viewsets


def index(request):
    return render(request, 'templatesLibros/index.html')

def listadoAutores(request):
    autores = autor.objects.all()
    data = {'autores': autores}
    return render(request, 'templatesLibros/autor.html', data)

def agregarAutor(request):
    form = FormAutor()
    if request.method == 'POST':
        form = FormAutor(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        return listadoAutores(request)
    data = {'form': form}
    return render(request, 'templatesLibros/agregarAutor.html', data)

def listadoLibros(request):
    libros = libro.objects.all()
    data = {'libros': libros}
    return render(request, 'templatesLibros/libros.html', data)

def agregarLibro(request):
    form = FormLibro()
    if request.method == 'POST':
        form = FormLibro(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        return listadoLibros(request)
    data = {'form': form}
    return render(request, 'templatesLibros/AgregarLibro.html', data)

def eliminarAutor(request, id):
    autor_a_eliminar = autor.objects.get(id=id)
    autor_a_eliminar.delete()
    return redirect('/autores')

def actualizarAutor(request, id):
    autor_a_actualizar = autor.objects.get(id=id)
    form = FormAutor(instance=autor_a_actualizar)
    if request.method == 'POST':
        form = FormAutor(request.POST, instance=autor_a_actualizar)
        if form.is_valid():
            form.save()
            return redirect('/autores')
    data = {'form': form}
    return render(request, 'templatesLibros/agregarAutor.html', data)

def eliminar_libro(request, id):
    libro_a_eliminar = libro.objects.get(id=id)
    libro_a_eliminar.delete()
    return redirect('/libros')

def actualizar_libro(request, id):
    libro_a_actualizar = libro.objects.get(id=id)
    form = FormLibro(instance=libro_a_actualizar)
    if request.method == 'POST':
        form = FormLibro(request.POST, instance=libro_a_actualizar)
        if form.is_valid():
            form.save()
            return redirect('/libros')
    data = {'form': form}
    return render(request, 'templatesLibros/agregarLibro.html', data)


class autorList(generics.ListCreateAPIView):
    query = autor.objects.all()
    serializers_class = autorSerializer


    def get(self, request):    
        autores = autor.objects.all()
        serializer = autorSerializer(autores, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = autorSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class autorDetail(generics.ListCreateAPIView):
    query = autor.objects.all()
    serializers_class = autorSerializer
    
    def get_object(self, pk):
        try: 
            return autor.objects.get(pk=pk)
        except autor.DoesNotExist:
            return Http404
        
    def get(self, request, pk):
        autores = self.get_object(pk)
        serializer = autorSerializer(autores)
        return Response(serializer.data)
    
    def put(self, request, pk):
        autores = self.get_object(pk)
        serializer = autorSerializer(autores, data=request.data)
        if serializer.iis_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        autores = self.get_object(pk)
        autores.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
        

class autorViewSets(viewsets.ModelViewSet):
    queryset = autor.objects.all()
    serializer_class = autorSerializer


class libroList(generics.ListCreateAPIView):
    query = libro.objects.all()
    serializers_class = libroSerializer


    def get(self, request):    
        libros = libro.objects.all()
        serializer = libroSerializer(libros, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = libroSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class libroDetail(generics.ListCreateAPIView):
    query = libro.objects.all()
    serializers_class = libroSerializer
    
    def get_object(self, pk):
        try: 
            return libro.objects.get(pk=pk)
        except libro.DoesNotExist:
            return Http404
        
    def get(self, request, pk):
        libros = self.get_object(pk)
        serializer = libroSerializer(libros)
        return Response(serializer.data)
    
    def put(self, request, pk):
        libros = self.get_object(pk)
        serializer = libroSerializer(libros, data=request.data)
        if serializer.iis_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        libros = self.get_object(pk)
        libros.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
        

class libroViewSets(viewsets.ModelViewSet):
    queryset = libro.objects.all()
    serializer_class = libroSerializer
    
    