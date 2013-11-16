from django.shortcuts import render, get_object_or_404
from django.core.urlresolvers import reverse
from django.contrib.syndication.views import Feed
from django.contrib.auth.decorators import login_required
from django.forms.formsets import formset_factory

from .models import Recipe
from .forms import RecipeForm, IngredientForm, IngredientFormSetHelper


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
    recipe_form = RecipeForm(prefix="recipe")
    ingredient_formset = formset_factory(IngredientForm, extra=3)
    ingredient_formset_helper = IngredientFormSetHelper()
    return render(request, 'recipe/new_recipe.html', {
        'recipe_form': recipe_form,
        'ingredient_formset': ingredient_formset(prefix="ingredient"),
        'ingredient_formset_helper': ingredient_formset_helper,
    })


def submit_recipe(request):
    if request.method == "POST":
        recipe_form = RecipeForm(request.POST, prefix="recipe")
        ingredient_formset = formset_factory(IngredientForm)
        ingredient_form = ingredient_formset(request.POST, prefix="ingredient")
        if recipe_form.is_valid() and ingredient_form.is_valid():
            r_info = recipe_form.cleaned_data
            recipe = Recipe.objects.create(
                name=r_info['recipe_name'], description=r_info['description'],
                directions=r_info['directions'], image=r_info['image'],
            )
            print recipe
            print recipe_form.cleaned_data
            print ingredient_form.cleaned_data

    assert False

    return render(request, 'recipe/home.html', {
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
