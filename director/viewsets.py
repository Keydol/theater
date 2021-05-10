from rest_framework import viewsets
from rest_framework.decorators import action
import director.models as theater_models
import director.serializers as theater_serializers

class SpectacleViewSet(viewsets.ModelViewSet):
    queryset = theater_models.Spectacle.objects.all()
    serializer_class = theater_serializers.SpectacleSerializer

class RepetitionViewSet(viewsets.ModelViewSet):
    queryset = theater_models.Repetition.objects.all()
    serializer_class = theater_serializers.RepetitionSerializer


class ActorViewSet(viewsets.ModelViewSet):
    queryset = theater_models.Actor.objects.all()
    serializer_class = theater_serializers.ActorSerializer


class SpectacleActorsViewSet(viewsets.ModelViewSet):
    queryset = theater_models.SpectacleActors.objects.all()
    serializer_class = theater_serializers.SpectacleActorsSerializer
