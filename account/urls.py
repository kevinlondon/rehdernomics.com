from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^login/$', 'django.contrib.auth.views.login', {'template_name': 'account/login.html'}),
    url(r'^profile/$', 'account.views.profile', name='account_profile'),
)
