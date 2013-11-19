from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'recipe.views.landing_page'),
    url(r'^lunchclub/', include('recipe.urls')),
    url(r'^rehdernomics/', include('rehdernomics.urls')),
    url(r'^accounts/', include('account.urls')),
    url(r'^admin/', include(admin.site.urls)),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    # static files (images, css, javascript, etc.)
    urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve', {
	        'document_root': settings.MEDIA_ROOT,
        }),
        (r'^static/(?P<path>.*)$', 'django.views.static.serve', {
	        'document_root': settings.STATIC_ROOT
        }),
    )

