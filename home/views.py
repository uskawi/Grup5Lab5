from django.shortcuts import render
from .models import Img

def index(request):
    images = Img.objects.all()

    context = {
      'images': images,
    }

    return render(request, 'index.html', context)

def contact(request):

    return render(request, 'contact.html')

def features(request):

    return render(request, 'features.html')

def price(request):

    return render(request, 'price.html')

def gallery(request):

    images = Img.objects.all()

    context = {
      'images': images,
    }

    return render(request, 'gallery.html', context)
