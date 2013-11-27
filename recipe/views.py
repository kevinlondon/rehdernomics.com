from django.shortcuts import render, get_object_or_404, redirect
from django.core.urlresolvers import reverse
from django.contrib.syndication.views import Feed
from django.contrib.auth.decorators import login_required
from django.forms.formsets import formset_factory
from django.views.generic import ListView, DetailView

from .models import Recipe, Ingredient, RecipeIngredient
from .forms import RecipeForm, IngredientForm, IngredientFormSetHelper, RecipeRatingForm


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


class RecipeDetailView(DetailView):
    template_name = "recipe/detail.html"
    model = Recipe

    def get_context_data(self, **kwargs):
        context = super(RecipeDetailView, self).get_context_data(**kwargs)
        context['recipe_rating_form'] = RecipeRatingForm()
        return context



class IngredientListView(ListView):
    context_object_name = "ingredients"
    template_name = "recipe/ingredient_list.html"
    queryset = Ingredient.objects.all()


class IngredientRecipeList(ListView):
    context_object_name = "recipes"
    template_name = "recipe/ingredient_recipes.html"
    model = Ingredient

    def get_queryset(self):
        self.ingredient = get_object_or_404(Ingredient, pk=self.kwargs['pk'])
        return Recipe.objects.filter(ingredients__name=self.ingredient.name)

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(IngredientRecipeList, self).get_context_data(**kwargs)
        context['ingredient'] = self.ingredient
        return context


def submit_rating(request):
    if request.method == "POST":
        recipe_id = request.POST["recipe_id"]
        rating_id = request.POST['rating_id']
        rating = int(rating_id[-1]) + 1
        recipe = get_object_or_404(Recipe, pk=recipe_id)

        recipe.rating.add(score=rating, user=request.user, ip_address=request.META['REMOTE_ADDR'])
        print "Saved rating", rating

    return None

def submit_recipe(request):
    if request.method == "POST":
        recipe_form = RecipeForm(request.POST, request.FILES, prefix="recipe")
        ingredient_formset = formset_factory(IngredientForm)
        ingredient_form = ingredient_formset(request.POST, prefix="ingredient")
        if recipe_form.is_valid() and ingredient_form.is_valid():
            r_info = recipe_form.cleaned_data
            recipe = Recipe.objects.create(
                title=r_info['name'],
                author=request.user,
                description=r_info['description'],
                directions=r_info['directions'],
                image=r_info['image'],
            )

            for i_info in ingredient_form.cleaned_data:
                if not i_info:
                    continue

                name = i_info['name']
                ingredient, created = Ingredient.objects.get_or_create(name=name)
                requirement = RecipeIngredient.objects.create(
                    recipe=recipe,
                    ingredient=ingredient,
                    quantity=i_info['quantity'],
                    ingredient_state=i_info['state'],
                )

            return redirect(recipe.get_absolute_url())

        return redirect('recipe_new')


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
