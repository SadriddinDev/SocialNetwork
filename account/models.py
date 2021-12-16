from PIL import Image
from django.db import models
from django.contrib.auth.models import AbstractUser


class Interesting(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class User(AbstractUser):
    image = models.ImageField(upload_to="user/", null=True, blank=True)
    birthday = models.DateField(default="1990-01-01")
    interestings = models.ManyToManyField(Interesting, blank=True)

    def save(self, *args, **kwargs):
        super(User, self).save(*args, **kwargs)
        if self.image:
            img = Image.open(self.image)
            img = img.resize((500, 500), Image.ANTIALIAS)
            img.save(self.image.path)
  
    class Meta(AbstractUser.Meta):
        swappable = 'AUTH_USER_MODEL'
