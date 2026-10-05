from django.contrib import admin
from .models import Volumen, Precios ######## NUEVO   uimportante el . en models
# Register your models here.

@admin.register(Volumen)
class VolumenAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'marca', 'categoria', 'disponible', 'stock')
    search_fields = ('nombre', 'marca', 'categoria')
    list_filter = ('categoria', 'disponible')
    ordering = ('id',)

@admin.register(Precios)
class PreciosAdmin(admin.ModelAdmin):
    list_display = ('id', 'volumen', 'precio', 'moneda', 'observacion')
    search_fields = ('volumen__nombre', 'moneda')
    list_filter = ('moneda',)
    ordering = ('id',)