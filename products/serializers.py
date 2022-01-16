from rest_framework import serializers

from .models import Category, Card


class CardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Card
        fields = (
            'id',
            'name',
            'price',
            'get_absolute_url',
            'description',
            'get_image',
            'get_thumbnail'

        )
