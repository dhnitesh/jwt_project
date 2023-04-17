from django.contrib import admin

# Register your models here.
# UserProfile
from .models import UserProfile
admin.site.register(UserProfile)