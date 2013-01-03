from domain.models import Winery, Wine, WineList, WineListWine, SysConfig
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render_to_response
from datetime import datetime

def batch_ops(request):
    return render_to_response('internal/batch_ops.html')

##    
# Wipes all test data
##
def wipe_data(request):
    User.objects.filter(email='lennon@thebeatles.com').delete()
    SysConfig.objects.all().delete()
    Winery.objects.all().delete()
    Wine.objects.all().delete()
    WineList.objects.all().delete()
    WineListWine.objects.all().delete()

    return HttpResponse("OK")

##
# Populates all test data
##
def populate_data(request):

    # User
    user = User.objects.create_user('john', 'lennon@thebeatles.com', 'johnpassword')
    user.is_staff = True
    user.is_active = True
    user.save()

    # Sys Config
    config = SysConfig(supported_version='1.0')
    config.save()
    
    # Wineries
    bogle = Winery(name='Bogle', date_updated=datetime.now(), date_created=datetime.now())
    bogle.save()
    
    husch = Winery(name='Husch', date_updated=datetime.now(), date_created=datetime.now())
    husch.save()
    
    # Wines
    bogle1 = Wine(winery = bogle, wine_type='Cabernet Savignon', vintage='2011', date_updated=datetime.now(), date_created=datetime.now())
    bogle1.save()
    
    bogle2 = Wine(winery = bogle, wine_type='Cabernet Savignon', vintage='2010', date_updated=datetime.now(), date_created=datetime.now())
    bogle2.save()
    
    husch1 = Wine(winery = husch, wine_type='Cabernet Savignon', vintage='2009', date_updated=datetime.now(), date_created=datetime.now())
    husch1.save()
    
    # Wine Lists
    list1 = WineList(description='MyList1', user=user, date_updated=datetime.now(), date_created=datetime.now())
    list1.save()
    
    # Wine List Wines
    wlw = WineListWine(wine_list=list1, wine=bogle1, date_updated=datetime.now(), date_created=datetime.now())
    wlw.save()
    
    wlw = WineListWine(wine_list=list1, wine=husch1, date_updated=datetime.now(), date_created=datetime.now())
    wlw.save()
    
    return HttpResponse("OK")
    
##
# Refreshes the test data
##
def refresh_data(request):
    wipe_data(request)
    return populate_data(request)

##
# Winery List
##
def wineries_list(request):
    wineries = Winery.objects.all()
    return render_to_response('internal/wineries.html', {"wineries" : wineries })
    
##
# Wines by winery
##
def wines_by_winery(request, winery_id):
    wines = Wine.objects.filter(winery__id=winery_id)
    return render_to_response('internal/wines.html', {"wines" : wines, "winery_id" : winery_id })
    

