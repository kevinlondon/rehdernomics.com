from django.conf.urls import patterns, url

urlpatterns = patterns('rehdernomics.views',
    url(r'^$', 'home', name="rehdernomics_home"),
)
