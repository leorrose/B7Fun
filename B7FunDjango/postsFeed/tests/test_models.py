# pylint: disable=missing-module-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=missing-class-docstring

from datetime import datetime
from django.test import TestCase, tag
from postsFeed.models import PostFeed

@tag('unit-test')
class PostFeedModelTest(TestCase):
    def setUp(self):
        #Arrange
        self.date = datetime.today()
        self.post = PostFeed.objects.create(
            title='new post',
            body='post body post body post body post body post body',
            date=self.date,
            image="default_profile.png")

    def test_post_feed_creation(self):
        #Assert
        self.assertEqual(self.post.title, 'new post')

    def test_body(self):
        #Assert
        self.assertEqual(self.post.body, 'post body post body post body post body post body')

    def test_date(self):
        #Arrange
        self.date = datetime(2013, 11, 20, 20, 8, 7, 127325)

        #Act
        self.post.date = self.date
        self.post.save()

        #Assert
        self.assertEqual(self.date, self.post.date)

    def test_image(self):
        #Assert
        self.assertEqual(self.post.image.name, "default_profile.png")

    def test_str(self):
        #Assert
        self.assertEqual(self.post.__str__(), 'new post')
