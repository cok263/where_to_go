from django.http import JsonResponse
from django.shortcuts import get_object_or_404
import json

from places.models import *


def show_place(request, id=1):
    place = get_object_or_404(Place, id=id)
    imgs = [img.image.url for img in Image.objects.filter(place=place)]
    data = {
        "title": place.title,
        "imgs": imgs,
        "description_short": place.description_short,
        "description_long": place.description_long,
        "coordinates": {"lat": place.lat, "lng": place.lng},
    }
    response = JsonResponse(data, safe=False,
                            json_dumps_params={'ensure_ascii': False})

    return response
