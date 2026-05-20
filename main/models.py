from django.db import models
from django.contrib.auth.models import User


class Hotel(models.Model):

    title = models.CharField(max_length=255)

    description = models.TextField()

    address = models.CharField(max_length=255)

    city = models.CharField(max_length=100)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class HotelImage(models.Model):

    hotel = models.ForeignKey(
        Hotel,
        on_delete=models.CASCADE,
        related_name='images'
    )

    image = models.ImageField(upload_to='hotels/')

    def __str__(self):
        return f"Image for {self.hotel.title}"


class Room(models.Model):

    ROOM_TYPES = (
        ('economy', 'Economy'),
        ('standard', 'Standard'),
        ('comfort', 'Comfort'),
        ('deluxe', 'Deluxe'),
        ('lux', 'Lux'),
        ('full_lux', 'Full Lux'),
        ('presidential', 'Presidential'),
    )

    hotel = models.ForeignKey(
        Hotel,
        on_delete=models.CASCADE,
        related_name='rooms'
    )

    title = models.CharField(max_length=255)

    description = models.TextField()

    room_type = models.CharField(
        max_length=20,
        choices=ROOM_TYPES,
        default='standard'
    )

    price = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    capacity = models.PositiveIntegerField()

    size_m2 = models.PositiveIntegerField(
        null=True,
        blank=True
    )
    BED_TYPES = (
        ('single', 'Single'),
        ('double', 'Double'),
        ('triple', 'Triple'),
        ('queen (1 big bed for 1 person)', 'Queen (1 big bed for 1 person)'),
        ('king (bed for 4 people)', 'King (bed for 4 people)'),
    )
    beds = models.PositiveIntegerField(default=1)
    bed_type = models.CharField(
        max_length=50,
        choices=BED_TYPES,
        default='single'
    )

    has_wifi = models.BooleanField(default=True)

    has_breakfast = models.BooleanField(default=False)

    has_air_conditioning = models.BooleanField(default=True)

    is_available = models.BooleanField(default=True)

    rating = models.DecimalField(
        max_digits=3,
        decimal_places=1,
        default=4.0
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.hotel.title} - {self.title}"


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

    total_price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0
    )

    status = models.CharField(
        max_length=20,
        choices=BOOKING_STATUS,
        default='pending'
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.room.title}"

class Guest(models.Model):

    booking = models.ForeignKey(
        Booking,
        on_delete=models.CASCADE,
        related_name='guests'
    )

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    passport_number = models.CharField(max_length=100)
    national_id = models.CharField(max_length=100)

    phone_number = models.CharField(max_length=30, blank=True, null=True)
    citizenship = models.CharField(max_length=100)
    birth_date = models.DateField()

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"