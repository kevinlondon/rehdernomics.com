from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect

from blog.models import Post

def home(request):
    context = {'posts': Post.objects.all()}
    return render(request, 'home.html', context)


def landing_page(request):
    return render(request, 'landing_page.html')
