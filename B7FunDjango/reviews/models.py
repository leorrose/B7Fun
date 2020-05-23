# pylint: disable=missing-module-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=missing-class-docstring

from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


# Create your models here.
class Review(models.Model):
    id = models.IntegerField(primary_key=True)
    date = models.DateTimeField(auto_now_add=True, verbose_name="date")
    review_content = models.TextField(max_length=500, verbose_name="review_content")
    sender_email = models.EmailField(max_length=60, verbose_name="sender_email")
    sender_user_name = models.CharField(max_length=30, verbose_name="sender_user_name")
    rating = models.IntegerField(validators=[MaxValueValidator(5), MinValueValidator(1)], verbose_name="rating")

    class Meta:
        db_table = 'reviews'

    def __str__(self):
        if len(self.review_content) > 50:
            return self.sender_email + ' - ' + self.review_content[:50] + '...'
        return self.sender_email + ' - ' + self.review_content
