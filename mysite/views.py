from django.http import HttpResponse
from django.template import loader

from places.models import *


def show_where_to_go(request):
    places = Place.objects.all()

    features = {
        "type": "FeatureCollection",
        "features": [],
    }

    for place in places:
        feature = {"type": "Feature",}
        
        feature["geometry"] = {
            "type": "Point",
            "coordinates": [ place.lng, place.lat ],
        }
        feature["properties"] = {
            "title": place.title,
            "placeId": place.id,
            "detailsUrl": "./places/file.json",
        }
        features["features"].append(feature)
        
    data = {
        "places": features,
    }

    template = loader.get_template('index.html')
    context = data
    rendered_page = template.render(context, request)
    return HttpResponse(rendered_page)
