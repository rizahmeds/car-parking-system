from django.urls import path
from parking import views

urlpatterns = [
    path('', views.parking_list, name='parkingslots'),
    path('exit_car/<str:car_number>', views.exit_car, name='exit_car'),
]