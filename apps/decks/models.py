from django.db import models

# Create your models here.
class Deck(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    last_reviewed_at = models.DateTimeField(null=True,blank =True)
    # createdAt:
    # updatedAt:

    def __str__(self):
        return self.title