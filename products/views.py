from django.shortcuts import render
from .models import Card, Category
from .serializers import CardSerializer

from rest_framework.views import APIView
from rest_framework.response import responses


# Using class to get data list
class LatestCardList(APIView):
    def get(self, request, format=None):
        # load all the objects from database
        cards = Card.objects.all()[0:4]
        # creating a variable and  passing the objects query through serializer
        serializer = CardSerializer(cards, many=True)
        # returning a response with the serializer variable
        return responses(serializer.data)
