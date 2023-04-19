from django.shortcuts import render , redirect , get_object_or_404
from .models import Molo

def home(request):
    data = Molo.objects.all()
    context = {'data': data }
    return render(request, 'home.html',context)

def molo_view(request):
    molo = Molo.objects.all()
    context = {'molo': molo }
    return render(request, 'molo.html',context)