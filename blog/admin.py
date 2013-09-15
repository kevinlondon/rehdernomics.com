from django.contrib import admin

from blog.models import Post, PostAdminForm

class BlogPostAdmin(admin.ModelAdmin):
    """Admin class for blog posts."""
    search_fields = ["title"]
    form = PostAdminForm

admin.site.register(Post, BlogPostAdmin)
