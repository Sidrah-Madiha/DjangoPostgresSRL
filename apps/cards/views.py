from django.shortcuts import render
from rest_framework import viewsets, serializers
from .models import Card
from apps.decks.models import Deck
# Create your views here.
class CardSerializer(serializers.ModelSerializer):
    deckId = serializers.PrimaryKeyRelatedField(queryset=Deck.objects.all())
    class Meta:
        model = Card
        fields = ['id', 'deckId', 'question','answer','created_at', 'updated_at', 'bucket']

class CardViewSet(viewsets.ModelViewSet):
    """
    A viewset that provides the standard actions
    """
    queryset = Card.objects.all()
    serializer_class = CardSerializer