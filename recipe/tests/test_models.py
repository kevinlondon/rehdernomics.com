from django.test import TestCase
from django.utils import timezone

from recipe.models import Recipe


class Recipe(TestCase):
    def test_creating_a_new_recipe(self):
        # Create a new recipe object with its recipe.

        recipe = Recipe()
        recipe.title = "What's up?"
        recipe.body = "This is a goldarn recipe."
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
        self.assertEqual(only_recipe_in_db.body, recipe.body)
