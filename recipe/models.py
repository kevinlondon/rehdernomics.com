from django import forms
from django.db import models
from django.conf import settings

from djangoratings.fields import RatingField

from .utils import unique_slugify


class Recipe(models.Model):
    """A single, self-contained recipe with ingredients."""
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=40, editable=False)
    created = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL)
    description = models.TextField()
    directions = models.TextField()
    ingredients = models.ManyToManyField('Ingredient', through="RecipeIngredient")
    image = models.ImageField(upload_to="recipes/%Y/%m/%d", null=True)
    rating = RatingField(range=3, weight=3) # 5 possible rating values, 1-5

    def __unicode__(self):
        return self.title

    @models.permalink
    def get_absolute_url(self):
        url_name = "recipe_detail"
        self.save()
        kwargs = {
            "slug": self.slug,
            "year": self.created.year,
            "month": "%02d" % self.created.month,
            "day": self.created.day,
        }
        return (url_name, (), kwargs)

    def save(self, *args, **kwargs):
        slug_str = "%s" % (self.title)
        unique_slugify(self, slug_str)
        super(Recipe, self).save()


class Ingredient(models.Model):
    """One element in a recipe."""
    name = models.CharField(max_length=100)

    def __unicode__(self):
        return "%s" % self.name


class RecipeIngredient(models.Model):
    """Contains additional information about each ingredient."""
    recipe = models.ForeignKey(Recipe)
    ingredient = models.ForeignKey(Ingredient)
    quantity = models.CharField(max_length=20)
    ingredient_state = models.CharField(max_length=30, default="", null=True)

    def __unicode__(self):
        return "%s %s %s" % (
            self.quantity, self.ingredient_state, self.ingredient
        )

    def description(self):
        return "%s %s %s" % (
            self.quantity, self.ingredient_state, self.ingredient
        )


