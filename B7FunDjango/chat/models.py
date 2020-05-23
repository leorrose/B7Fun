# pylint: disable=missing-module-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=missing-class-docstring

from django.db import models

# Create your models here.
class ChatMessage(models.Model):
    message_id = models.IntegerField(primary_key=True)
    date = models.DateTimeField(verbose_name="Time sent", auto_now_add=True)
    message = models.TextField(verbose_name="message")
    sender_email = models.EmailField(verbose_name="sender email", max_length=60)
    chat_room_type = models.CharField(verbose_name="Chat room type", max_length=30)
    chat_room_id = models.IntegerField(verbose_name="Chat room id")

    class Meta:
        verbose_name_plural = 'Chat Messages'
        db_table = 'Chat Messages'

class AbusiveChatMessage(models.Model):
    abusive_message_id = models.IntegerField(primary_key=True)
    message = models.TextField(verbose_name="message")
    sender_email = models.EmailField(verbose_name="sender email", max_length=60)

    class Meta:
        verbose_name_plural = 'Abusive Chat Messages'
        db_table = 'Abusive Chat Messages'
