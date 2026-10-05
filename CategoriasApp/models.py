from django.db import models

# Create your models here.######## NUEVO######## NUEVO######## NUEVO######## NUEVO
class Volumen(models.Model):
    id = models.PositiveSmallIntegerField(primary_key=True)
    nombre = models.CharField(max_length=50)
    marca = models.CharField(max_length=50)
    disponible= models.CharField(max_length=20)
    categoria = models.CharField(max_length=50)
    stock = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.nombre

class Precios(models.Model):
    volumen =models.OneToOneField(Volumen, on_delete=models.CASCADE) # esto conecta ambos modelos, cada producto tendrá un precio asociado
    precio = models.DecimalField(max_digits=10, decimal_places=0)
    moneda = models.CharField(max_length=10, default='CLP')
    observacion = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return f'{self.volumen.nombre}: ${self.precio}'