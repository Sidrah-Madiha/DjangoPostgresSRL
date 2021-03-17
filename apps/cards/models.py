from django.db import models
from apps.decks.models import Deck
from apps.utils.models import Timestamps


# Create your models here.
class Card(Timestamps):
    deckId = models.ForeignKey(Deck, on_delete=models.CASCADE)
    question = models.TextField()
    answer = models.TextField()
    buckets = [
        (1, '1 Day'),
        (2, '3 Days'),
        (3, '7 Days'),
        (4, '16 Days'),
        (5, '30 Days'),
    ]
    bucket = models.IntegerField(choices=buckets, default=1)
    next_reviewed_at = models.DateTimeField(auto_now_add=True)
    last_reviewed_at = models.DateTimeField(blank=True, null=True)

    # // createdAt:
    # // updatedAt:

    def __str__(self):
        return self.question
