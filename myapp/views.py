from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'myapp/index.html')

def pestaña(request):
    return render(request, 'myapp/pestaña.html')

def equipo(request):
    return render(request, 'myapp/equipo.html')