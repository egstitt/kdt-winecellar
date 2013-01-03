from domain.models import WineList, Winery, Wine, WineListWine, SysConfig
from django.contrib import admin

admin.site.register(SysConfig)
admin.site.register(WineListWine)
admin.site.register(WineList)
admin.site.register(Winery)
admin.site.register(Wine)
