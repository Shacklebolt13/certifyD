from rest_framework import viewsets, serializers
from . import models


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.User
