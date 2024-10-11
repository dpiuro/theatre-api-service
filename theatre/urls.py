from rest_framework.routers import DefaultRouter
from django.urls import path, include

from theatre.views import (
    PlayViewSet,
    TheatreHallViewSet,
    PerformanceViewSet,
    ReservationViewSet,
    TicketViewSet,
    ActorViewSet,
    GenreViewSet
)


router = DefaultRouter()
router.register(r"plays", PlayViewSet)
router.register(r"theatre_halls", TheatreHallViewSet)
router.register(r"performances", PerformanceViewSet)
router.register(r"reservations", ReservationViewSet)
router.register(r"tickets", TicketViewSet)
router.register(r"actors", ActorViewSet)
router.register(r"genres", GenreViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
