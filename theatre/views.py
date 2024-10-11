from rest_framework import viewsets
from theatre.models import (
    Play,
    TheatreHall,
    Performance,
    Reservation,
    Ticket,
    Actor,
    Genre
)
from theatre.serializers import (
    PlaySerializer,
    TheatreHallSerializer,
    PerformanceSerializer,
    ReservationSerializer,
    TicketSerializer,
    ActorSerializer,
    GenreSerializer
)


class BaseViewSet(viewsets.ModelViewSet):
    model = None
    serializer_class = None

    def get_queryset(self):
        return self.model.objects.all()

class PlayViewSet(BaseViewSet):
    model = Play
    serializer_class = PlaySerializer

class TheatreHallViewSet(BaseViewSet):
    model = TheatreHall
    serializer_class = TheatreHallSerializer

class PerformanceViewSet(BaseViewSet):
    model = Performance
    serializer_class = PerformanceSerializer

class ReservationViewSet(BaseViewSet):
    model = Reservation
    serializer_class = ReservationSerializer

class TicketViewSet(BaseViewSet):
    model = Ticket
    serializer_class = TicketSerializer

class ActorViewSet(BaseViewSet):
    model = Actor
    serializer_class = ActorSerializer

class GenreViewSet(BaseViewSet):
    model = Genre
    serializer_class = GenreSerializer
