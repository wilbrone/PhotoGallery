from django.shortcuts import render,redirect
from django.http import Http404, HttpResponse, request
import datetime as dt

from .models import Image,Category,Location

# Create your views here.

def all_photos(request):
    gallery = Image.get_images()

    return render(request, 'all-pics/index.html', {"gallery": gallery})


def single_image(request, image_id):
    try:
        gallery = Image.objects.get(id = image_id)
    except DoesNotExist:
        raise Http404()

    return render(request, 'all-pics/img.html', {"gallery":gallery})

def search_results(request):
    if 'category' in request.GET and request.GET['category']:
        search_term = request.GET.get('category')
        print ('*********'+search_term)
        searched_categ = Category.search_category(search_term)
        print ('*********'+searched_categ)
        message = f'{search_term}'

        searched_image = Image.get_pics_cat(searched_categ)

        return render(request, 'all-pics/search.html', {'message': message, 'photoz':searched_image})

    else:
        message = 'You havent searched for any item'
        return render(request, 'all-pics/search.html', {'message':message})