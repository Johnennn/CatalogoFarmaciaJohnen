from CategoriasApp import views
from django.urls import path

urlpatterns = [
    path('volumen/',views.volumen),
    path('resumen/',views.resumen),
]
