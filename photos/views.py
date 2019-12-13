from django.shortcuts import render,redirect
from django.http  import HttpResponse, Http404
import datetime as dt

from .models import Image,Category,Location

# Create your views here.

def all_photos(request):
    gallery = Image.get_images()

    return render(request, 'all-pics/pics.html', {"gallery": gallery})

def single_image(request, image_id):
    try:
        gallery = Image.objects.get(id = image_id)
    except DoesNotExist:
        raise Http404()

    return render(request, 'all-pics/img.html', {"gallery":gallery})
