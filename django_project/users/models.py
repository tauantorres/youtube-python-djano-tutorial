from typing import Any

from django.db import models
from django.contrib.auth.models import User

from PIL import Image


# Create your models here.
class Profile(models.Model):

    user = models.OneToOneField(to=User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    # file = models.FileField(default='default.txt', upload_to='profile_files')

    def save(self: "Profile", *args: Any, **kwargs: Any) -> None:
        super().save(*args, **kwargs)

        img = Image.open(fp=self.image.path)

        max_dimension = 300  # Maximum allowed dimension

        if img.height > max_dimension or img.width > max_dimension:
            scaling_factor = max_dimension / max(img.height, img.width)
            new_size = (
                int(img.width * scaling_factor),
                int(img.height * scaling_factor)
            )
            img = img.resize(size=new_size)
            img.save(fp=self.image.path, quality=95)
            

    def __str__(self: "Profile") -> str:
        return f'{self.user.username} Profile'
