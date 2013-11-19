from django.contrib import admin

from .models import Recipe


class RecipePostAdmin(admin.ModelAdmin):
    """Admin class for Recipe posts."""
    search_fields = ["title"]
    fields = ('title', 'image', 'description', 'directions')
    #form = PostAdminForm

    def save_model(self, request, obj, form, change): 
        obj.author = request.user
        obj.save()

    def save_formset(self, request, form, formset, change): 
        if formset.model == Recipe:
            instances = formset.save(commit=False)
            for instance in instances:
                instance.author = request.user
                instance.save()
        else:
            formset.save()

admin.site.register(Recipe, RecipePostAdmin)
