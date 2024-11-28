from django.contrib import admin

# Import the Profile model from the models.py file in the users directory.
from .models import Profile


# Register your models here.
admin.site.register(model_or_iterable=Profile)    
