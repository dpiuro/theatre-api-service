from rest_framework import viewsets, filters, status
from rest_framework.decorators import action
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response

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
    GenreSerializer, PerformanceImageSerializer
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


class PerformanceViewSet(viewsets.ModelViewSet):
    queryset = Performance.objects.all()
    serializer_class = PerformanceSerializer

    @action(
        methods=["POST"],
        detail=True,
        url_path="upload-image",
        permission_classes=[IsAdminUser],
    )
    def upload_image(self, request, pk=None):
        performance = self.get_object()
        serializer = PerformanceImageSerializer(performance, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
