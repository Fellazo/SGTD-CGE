from django.db import models
from django.contrib.auth.models import AbstractUser

# Modelo de Usuario
class Usuario(AbstractUser):
    is_active = models.BooleanField(default=True)

# Modelo de Rol
class Rol(models.Model):
    nombre = models.CharField(max_length=50)
    permisos = models.ManyToManyField('Permiso')
    is_active = models.BooleanField(default=True)

# Modelo de Tesista
class Tesista(models.Model):
    nombre = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=100)
    correo = models.EmailField()

# Modelo de Tutor
class Tutor(models.Model):
    nombre = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=100)

# Modelo de Tribunal
class Tribunal(models.Model):
    nombre = models.CharField(max_length=50)
    profesores = models.ManyToManyField('Tutor')

# Modelo de Tesis
class Tesis(models.Model):
    titulo = models.CharField(max_length=200)
    tesista = models.ForeignKey('Tesista', on_delete=models.CASCADE)
    tutor = models.ForeignKey('Tutor', on_delete=models.CASCADE)
    tribunal = models.ForeignKey('Tribunal', on_delete=models.CASCADE)
    fecha = models.DateField()

# Modelo de Permiso
class Permiso(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField()
    is_active = models.BooleanField(default=True)

# Modelo de No Conformidad
class NoConformidad(models.Model):
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField()
    fecha = models.DateField()
