from django.shortcuts import render
def natal(request):
    return render(request, 'feriado.html')

# Create your views here.
from django.http import HttpResponse
def feriado(request):
    return HttpResponse("Não é feriado.")

from django.shortcuts import render
def natal(request):
    contexto = {'feriado': True,
    'carnaval': False}
    return render(request, 'feriado.html', contexto)