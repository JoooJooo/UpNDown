from django.template import loader
from django.shortcuts import render

def index(request):
    return render(request, 'core/index.html')