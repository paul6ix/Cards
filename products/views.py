from django.http import Http404
from django.shortcuts import render
from .models import Card, Category
from .serializers import CardSerializer

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import viewsets


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
    def get_object(self, category, card):
        try:
            return Card.objects.filter(category__slug=category).get(slug=card)
        except Card.DoesNotExist:
            raise Http404

    def get(self, request, card, category, format=None):
        cards = self.get_object(category, card)
        serializer = CardSerializer(cards)
        return Response(serializer.data)
