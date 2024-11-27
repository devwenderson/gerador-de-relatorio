from django import forms
from app.models import Location, Work

class LocationForm(forms.ModelForm):
    class Meta:
        model = Location
        fields = '__all__'

class WorkForm(forms.ModelForm):
    class Meta:
        model = Work
        fields = '__all__'