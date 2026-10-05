from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def secciones(request):
    return render(request, 'PrincipalApp/secciones.html')