from django import forms
from parking.models import CarInfo

class CarInfoForm(forms.ModelForm):
    class Meta:
        model = CarInfo
        fields = ['car_number', 'in_time', 'out_time', 'date']
        widgets = {
            'car_number': forms.TextInput(attrs={'type': 'text', 'class': 'form-control'}),
            'in_time': forms.DateTimeInput(attrs={'class': 'form-control datetimepicker1'}),
            'out_time': forms.DateTimeInput(attrs={'class': 'form-control datetimepicker1'}),
            'date': forms.DateInput(attrs={'class': 'form-control'}),
        }