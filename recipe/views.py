from django.shortcuts import render, get_object_or_404
from django.core.urlresolvers import reverse
from django.contrib.syndication.views import Feed

from recipe.models import Recipe


def home(request):
    context = {'recipes': Recipe.objects.all()}
    return render(request, 'home.html', context)


def landing_page(request):
    return render(request, 'landing_page.html')


def tagpage(request, tag):
    recipes = Recipe.objects.filter(tags__name=tag)
    return render(request, "recipe/tagpage.html", {
        "recipes": recipes,
        "tag": tag
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
