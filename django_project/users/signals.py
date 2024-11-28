from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models import Model

from .models import Profile
from typing import Type, Any


@receiver(signal=post_save, sender=User)
def create_profile(sender: Type[Model], instance: User, created: bool, **kwargs: Any) -> None:
    if created:
        Profile.objects.create(user=instance)


@receiver(signal=post_save, sender=User)
def save_profile(sender: Type[Model], instance: User, **kwargs: Any) -> None:
    instance.profile.save()
    
