from django.db import models
from django import forms

class ParkingSlot(models.Model):
    slot_no = models.IntegerField(primary_key=True)

    def __str__(self):
       return str(self.slot_no)


class CarInfo(models.Model):
    slot = models.OneToOneField(ParkingSlot, on_delete=models.CASCADE)
    car_number = models.CharField(max_length=20, primary_key=True)
    in_time = models.DateTimeField(auto_now=False, auto_now_add=False)
    out_time = models.DateTimeField(auto_now=False, auto_now_add=False)
    date = models.DateField(auto_now=False, auto_now_add=False)

    def __str__(self):
        return str(self.car_number)