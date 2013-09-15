from django.conf.urls import patterns, url
from django.views.generic import ListView, DetailView
from django.contrib.syndication.views import Feed

from blog.models import Post


class BlogFeed(Feed):
    title = "Kevin London's Blog"
    description = "Programming, film, etc."
    link = "/blog/feed"

    def items(self):
        return Post.objects.all().order_by("-created")[:5]

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.body

    def item_link(self, item):
        return u"/blog/%d" % item.id


urlpatterns = patterns('blog.views',
    #url(r'^$', 'home', name="blog-home"),
    url(r'^$', ListView.as_view(
                 queryset=Post.objects.all().order_by("-created"),
                 template_name="blog/list.html",
                 paginate_by = 3,
                 )),
    url(r'^(?P<year>\d{4})/(?P<day>\d{1,2})/(?P<slug>[-\w]+)/$',
                 view=DetailView.as_view(
                        model=Post, template_name="blog/post.html"
                        ),
                 name='blog_post_detail'),
    url(r'^archive/$', ListView.as_view(
                 queryset=Post.objects.all().order_by("-created"),
                 template_name="blog/archives.html")),
    url(r'^tag/(?P<tag>\w+)$', 'tagpage'),
    url(r'^feed/$', BlogFeed()),
)
