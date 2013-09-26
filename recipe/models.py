from django import forms
from django.db import models
from django.conf import settings

from .utils import unique_slugify
#from tinymce.widgets import TinyMCE
#from taggit.managers import TaggableManager


class Recipe(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=40, editable=False)
    created = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL)
    description = models.TextField()
    directions = models.TextField()
    hero_image = models.ImageField(upload_to='media')
    additional_image = models.ImageField(upload_to='media', null=True)
    #ratings = None
    #commments = None
    #tags = TaggableManager()

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
    name = models.CharField(max_length=100)

    def __unicode__(self):
        return self.name


class RecipeIngredientRequirement(models.Model):
    recipe = models.ForeignKey(Recipe)
    ingredient = models.ForeignKey(Ingredient)
    quantity = models.CharField(max_length=20)
    ingredient_state = models.CharField(max_length=30, default="")

    def __unicode__(self):
        return "%s of %s, %s" % (
            self.quantity, self.ingredient, self.ingredient_state
        )

"""
class PostAdminForm(forms.ModelForm):
    class Meta:
        model = Post
        widgets = {
            'body': TinyMCE(
                attrs={'cols': 80, 'rows': 30}
            )
        }
"""
