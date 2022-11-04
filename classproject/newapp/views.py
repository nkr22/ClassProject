# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
        
def indexPageView(request) :
    return render(request, 'apppages/index.html')    