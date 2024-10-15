from django.db import models
from django.contrib.auth import get_user_model
from rest_framework.exceptions import ValidationError


class Actor(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Genre(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Play(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    actors = models.ManyToManyField(Actor, related_name="plays")
    genres = models.ManyToManyField(Genre, related_name="plays")
    image = models.ImageField(upload_to="plays/", blank=True, null=True)

    def __str__(self):
        return self.title


class TheatreHall(models.Model):
    name = models.CharField(max_length=255)
    rows = models.IntegerField()
    seats_in_row = models.IntegerField()

    def __str__(self):
        return self.name


class Performance(models.Model):
    play = models.ForeignKey(
        Play, on_delete=models.CASCADE, related_name="performances"
    )
    theatre_hall = models.ForeignKey(
        TheatreHall, on_delete=models.CASCADE, related_name="performances"
    )
    show_time = models.DateTimeField()

    def __str__(self):
        return (
            f"{self.play.title} in {self.theatre_hall.name} "
            f"" f"on {self.show_time}"
        )


class Reservation(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name="reservations"
    )

    def __str__(self):
        return f"Reservation by {self.user} on {self.created_at}"


class Ticket(models.Model):
    row = models.IntegerField()
    seat = models.IntegerField()
    performance = models.ForeignKey(
        Performance, on_delete=models.CASCADE, related_name="tickets"
    )
    reservation = models.ForeignKey(
        Reservation, on_delete=models.CASCADE, related_name="tickets"
    )

    def __str__(self):
        return (
            f"Ticket {self.row}-{self.seat} "
            f"for " f"{self.performance.play.title}"
        )

    def clean(self):
        if Ticket.objects.filter(
            performance=self.performance, row=self.row, seat=self.seat
        ).exists():
            raise ValidationError(
                f"Seat {self.row}-{self.seat} "
                f"for this performance is already booked."
            )

        if self.row > self.performance.theatre_hall.rows or self.row < 1:
            raise ValidationError(
                f"Row {self.row} is out of range for this theatre hall."
            )

        if (
                self.seat > self.performance.theatre_hall.seats_in_row
                or self.seat < 1
        ):
            raise ValidationError(
                f"Seat {self.seat} is out of range for this theatre hall."
            )

    def save(self, *args, **kwargs):
        self.clean()
        super().save(*args, **kwargs)
