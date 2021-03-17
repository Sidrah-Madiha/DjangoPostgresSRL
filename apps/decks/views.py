from django.shortcuts import render
from rest_framework import viewsets, serializers
from .models import Deck
from apps.cards.views import CardSerializer
from apps.cards.models import Card
from rest_framework.response import Response
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
    def list(self, request, deckId_pk=None):
        queryset = Card.objects.filter(deckId=deckId_pk)
        serializer = CardSerializer(queryset, many=True)
        return Response(serializer.data)
