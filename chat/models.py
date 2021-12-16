from django.db import models
from account.models import User


class Chat(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    user_1 = models.ForeignKey(
        User, on_delete=models.PROTECT, related_name="User_1")
    user_2 = models.ForeignKey(
        User, on_delete=models.PROTECT, related_name="User_2")

    def __str__(self):
        return f"{self.id}-chat"


class Message(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    chat = models.ForeignKey(Chat, on_delete=models.PROTECT)
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    text = models.TextField(max_length=2048)
