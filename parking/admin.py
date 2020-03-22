from django.contrib import admin
from parking.models import ParkingSlot, CarInfo

# Register your models here.
admin.site.register([ParkingSlot, CarInfo])