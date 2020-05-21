# pylint: disable=missing-module-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=missing-class-docstring

from django.db import models

# Create your models here.
class ChatMessage(models.Model):
    id = models.IntegerField(primary_key=True)
    date = models.DateTimeField(verbose_name="Time sent", auto_now_add=True)
    message = models.TextField(verbose_name="message")
    sender_email = models.EmailField(verbose_name="sender email", max_length=60)
    chat_room_type = models.CharField(verbose_name="Chat room type", max_length=30)
    chat_room_id = models.IntegerField(verbose_name="Chat room id")

    class Meta:
        verbose_name_plural = 'Chat Messages'
        db_table = 'Chat Messages'
