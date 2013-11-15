from django.shortcuts import render, get_object_or_404
from django.core.urlresolvers import reverse
from django.contrib.syndication.views import Feed
from django.contrib.auth.decorators import login_required

from .models import Recipe
from .forms import RecipeForm


def landing_page(request):
    return render(request, 'landing_page.html')


def home(request):
    context = {'recipes': Recipe.objects.all().order_by('-created')}
    return render(request, 'recipe/home.html', context)


def tagpage(request, tag):
    recipes = Recipe.objects.filter(tags__name=tag)
    return render(request, "recipe/tagpage.html", {
        "recipes": recipes,
        "tag": tag
    })


@login_required(redirect_field_name='redirect_to')
def new_recipe(request):
    recipe_form = RecipeForm()
    return render(request, 'recipe/new_recipe.html', {
        'recipe_form': recipe_form,
    })

def submit_recipe(request):
    return render(request, 'recipe/new_recipe.html', {
    })

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
