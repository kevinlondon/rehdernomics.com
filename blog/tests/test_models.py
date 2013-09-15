from django.test import TestCase
from django.utils import timezone

from blog.models import Post

class PostModelTest(TestCase):
    def test_creating_a_new_post(self):
        # Create a new post object with its recipe.

        post = Post()
        post.title = "What's up?"
        post.body = "This is a goldarn post."
        post.created = timezone.now()

        # Check if we can save it to the db
        post.save()

        # Now check if we can find it in the db again
        all_posts_in_db = Post.objects.all()
        self.assertEqual(len(all_posts_in_db), 1)
        only_post_in_db = all_posts_in_db[0]
        self.assertEqual(only_post_in_db, post)

        # And check that it has saved its two attrbs, question and pub_date
        self.assertEqual(only_post_in_db.title, post.title)
        self.assertEqual(only_post_in_db.body, post.body)
