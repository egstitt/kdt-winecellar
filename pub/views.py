from domain.models import Winery, Wine
from django.http import HttpResponse, Http404
from django.core import serializers

# Winery details
def winery_detail(request, winery_id):
    try:
        w = Winery.objects.get(pk=winery_id)
    except Winery.DoesNotExist:
        raise Http404

    data = serializers.serialize("xml", [w])
    return HttpResponse(data)

# Wine details
def wine_detail(request, wine_id):
    try:
        w = Wine.objects.get(pk=wine_id)
    except Wine.DoesNotExist:
        raise Http404

    data = serializers.serialize("xml", [w])
    return HttpResponse(data)

