# pylint: disable=missing-module-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=missing-class-docstring

from django.db import models

class Reports(models.Model):

    id = models.IntegerField(primary_key=True)
    date = models.DateTimeField(auto_now_add=True, verbose_name="date")
    subject = models.CharField(max_length=255, verbose_name="subject")
    content = models.TextField(max_length=500, verbose_name="content")
    sender_email = models.EmailField(max_length=60, verbose_name="sender_email")

    class Meta:
        db_table = 'reports'
        verbose_name_plural = 'reports'

    def __str__(self):
        if len(self.content) > 50:
            return self.sender_email + ' - ' + self.content[:50] + '...'
        return self.sender_email + ' - ' + self.content
