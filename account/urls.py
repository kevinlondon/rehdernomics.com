from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^login/$', 'django.contrib.auth.views.login', {'template_name': 'account/login.html'}, name="account-login"),
    url(r'^profile/$', 'account.views.profile', name='account-profile'),
    url(r'^change_password/$', 'django.contrib.auth.views.password_change', name='account-password-change'),
    url(r'^change_password/done/$', 'django.contrib.auth.views.password_change_done', name="password_change_done"),
)
