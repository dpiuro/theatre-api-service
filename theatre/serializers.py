from rest_framework import serializers

from theatre.models import (
    Play,
    TheatreHall,
    Performance,
    Reservation,
    Ticket,
    Actor,
    Genre,
)


class PlayIDSerializer(serializers.ModelSerializer):
    class Meta:
        model = Play
        fields = ["id"]


class TheatreHallIDSerializer(serializers.ModelSerializer):
    class Meta:
        model = TheatreHall
        fields = ["id"]


class ActorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = ["id", "first_name", "last_name"]


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ["id", "name"]


class PlaySerializer(serializers.ModelSerializer):
    actors = serializers.PrimaryKeyRelatedField(
        queryset=Actor.objects.all(), many=True, required=False
    )
    genres = serializers.PrimaryKeyRelatedField(
        queryset=Genre.objects.all(), many=True, required=False
    )
    image = serializers.ImageField(max_length=None, use_url=True, required=False)

    class Meta:
        model = Play
        fields = ["id", "title", "description", "actors", "genres", "image"]


class TheatreHallSerializer(serializers.ModelSerializer):
    class Meta:
        model = TheatreHall
        fields = ["id", "name", "rows", "seats_in_row"]


class PerformanceSerializer(serializers.ModelSerializer):
    play = serializers.PrimaryKeyRelatedField(
        queryset=Play.objects
    )
    theatre_hall = serializers.PrimaryKeyRelatedField(
        queryset=TheatreHall.objects
    )

    class Meta:
        model = Performance
        fields = ["id", "play", "theatre_hall", "show_time"]


class ReservationSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()

    class Meta:
        model = Reservation
        fields = ["id", "created_at", "user"]


class TicketSerializer(serializers.ModelSerializer):
    performance = PerformanceSerializer()
    reservation = ReservationSerializer()

    class Meta:
        model = Ticket
        fields = ["id", "row", "seat", "performance", "reservation"]


class TicketCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = ("row", "seat", "performance", "reservation")


class PlayImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Play
        fields = ("id", "image")
