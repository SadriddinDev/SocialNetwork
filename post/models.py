from PIL import Image
from django.db import models
from account.models import User


class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    created_at = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to="post/")
    view_count = models.IntegerField(default=0)

    def save(self, *args, **kwargs):
        super(Post, self).save(*args, **kwargs)
        img = Image.open(self.image)
        img = img.resize((500, 500), Image.ANTIALIAS)
        img.save(self.image.path)
    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    created_at = models.DateTimeField(auto_now_add=True)
    text = models.TextField(max_length=1000)


class ViewPost(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.PROTECT)
