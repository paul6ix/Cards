from django.http import Http404
from django.shortcuts import render
from .models import Card, Category
from .serializers import CardSerializer

from rest_framework.views import APIView
from rest_framework.response import Response


# Using class to get data list
class LatestCardList(APIView):
    def get(self, request, format=None):
        # load all the objects from database
        cards = Card.objects.all()[0:4]
        # creating a variable and  passing the objects query through serializer
        serializer = CardSerializer(cards, many=True)
        # returning a response with the serializer variable
        return Response(serializer.data)


class CardDetail(APIView):
    def get_object(self, card_slug, category_slug):
        try:
            return Card.objects.filter(category_slug=category_slug).get(slug=card_slug)
        except Card.DoesNotExist:
            raise Http404

    def get(self, card_slug, category_slug, format=None):
        cards = Card.objects.get(category_slug, card_slug)
        serializer = CardSerializer(cards)
        return Response(serializer.data)
