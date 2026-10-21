
from django.db import models


class Proyecto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    fecha_creacion = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.nombre


class Tarea(models.Model):
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField()
    proyecto = models.ForeignKey(
        Proyecto,
        on_delete=models.CASCADE,
        related_name="tareas"
    )

    def __str__(self):
        return self.titulo

