from django.conf.urls import patterns, url
from django.views.generic import ListView, DetailView
from django.contrib.syndication.views import Feed

from recipe.models import Recipe


class RecipeFeed(Feed):
    title = "Lunch Club Recipes"
    description = "Recipes from the Lunch Club."
    link = "/lunchclub/feed"

    def items(self):
        return Recipe.objects.all().order_by("-created")[:5]

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.body

    def item_link(self, item):
        return u"/recipe/%d" % item.id


urlpatterns = patterns('recipe.views',
    url(r'^$', ListView.as_view(
        queryset=Recipe.objects.all().order_by("-created"),
        context_object_name="recipes",
        template_name="recipe/list.html",
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
