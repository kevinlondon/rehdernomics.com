from django.shortcuts import render, get_object_or_404
from django.core.urlresolvers import reverse

from blog.models import Post


def home(request):
    context = {'posts': Post.objects.all()}
    return render(request, 'home.html', context)


def landing_page(request):
    return render(request, 'landing_page.html')


def tagpage(request, tag):
    posts = Post.objects.filter(tags__name=tag)
    return render(request, "blog/tagpage.html", {
        "posts": posts,
        "tag": tag
    })
