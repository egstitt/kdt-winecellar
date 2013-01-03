from django.conf.urls.defaults import *

handler500 = 'djangotoolbox.errorviews.server_error'

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Public
    url(r'^pub/wineries/(?P<winery_id>\d+)/$', 'pub.views.winery_detail'),
    url(r'^pub/wines/(?P<wine_id>\d+)/$', 'pub.views.wine_detail'),

    # Internal
    url(r'^internal/wineries/list/$', 'internal.views.wineries_list'),
    url(r'^internal/wines/winery/(?P<winery_id>\d+)/$', 'internal.views.wines_by_winery'),
    url(r'^internal/batch/$', 'internal.views.batch_ops'),
    url(r'^internal/batch/wipe_data/$', 'internal.views.wipe_data'),
    url(r'^internal/batch/populate_data/$', 'internal.views.populate_data'),
    url(r'^internal/batch/refresh_data/$', 'internal.views.refresh_data'),

    # Services
    url(r'^services/config/$', 'services.views.sys_config'),
    url(r'^services/wineries/(?P<winery_id>\d+)/$', 'services.views.winery_detail'),
    url(r'^services/wineries/list/$', 'services.views.all_wineries'),
    url(r'^services/wines/(?P<wine_id>\d+)/$', 'services.views.wine_detail'),
    url(r'^services/wines/list/$', 'services.views.all_wines'),
    url(r'^services/wines/winery/(?P<winery_id>\d+)/$', 'services.views.wines_by_winery'),
    url(r'^services/winelists/(?P<wine_list_id>\d+)/$', 'services.views.winelist_detail'),
    url(r'^services/winelists/user/(?P<user_id>\d+)/$', 'services.views.user_winelists'),
    url(r'^services/winelists/(?P<wine_list_id>\d+)/wines/$', 'services.views.winelist_wines'),
    url(r'^admin/', include(admin.site.urls)),
    ('^_ah/warmup$', 'djangoappengine.views.warmup'),
    ('^$', 'django.views.generic.simple.direct_to_template',
     {'template': 'home.html'}),
     
)
