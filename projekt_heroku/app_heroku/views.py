from django.shortcuts import render

from .models import Applikacio

def toc(request):
    return render(request, 'toc/toc.html', {'apps':Applikacio.objects.all()})