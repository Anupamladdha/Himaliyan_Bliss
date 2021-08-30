from django.contrib import admin
from .models import Room,Booking,Contact,Event
# Register your models here.
admin.site.register(Room)
admin.site.register(Booking)
admin.site.register(Contact)
admin.site.register(Event)