from django.db import models

# Create your models here.
class Eventos(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    activo = models.BooleanField(default=False)
    precio = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    imagen_url = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = 'Eventos'