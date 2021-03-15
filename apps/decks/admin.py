from django.contrib import admin

# Register your models here.
from .models import Deck

# admin.site.register(User)
@admin.register(Deck)
class DeckAdmin(admin.ModelAdmin):
    list_display = ("title", "description", "last_reviewed_at")