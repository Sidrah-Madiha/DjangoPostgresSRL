from django.shortcuts import render
from rest_framework import viewsets, serializers
from .models import Deck
from apps.cards.views import CardSerializer
from apps.cards.models import Card
from rest_framework.response import Response
from datetime import date
# import datetime
# Create your views here.
class DeckSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    class Meta:
        model = Deck
        fields = ['id','title', 'description', 'created_at', 'updated_at']

class DeckViewSet(viewsets.ModelViewSet):
    """
    A viewset that provides the standard actions
    """
    queryset = Deck.objects.all()
    serializer_class = DeckSerializer

class DeckCardViewSet(viewsets.ViewSet):
    def list(self, request, deckId_pk):
        queryset = Card.objects.filter(deckId=deckId_pk)
        serializer = CardSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk, deckId_pk):
        queryset = Card.objects.filter(pk=pk, deckId=deckId_pk)
        serializer = CardSerializer(queryset, many=True)
        return Response(serializer.data)

class TodaysCardViewSet(viewsets.ViewSet):
    def list(self, request, deckId_pk):
        # today = datetime.date.today()
        # yesterday = today - datetime.timedelta(days=1)

        queryset = Card.objects.filter(deckId=deckId_pk, next_reviewed_at__date=date.today()) #date.today()yesterday
        # print(date.today())
        serializer = CardSerializer(queryset, many=True)
        return Response(serializer.data)