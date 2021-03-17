from django.shortcuts import render
from rest_framework import viewsets, serializers
from .models import Deck
# Create your views here.
class DeckSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    class Meta:
        model = Deck
        fields = ['id','title', 'description']

class DeckViewSet(viewsets.ModelViewSet):
    """
    A viewset that provides the standard actions
    """
    queryset = Deck.objects.all()
    serializer_class = DeckSerializer