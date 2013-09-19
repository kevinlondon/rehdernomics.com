from django.test import TestCase

from django.utils import timezone
from django.core.urlresolvers import reverse

from recipe.models import Recipe
#from recipes.forms import PollVoteForm


class HomePageViewTest(TestCase):
    def test_root_url_links_to_rehdernomics_and_recipes(self):
        response = self.client.get('/')

        self.assertTemplateUsed(response, 'landing_page.html')

        # Check that we have links to both.
        recipe_home = reverse("recipe-home")
        self.assertIn(recipe_home, response.content)

        rehder_home = reverse("rehdernomics-home")
        self.assertIn(rehder_home, response.content)

    def test_recipe_homepage(self):
        """Should contain the two sample entries we create."""
        self.fail()

        recipe1 = Recipe(
            title='My First recipe',
            body='This is a test recipe.',
            created=timezone.now()
        )
        recipe1.save()
        recipe2 = Recipe(
            title="life, the universe and everything",
            body="This is the body of the recipe.",
            created=timezone.now()
        )
        recipe2.save()

        response = self.client.get('/')

        # Check that we've used the right template
        self.assertTemplateUsed(response, 'home.html')

        # Check that we've passed recipes to the template
        recipes_in_context = response.context['recipes']
        self.assertEquals(list(recipes_in_context), [recipe1, recipe2])

        # Check the poll names appear on the page
        self.assertIn(recipe1.question, response.content)
        self.assertIn(recipe2.question, response.content)

        # Check that the page also contains the urls to individual recipes
        recipe1_url = reverse('recipe.views.recipe', args=[recipe1.id, ])
        self.assertIn(recipe1_url, response.content)
        recipe2_url = reverse('recipe.views.recipe', args=[recipe2.id, ])
        self.assertIn(recipe2_url, response.content)
