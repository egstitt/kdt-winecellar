from django.db import models
from django.contrib.auth.models import User

# Model base
class ModelBase(models.Model):
    date_created = models.DateTimeField('date created')
    date_updated = models.DateTimeField('date updated')
    created_by = models.ForeignKey(User, null=True, related_name='+')
    updated_by = models.ForeignKey(User, null=True, related_name='+')
    
    class Meta:
        abstract = True

# SysConfig
class SysConfig(models.Model):
    supported_version = models.CharField(max_length=10)
    def __unicode__(self):
        return self.supported_version

# Winery
class Winery(ModelBase):
    name = models.CharField(max_length=200)
    def __unicode__(self):
        return self.name

# Wine
class Wine(ModelBase):
    winery = models.ForeignKey(Winery)
    wine_type = models.CharField(max_length=200)
    vintage = models.CharField(max_length=4)
    def __unicode__(self):
        return self.winery.name + " " + self.wine_type + " " + self.vintage

# WineList
class WineList(ModelBase):
    description = models.CharField(max_length=200)
    user = models.ForeignKey(User)
    def __unicode__(self):
        return self.description
        
# WineListWine
class WineListWine(ModelBase):
    wine_list = models.ForeignKey(WineList)
    wine = models.ForeignKey(Wine)
    def __unicode__(self):
        return self.wine_list.__unicode__() + " " + self.wine.__unicode__()
       
