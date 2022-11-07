
# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse  
from .models import Person

def indexPageView(request) :
    data= Person.objects.all()
    context = {
        "data" : data
    }
    return render(request, 'apppages/index.html', context)

