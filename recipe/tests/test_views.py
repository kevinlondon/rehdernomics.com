from django.test import TestCase

from django.utils import timezone
from django.core.urlresolvers import reverse

from recipe.models import Recipe
from .factories import RecipeFactory, UserFactory
#from recipes.forms import recipe


class HomePageViewTest(TestCase):
    def test_root_url_links_to_rehdernomics_and_recipes(self):
        response = self.client.get('/')

        self.assertTemplateUsed(response, 'landing_page.html')

        # Check that we have links to both.
        recipe_home = reverse("recipe_home")
        self.assertIn(recipe_home, response.content)

        rehder_home = reverse("rehdernomics_home")
        self.assertIn(rehder_home, response.content)

    def test_recipe_homepage(self):
        """Should contain the two sample entries we create."""

        user = UserFactory(first_name="Amit")
        recipe1 = RecipeFactory(
            title='My First recipe',
            description='This is a test recipe.',
            created=timezone.now(),
            author=user,
        )
        recipe1.save()
        recipe2 = RecipeFactory(
            title="life, the universe and everything",
            description="This is the body of the recipe.",
            created=timezone.now(),
            author=user,
        )
        recipe2.save()

        response = self.client.get('/lunchclub/')

        # Check that we've used the right template
        self.assertTemplateUsed(response, 'recipe/home.html')

        # Check that we've passed recipes to the template
        recipes_in_context = response.context['recipes']
        # Should be in reverse chronological order
        self.assertEquals(list(recipes_in_context), [recipe2, recipe1])

        # Check the recipe names appear on the page
        self.assertIn(recipe1.title, response.content)
        self.assertIn(recipe2.title, response.content)

        # Check that the page also contains the urls to individual recipes
        recipe1_url = reverse('recipe.views.detail', args=[recipe1.id, ])
        self.assertIn(recipe1_url, response.content)
        recipe2_url = reverse('recipe.views.detail', args=[recipe2.id, ])
        self.assertIn(recipe2_url, response.content)
