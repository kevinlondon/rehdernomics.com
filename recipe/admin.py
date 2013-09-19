from django.contrib import admin

from .models import Recipe


class RecipePostAdmin(admin.ModelAdmin):
    """Admin class for Recipe posts."""
    search_fields = ["title"]
    #form = PostAdminForm

admin.site.register(Recipe, RecipePostAdmin)
