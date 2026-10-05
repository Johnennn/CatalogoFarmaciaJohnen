from django.shortcuts import render
from django.http import HttpResponse
from pathlib import Path
import json
from .models import Volumen
# Create your views here

def volumen(request):
    productos = Volumen.objects.all()
    return render(request, 'CategoriasApp/volumen.html', {'productos': productos})
def resumen(request):
   total = Volumen.objects.count()
   disponibles = Volumen.objects.filter(stock__gt=0).count()
   sin_stock = Volumen.objects.filter(stock=0).count()
   return render(request, 'CategoriasApp/resumen.html', {
       'total': total,
         'disponibles': disponibles,
            'sin_stock': sin_stock
             })