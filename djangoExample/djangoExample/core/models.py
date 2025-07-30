from django.db import models


class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    imagen = models.ImageField(upload_to='productos/')
    disponible = models.BooleanField(default=True)
    tipo = models.CharField(max_length=50, null=True, blank=True)


def __str__(self):
    return self.nombre
