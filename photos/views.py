from django.shortcuts import render

# Create your views here.
from django.http  import HttpResponse, Http404
import datetime as dt
from django.shortcuts import render,redirect

from .models import Image,Category,Location


def all_photos(request):
    gallery = Image.get_images()

    return render(request, 'all-pics/pics.html', {"gallery": gallery})