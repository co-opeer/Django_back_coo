from django.db import models


class Parking_Spot(models.Model):
    name_of_spot = models.CharField(max_length=100)
    status = models.BooleanField()
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name_of_spot} has {self.status} status. Last updated was at: {self.last_updated}."


class Parking_Statistics(models.Model):
    cars_parked = models.IntegerField()
    timestamp = models.DateTimeField()

    def __str__(self):
        return f"Number of parked cars: {self.cars_parked}, timestamp: {self.timestamp}."


class Parking_Lot(models.Model):
    current_accupancy = models.ForeignKey(Parking_Statistics, on_delete=models.CASCADE)
    parking_spot = models.ForeignKey(Parking_Spot, on_delete=models.CASCADE)

    def __str__(self):
        return f"current_accupancy: {self.current_accupancy}, parking_spot: {self.parking_spot}."
