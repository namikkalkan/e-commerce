from django.shortcuts import render
from django.http import HttpResponse
from PIL import Image

# Create your views here.

def index(request):

    return render(request,'index.html')

def indexitem(request):

    return render(request,'index-item.html')