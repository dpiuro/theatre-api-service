from rest_framework.routers import DefaultRouter
from django.urls import path, include

from theatre.views import (
    PlayViewSet,
    TheatreHallViewSet,
    PerformanceViewSet,
    ReservationViewSet,
    TicketViewSet,
    ActorViewSet,
    GenreViewSet,
    RegisterViewSet,
)


router = DefaultRouter()
router.register(r"plays", PlayViewSet, basename="play")
router.register(r"theatre_halls", TheatreHallViewSet, basename="theatrehall")
router.register(r"performances", PerformanceViewSet, basename="performance")
router.register(r"reservations", ReservationViewSet, basename="reservation")
router.register(r"tickets", TicketViewSet, basename="ticket")
router.register(r"actors", ActorViewSet, basename="actor")
router.register(r"genres", GenreViewSet, basename="genre")
router.register(r"register", RegisterViewSet, basename="register")


urlpatterns = [
    path("", include(router.urls)),
]
