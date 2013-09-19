from django.db import models
from django import forms

from recipe.utils import unique_slugify
#from tinymce.widgets import TinyMCE
#from taggit.managers import TaggableManager


class Recipe(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=40, editable=False)
    description = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    #creator = Person
    #ingredients = None
    #directions = None
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
            "day": str(self.created.day),
        }
        return (url_name, (), kwargs)

    def save(self, *args, **kwargs):
        slug_str = "%s" % (self.title)
        unique_slugify(self, slug_str)
        super(Recipe, self).save()


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
