from django.test import TestCase
from postsFeed.models import PostFeed
from datetime import datetime


class PostFeedModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        PostFeed.objects.create(title = 'new post',
                                body = 'post body post body post body post body post body',
                                date = datetime.now(),
                                img = None)

    def test_postFeed_creation(self):
        postFeed = self.setUpTestData()
        self.assertTrue(isinstance(postFeed, PostFeed))


 #   def test_body(self):
 #       postFeed = PostFeed.objects.get(title = 'new post')
 #       self.assertEqual(postFeed.body, 'post body post body post body post body post body')

 #   def test_date(self):
 #       postFeed = PostFeed.objects.get(title = 'new post')
 #       self.assertEqual(postFeed.date, datetime.now())

 #   def test_title(self):
 #       postFeed = PostFeed.objects.get(title = 'new post')
 #       self.assertEqual(postFeed.img, None)

