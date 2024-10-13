from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, filters, status
from rest_framework.decorators import action
from rest_framework.permissions import IsAdminUser, IsAuthenticated
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
    GenreSerializer, PerformanceImageSerializer, TicketCreateSerializer
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


class TicketViewSet(viewsets.ModelViewSet):
    queryset = Ticket.objects.all()
    serializer_class = TicketCreateSerializer
    permission_classes = [IsAuthenticated]

    @action(detail=False, methods=['post'], url_path='book')
    def book_ticket(self, request):
        """Endpoint for booking a ticket"""
        user = request.user

        if user.is_anonymous:
            return Response({"detail": "Authentication required."}, status=status.HTTP_401_UNAUTHORIZED)

        try:
            performance_id = int(request.data.get("performance"))
            row = int(request.data.get("row"))
            seat = int(request.data.get("seat"))
        except (TypeError, ValueError):
            return Response({"detail": "Invalid input. 'performance', 'row', and 'seat' must be integers."},
                            status=status.HTTP_400_BAD_REQUEST)

        if Ticket.objects.filter(performance_id=performance_id, row=row, seat=seat).exists():
            return Response({"detail": "This seat is already booked."}, status=status.HTTP_400_BAD_REQUEST)

        reservation, created = Reservation.objects.get_or_create(user=user)

        ticket = Ticket.objects.create(
            performance_id=performance_id,
            row=row,
            seat=seat,
            reservation=reservation
        )

        serializer = TicketCreateSerializer(ticket)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class ActorViewSet(BaseViewSet):
    model = Actor
    serializer_class = ActorSerializer


class GenreViewSet(BaseViewSet):
    model = Genre
    serializer_class = GenreSerializer


class PerformanceViewSet(viewsets.ModelViewSet):
    queryset = Performance.objects.all()
    serializer_class = PerformanceSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = {'play__title': ['icontains']}

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
