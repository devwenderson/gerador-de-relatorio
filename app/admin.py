from django.contrib import admin
from app.models import Location, Work

@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = ['id', 'city', 'state']

@admin.register(Work)
class WorkAdmin(admin.ModelAdmin):
    list_display = ['id', 'location']
