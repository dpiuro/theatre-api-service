from django.conf import settings
from django.conf.urls.static import static
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
router.register(r"plays", PlayViewSet, basename="play")
router.register(r"theatre_halls", TheatreHallViewSet, basename="theatrehall")
router.register(r"performances", PerformanceViewSet, basename="performance")
router.register(r"reservations", ReservationViewSet, basename="reservation")
router.register(r"tickets", TicketViewSet, basename="ticket")
router.register(r"actors", ActorViewSet, basename="actor")
router.register(r"genres", GenreViewSet, basename="genre")


urlpatterns = [
    path("", include(router.urls)),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
