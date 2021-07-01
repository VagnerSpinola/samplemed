from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Blog


class BlogSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.get_full_name')

    class Meta:
        model = Blog
        fields = "__all__"
