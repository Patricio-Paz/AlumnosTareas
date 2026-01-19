from django.db import models

# Create your models here.
class Tarea(models.Model):
    nombre= models.CharField(max_length=100)
    descripcion= models.TextField()
    estado=models.BooleanField(default=False)

    
    def __str__(self):
        return self.nombre
    
class Alumno(models.Model):
    rut = models.CharField(max_length=100,primary_key=True)
    nombre_completo=models.CharField(max_length=100)
    tarea = models.ManyToManyField(Tarea,blank=True)
    