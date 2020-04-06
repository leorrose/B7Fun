from django.test import TestCase
from postsFeed.models import PostFeed
from datetime import datetime


class PostFeedModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        PostFeed.objects.create(title = 'new post',
                                body = 'post body post body post body post body post body',
                                date = datetime.now(),
                                image = None)

    def test_postFeed_creation(self):
        self.assertTrue(isinstance(PostFeed.objects.get(title = 'new post'), PostFeed))

    def test_body(self):
        postFeed = PostFeed.objects.get(title = 'new post')
        self.assertEqual(postFeed.body, 'post body post body post body post body post body')

    def test_date(self):
        postFeed = PostFeed.objects.get(title = 'new post')
        self.assertTrue(type(postFeed.date), type(PostFeed.date))

    def test_image(self):
        postFeed = PostFeed.objects.get(title = 'new post')
        self.assertTrue(type(postFeed.image), type(PostFeed.image))
