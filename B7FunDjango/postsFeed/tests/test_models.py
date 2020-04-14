from django.test import TestCase
from postsFeed.models import PostFeed
from datetime import datetime


class PostFeedModelTest(TestCase):
    def setUpTestData(self):
        self.date = datetime.today()
        self.post = PostFeed.objects.create(title = 'new post',
                                body = 'post body post body post body post body post body',
                                date = self.date,
                                image = "default_profile.png")

    def test_postFeed_creation(self):
        self.assertEqual(self.post.title, 'new post')

    def test_body(self):
        self.assertEqual(self.post.body, 'post body post body post body post body post body')

    def test_date(self):
        self.date = datetime.today()
        self.post.date = self.date 
        self.post.save()
        self.assertEqual(self.date, self.post.date)

    def test_image(self):
        self.assertEqual(self.post.image.name,"default_profile.png")

    def test_str(self):
        self.assertEqual(self.post.__str__(), 'new post')
