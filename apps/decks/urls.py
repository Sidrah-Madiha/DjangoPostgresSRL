from rest_framework_nested import routers
from .views import (DeckViewSet, DeckCardViewSet, TodaysCardViewSet)
from django.urls import path, include

router = routers.SimpleRouter()
router.register('', DeckViewSet)

deck_router = routers.NestedSimpleRouter(router, '', lookup='deckId')
deck_router.register('cards', DeckCardViewSet, basename='cards')

today_router = routers.NestedSimpleRouter(router, '', lookup='deckId')
today_router.register('todays-cards', TodaysCardViewSet, basename='todays-cards')

urlpatterns = [
    path('', include(router.urls)),
    path('', include(deck_router.urls)),
    path('', include(today_router.urls)),
]

