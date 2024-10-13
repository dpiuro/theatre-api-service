from rest_framework import serializers

from theatre.models import (
    Play,
    TheatreHall,
    Performance,
    Reservation,
    Ticket,
    Actor,
    Genre
)


class ActorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = ["id", "first_name", "last_name"]


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ["id", "name"]


class PlaySerializer(serializers.ModelSerializer):
    actors = ActorSerializer(many=True)
    genres = GenreSerializer(many=True)

    class Meta:
        model = Play
        fields = ["id", "title", "description", "actors", "genres"]


class TheatreHallSerializer(serializers.ModelSerializer):
    class Meta:
        model = TheatreHall
        fields = ["id", "name", "rows", "seats_in_row"]


class PerformanceSerializer(serializers.ModelSerializer):
    play = PlaySerializer()
    theatre_hall = TheatreHallSerializer()

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


class PerformanceImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Performance
        fields = ("id", "image")
