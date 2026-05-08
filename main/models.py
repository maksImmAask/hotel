from django.db import models
from django.contrib.auth.models import User


class Room(models.Model):

    ROOM_TYPES = (
        ('single', 'Single'),
        ('double', 'Double'),
        ('lux', 'Lux'),
        ('family', 'Family'),
    )

    title = models.CharField(max_length=255)

    description = models.TextField()

    price = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    capacity = models.PositiveIntegerField()

    room_type = models.CharField(
        max_length=20,
        choices=ROOM_TYPES
    )

    is_available = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class RoomImage(models.Model):

    room = models.ForeignKey(
        Room,
        on_delete=models.CASCADE,
        related_name='images'
    )

    image = models.ImageField(upload_to='rooms/')

    def __str__(self):
        return f"Image for {self.room.title}"


class Booking(models.Model):

    BOOKING_STATUS = (
        ('pending', 'Pending'),
        ('confirmed', 'Confirmed'),
        ('cancelled', 'Cancelled'),
    )

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='bookings'
    )

    room = models.ForeignKey(
        Room,
        on_delete=models.CASCADE,
        related_name='bookings'
    )

    check_in = models.DateField()

    check_out = models.DateField()

    status = models.CharField(
        max_length=20,
        choices=BOOKING_STATUS,
        default='pending'
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.room.title}"