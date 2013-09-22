from django.conf.urls import patterns, url
from django.views.generic import ListView, DetailView

from recipe.models import Recipe




urlpatterns = patterns('recipe.views',
    url(r'^$', ListView.as_view(
        queryset=Recipe.objects.all().order_by("-created"),
        context_object_name="recipes",
        template_name="recipe/home.html",
        paginate_by=4,
    ), name="recipe_home"),

    url(r'^(?P<year>\d{4})/(?P<day>\d{1,2})/(?P<slug>[-\w]+)/$',
         view=DetailView.as_view(model=Recipe, template_name="recipe/detail.html"),
         name='recipe_detail'),
    url(r'^archive/$', ListView.as_view(
        queryset=Recipe.objects.all().order_by("-created"),
        template_name="recipe/archives.html")),
    url(r'^tag/(?P<tag>\w+)$', 'tagpage'),
    url(r'^feed/$', RecipeFeed()),
)
