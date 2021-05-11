from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
import director.models as theater_models
import director.serializers as theater_serializers
from django.utils import timezone

class SpectacleViewSet(viewsets.ModelViewSet):
    queryset = theater_models.Spectacle.objects.all()
    serializer_class = theater_serializers.SpectacleSerializer

class RepetitionViewSet(viewsets.ModelViewSet):
    queryset = theater_models.Repetition.objects.all()
    serializer_class = theater_serializers.RepetitionSerializer


class ActorViewSet(viewsets.ModelViewSet):
    queryset = theater_models.Actor.objects.all()
    serializer_class = theater_serializers.ActorSerializer

    @action(detail=True, methods=["GET"], url_path='repetitions', url_name="repetitions")
    def repetitions(self, request, pk=None):
        repetitions = theater_models.Repetition.objects.filter(
            spectacle_id__in=theater_models.SpectacleActors.objects.filter(actor_id=pk).values_list("spectacle_id").distinct()
        )
        answer = []
        for repetition in repetitions:
            answer.append({
                "repetition_id": repetition.id,
                "spectacle_name": repetition.spectacle_id.name,
                "spectacle_id": repetition.spectacle_id.id,
                "date": repetition.datetime.strftime("%d.%m.%Y %H:%M"),
                "type": "warning" if repetition.datetime < timezone.now() else "success"
            })
        return Response(answer)

class SpectacleActorsViewSet(viewsets.ModelViewSet):
    queryset = theater_models.SpectacleActors.objects.all()
    serializer_class = theater_serializers.SpectacleActorsSerializer
