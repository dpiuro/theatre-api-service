from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from django.contrib.auth import get_user_model
from django.test import TestCase
from theatre.models import Play, TheatreHall, Performance, Reservation
from theatre.serializers import PlaySerializer


class PlayApiTests(TestCase):
    def setUp(self) -> None:
        self.client = APIClient()
        self.user = get_user_model().objects.create_user(
            "test@gmail.com",
            "testpassword123"
        )
        self.play = Play.objects.create(
            title="Hamlet",
            description="A tragedy written by Shakespeare."
        )

    def test_play_list_unauthorized(self):
        url = reverse('play-list')
        response = self.client.get(url)

        plays = Play.objects.all().order_by('id')
        serializer = PlaySerializer(plays, many=True)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(serializer.data, response.data['results'])

    def test_delete_play_authorized(self):
        self.user = get_user_model().objects.create_superuser(
            "admin@gmail.com",
            "testpassword123"
        )
        self.client.force_authenticate(self.user)

        play = Play.objects.create(title="Hamlet", description="A tragedy")
        url = reverse('play-detail', args=[play.id])
        response = self.client.delete(url)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        exists = Play.objects.filter(id=play.id).exists()
        self.assertFalse(exists)


class TheatreHallApiTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.theatre_hall = TheatreHall.objects.create(
            name="Main Hall",
            rows=10,
            seats_in_row=20
        )

    def test_theatre_hall_list_unauthorized(self):
        url = reverse("theatrehall-list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_theatre_hall_detail_unauthorized(self):
        url = reverse("theatrehall-detail", args=[self.theatre_hall.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class PerformanceApiTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.play = Play.objects.create(
            title="Hamlet",
            description="A tragedy written by Shakespeare."
        )
        self.theatre_hall = TheatreHall.objects.create(
            name="Main Hall",
            rows=10,
            seats_in_row=20
        )
        self.performance = Performance.objects.create(
            play=self.play,
            theatre_hall=self.theatre_hall,
            show_time="2024-12-31T19:00:00Z"
        )

    def test_performance_list_unauthorized(self):
        url = reverse("performance-list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_performance_detail_unauthorized(self):
        url = reverse("performance-detail", args=[self.performance.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class TicketApiTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = get_user_model().objects.create_user(
            "test@gmail.com",
            "testpassword123"
        )
        self.play = Play.objects.create(
            title="Hamlet",
            description="A tragedy written by Shakespeare."
        )
        self.theatre_hall = TheatreHall.objects.create(
            name="Main Hall",
            rows=10,
            seats_in_row=20
        )
        self.performance = Performance.objects.create(
            play=self.play,
            theatre_hall=self.theatre_hall,
            show_time="2024-12-31T19:00:00Z"
        )
        self.reservation = Reservation.objects.create(user=self.user)

    def test_ticket_create_unauthorized(self):
        url = reverse("ticket-list")
        data = {
            "performance": self.performance.id,
            "row": 1,
            "seat": 1,
            "reservation": self.reservation.id
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)


class RegisterApiTests(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_user_registration(self):
        url = reverse("register-list")
        data = {
            "email": "newuser@gmail.com",
            "password": "newuserpassword123"
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(
            response.data["message"],
            "User registered successfully"
        )
