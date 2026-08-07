from django.db import models

# Create your models here.


class Airport(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=10, unique=True)
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name} ({self.code})"


class Flight(models.Model):
    flight_number = models.CharField(max_length=20, unique=True)
    origin = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name='departures')
    destination = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name='arrivals')
    departure_time = models.DateTimeField()
    arrival_time = models.DateTimeField()
    created_by = models.ForeignKey(
            'auth.user',
            on_delete=models.SET_NULL,
            null=True, blank=True,
            related_name='created_flights'
            )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.flight_number}: {self.origin.code} -> {self.destination.code}"

