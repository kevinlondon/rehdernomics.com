from django.test import TestCase
from django.utils import timezone

from recipe.models import Recipe, Ingredient, RecipeIngredient
from .factories import UserFactory, RecipeFactory, IngredientFactory


class RecipeTest(TestCase):
    def test_creating_a_new_recipe(self):
        # Create a new recipe object with its recipe.

        recipe = Recipe()
        recipe.title = "What's up?"
        recipe.description = "This is a goldarn recipe."
        recipe.author = UserFactory.create()
        recipe.created = timezone.now()

        # Check if we can save it to the db
        recipe.save()

        # Now check if we can find it in the db again
        all_recipes_in_db = Recipe.objects.all()
        self.assertEqual(len(all_recipes_in_db), 1)
        only_recipe_in_db = all_recipes_in_db[0]
        self.assertEqual(only_recipe_in_db, recipe)

        # And check that it has saved its two attrbs, question and pub_date
        self.assertEqual(only_recipe_in_db.title, recipe.title)
        self.assertEqual(only_recipe_in_db.description, recipe.description)

    def test_absolute_url(self):
        recipe = RecipeFactory.create(title="Test Title")
        url = recipe.get_absolute_url()

        # Check for identifying times in url
        self.assertIn(str(recipe.created.year), url)
        self.assertIn(str(recipe.created.month), url)
        self.assertIn(str(recipe.created.day), url)

        # Test that at least a piece of the title is in the URL
        self.assertIn(recipe.title.split()[0].lower(), url)


class IngredientsTest(TestCase):
    def test_adding_ingredients_to_a_recipe(self):
        recipe = RecipeFactory.create()
        olive = IngredientFactory.create(name="Olives")
        requirement = RecipeIngredient.objects.create(recipe=recipe, ingredient=olive, quantity=5, ingredient_state="Chopped")
        self.assertEquals("%s" % requirement.ingredient, "Olives")
        self.assertEquals("%s" % requirement, "5 Chopped Olives")
        self.assertIn(olive, recipe.ingredients.all())


