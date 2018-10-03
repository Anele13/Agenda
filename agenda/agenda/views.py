from django.shortcuts import render
from materia.models import *
from django.http import JsonResponse
from django.core import serializers
import datetime

def home(request):
    return render(request, 'calendario.html')

def guardar(request):
    hoy=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(hoy)
    #evento = Evento(id=1, color='green',title="evento de la base",start=hoy,end=hoy)
    #evento.save()
    cosa = list(Evento.objects.values())
    #data = serializers.serialize('json', cosa)#,fields=('id','color','start','end'))
    print(cosa)
    return JsonResponse(cosa, safe=False)
