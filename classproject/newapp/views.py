
# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse  
from .models import JoinedData

def indexPageView(request) :
    data= JoinedData.objects.all()
    context = {
        "data" : data
    }
    return render(request, 'apppages/index.html', context)

