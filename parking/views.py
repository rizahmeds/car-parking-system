from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from parking.models import ParkingSlot, CarInfo
from parking.forms import CarInfoForm
from django.views.generic.list import ListView

def parking_list(request):
    parking_slots = ParkingSlot.objects.all()
    form = CarInfoForm()
    if request.method == "POST":
        add_car_info(request)
        parking_slots = ParkingSlot.objects.all()
        form = CarInfoForm()

    context = {
        'parking_slots': parking_slots,
        'form': form
    }
    return render(request, "parking/parking_list.html", context=context)

def add_car_info(request):
    empty_slot = False
    form = CarInfoForm(request.POST)
    for i in range(1,6):
        if not hasattr(ParkingSlot.objects.get(slot_no=i), 'carinfo'):
            empty_slot = ParkingSlot.objects.get(slot_no=i)
            break
    else:
        print("Parking full")
    
    if form.is_valid() and empty_slot:
        instance = form.save(commit=False)
        instance.slot = empty_slot
        instance.save()

def exit_car(request, car_number):
    obj = get_object_or_404(CarInfo, car_number=car_number)  
    obj.delete()  
    return HttpResponseRedirect("/parking") 