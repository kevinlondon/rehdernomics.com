from django.conf.urls import patterns, include, url

# Enable Admin
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'blog.views.landing_page'),
    url(r'^lunchclub/', include('blog.urls')),
    url(r'^rehdernomics/', include('rehdernomics.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
