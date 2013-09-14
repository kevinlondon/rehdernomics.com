from django.conf.urls import patterns, include, url

# Enable Admin
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'lunchclub.views.home', name='home'),
    url(r'^lunchclub/', include('recipe.urls')),
    url(r'^rehdernomics/', include('rehdernomics.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
