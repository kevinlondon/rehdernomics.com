from django.shortcuts import render, get_object_or_404
from django.core.urlresolvers import reverse

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
