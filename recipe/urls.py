from django.conf.urls import patterns, url
from django.views.generic import ListView, DetailView

from .models import Recipe
from .views import RecipeFeed, IngredientListView, IngredientRecipeList


urlpatterns = patterns('recipe.views',
    url(r'^$', 'home', name='recipe_home'),
    url(r'^new_recipe/$', 'new_recipe', name="recipe_new"),
    url(r'^submit_recipe/$', 'submit_recipe', name="recipe_submit"),
    url(r'^(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{1,2})/(?P<slug>[-\w]+)/$',
         view=DetailView.as_view(model=Recipe, template_name="recipe/detail.html"),
         name='recipe_detail'),
    url(r'^ingredients/$', IngredientListView.as_view(), name="recipe_ingredient_list"),
    url(r'^ingredients/(?P<pk>\d+)/$', IngredientRecipeList.as_view(), name="recipe_ingredient_search"),
    url(r'^recipes/$', ListView.as_view(
        queryset=Recipe.objects.all().order_by("-created"),
        template_name="recipe/archives.html")),
    url(r'^tag/(?P<tag>\w+)$', 'tagpage'),
    url(r'^feed/$', RecipeFeed()),
)
