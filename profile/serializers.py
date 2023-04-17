
from rest_framework import serializers
from .models import UserProfile

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ('user','phone_number','gender')

        # make user field read only
        extra_kwargs = {
            'user': {'read_only': True}
        }
        