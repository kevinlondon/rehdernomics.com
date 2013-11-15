import factory

from django.contrib.auth.models import User
from recipe.models import Recipe, Ingredient


class UserFactory(factory.django.DjangoModelFactory):
    FACTORY_FOR = User
    username = 'john'


class RecipeFactory(factory.django.DjangoModelFactory):
    FACTORY_FOR = Recipe
    author = factory.SubFactory(UserFactory)


class IngredientFactory(factory.django.DjangoModelFactory):
    FACTORY_FOR = Ingredient
    name = "Onion"
