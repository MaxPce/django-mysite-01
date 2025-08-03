from django.db import models

# Create your models here.
class Proyecto(models.Model):
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField()
    fecha_creacion = models.DateField(auto_now_add=True)
    tecnologias = models.CharField(max_length=100, blank=True)
    enlace = models.URLField(blank=True)

    def __str__(self):
        return self.titulo
    