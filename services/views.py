from domain.models import Winery, Wine, WineList, WineListWine, SysConfig
from django.http import HttpResponse, Http404
from django.core import serializers

# Sys Config
def sys_config(request):
    configs = SysConfig.objects.all()
    data = serializers.serialize("json", configs)
    return HttpResponse(data)

# Winery details
def winery_detail(request, winery_id):
    try:
        w = Winery.objects.get(pk=winery_id)
    except Winery.DoesNotExist:
        raise Http404

    data = serializers.serialize("json", [w])
    return HttpResponse(data)

# All wineries
def all_wineries(request):
    wineries = Winery.objects.all()
    data = serializers.serialize("json", wineries);
    return HttpResponse(data)
    
# Wine details
def wine_detail(request, wine_id):
    try:
        w = Wine.objects.get(pk=wine_id)
    except Wine.DoesNotExist:
        raise Http404

    data = serializers.serialize("json", [w])
    return HttpResponse(data)

# All wines
def all_wines(request):
    wines = Wine.objects.all()
    data = serializers.serialize("json", wines);
    return HttpResponse(data)

# Wines by winery
def wines_by_winery(request, winery_id):
    wines = Wine.objects.filter(winery__id=winery_id)
    data = serializers.serialize("json", wines)
    return HttpResponse(data)    

# WineList detail
def winelist_detail(request, wine_list_id):
    try:
        wl = WineList.objects.get(pk=wine_list_id)
    except WineList.DoesNotExist:
        raise Http404

    data = serializers.serialize("json", [wl])
    return HttpResponse(data)
    
# WineLists by user
def user_winelists(request, user_id):
    wl = WineList.objects.filter(user__id=user_id)

    data = serializers.serialize("json", wl)
    return HttpResponse(data)
    
# Wines by WineList
def winelist_wines(request, wine_list_id):
    wines = []
    wlws = WineListWine.objects.filter(wine_list__id=wine_list_id)
    for wlw in wlws:
        wines.append(wlw.wine)
    
    data = serializers.serialize("json", wines)
    return HttpResponse(data)
