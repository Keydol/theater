from rest_framework import serializers
import director.models as theater_models

class SpectacleSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)

    class Meta:
        model = theater_models.Spectacle
        fields = ["id", "name", "year", "budget"]


class RepetitionSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)

    class Meta:
        model = theater_models.Repetition
        fields = ["id", "spectacle_id", "datetime"]

class ActorSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)

    class Meta:
        model = theater_models.Actor
        fields = ["id", "name", "rank", "experience"]

class SpectacleActorsSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)

    class Meta:
        model = theater_models.SpectacleActors
        fields = ["id", "spectacle_id", "actor_id", "role", "contract_price", "premium"]