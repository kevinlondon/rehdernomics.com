from django.test import TestCase
from django.core.urlresolvers import reverse

from blog.models import Post
#from posts.forms import PollVoteForm


class HomePageViewTest(TestCase):
    def test_root_url_links_to_rehdernomics_and_recipes(self):
        response = self.client.get('/')

        self.assertTemplateUsed(response, 'landing_page.html')

        # Check that we have links to both.
        blog_home = reverse("blog-home")
        self.assertIn(blog_home, response.content)

        rehder_home = reverse("rehdernomics-home")
        self.assertIn(rehder_home, response.content)

    def test_blog_homepage(self):
        """Should contain the two sample entries we create."""
        self.fail()

        post1 = Post(title='My First Post', body='This is a test post.', created=timezone.now())
        post1.save()
        post2 = Poll(title="life, the universe and everything", body="This is the body of the post.", created=timezone.now())
        post2.save()

        response = self.client.get('/')

        # Check that we've used the right template
        self.assertTemplateUsed(response, 'home.html')

        # Check that we've passed posts to the template
        posts_in_context = response.context['posts']
        self.assertEquals(list(posts_in_context), [post1, post2])

        # Check the poll names appear on the page
        self.assertIn(post1.question, response.content)
        self.assertIn(post2.question, response.content)

        # Check that the page also contains the urls to individual posts
        post1_url = reverse('blog.views.post', args=[post1.id,])
        self.assertIn(poll1_url, response.content)
        post2_url = reverse('blog.views.post', args=[post2.id,])
        self.assertIn(post2_url, response.content)
