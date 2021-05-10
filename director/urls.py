from django.urls import path, include
from rest_framework import routers
import director.viewsets as therater_viewsets

router = routers.DefaultRouter()
router.register(r'spectacles', therater_viewsets.SpectacleViewSet)
router.register(r'repetitions', therater_viewsets.RepetitionViewSet)
router.register(r'actors', therater_viewsets.ActorViewSet)
router.register(r'spectacleactors', therater_viewsets.SpectacleActorsViewSet)

urlpatterns = [
    path('', include(router.urls)),
]