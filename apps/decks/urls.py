from rest_framework import routers
from .views import DeckViewSet

router = routers.DefaultRouter()
router.register(r'', DeckViewSet)

urlpatterns = router.urls