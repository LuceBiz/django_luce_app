from rest_framework import serializers
from .models import Film
from taggit.serializers import (TagListSerializerField, TaggitSerializer)

class FilmSerializer(TaggitSerializer, serializers.ModelSerializer):
    tags = TagListSerializerField()
    class Meta:
        model = Film
        fields = ('id', 'name', 'category', 'address', 'website', 'tags')


