from django.shortcuts import render, redirect
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, "web_asistencia/index.html")

def verificar_dispositivo_movil(request):
    user_agent = request.META.get('HTTP_USER_AGENT', '')
    return render(request, 'web_asistencia/index.html', {'user_agent': user_agent})

def mostrarIndex(request):
    es_dispositivo_movil = verificar_dispositivo_movil(request)

    context = {'es_dispositivo_movil': es_dispositivo_movil}

    return render(request, 'web_asistencia/index.html', context)
