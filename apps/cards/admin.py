from django.contrib import admin

# Register your models here.
from .models import Card


# admin.site.register(User)
@admin.register(Card)
class CardAdmin(admin.ModelAdmin):
    list_display = ("deckId", "question", "bucket")