from rest_framework_nested import routers
from .views import (DeckViewSet, DeckCardViewSet)
from django.urls import path, include

router = routers.SimpleRouter()
router.register('', DeckViewSet)

deck_router = routers.NestedSimpleRouter(router, '', lookup='deckId')
deck_router.register('cards', DeckCardViewSet, basename='cards')

urlpatterns = [
    path('', include(router.urls)),
    path('', include(deck_router.urls)),
]

