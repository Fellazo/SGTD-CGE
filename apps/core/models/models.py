from django.db import models

# Create your models here.
from django.db import models

class Usuario(models.Model):
    username = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=50)
    is_active = models.BooleanField(default=True)

class Rol(models.Model):
    nombre = models.CharField(max_length=50)
    permisos = models.ManyToManyField('Permiso')
    is_active = models.BooleanField(default=True)

class Tesista(models.Model):
    nombre = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=50)
    correo = models.EmailField()

class Tutor(models.Model):
    nombre = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=50)

class Tribunal(models.Model):
    nombre = models.CharField(max_length=50)
    profesores = models.ManyToManyField(Tutor)

class Tesis(models.Model):
    titulo = models.CharField(max_length=100)
    tesista = models.ForeignKey(Tesista, on_delete=models.CASCADE)
    tutor = models.ForeignKey(Tutor, on_delete=models.CASCADE)
    tribunal = models.ForeignKey(Tribunal, on_delete=models.CASCADE)
    fecha = models.DateField()

class Permiso(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField()
    is_active = models.BooleanField(default=True)

class NoConformidad(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField()
    fecha = models.DateField()
