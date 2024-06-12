from rest_framework import serializers
from .models import Recipe
class StudenCardRepotSerializer(serializers.ModelSerializer):

    class Meta:
        model = Recipe
        fields = ("id", "name", "lastName", "picture", "level", "codeNumber", "further_details")