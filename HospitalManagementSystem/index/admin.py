from django.contrib import admin
from .models import Invoice,Prescription,Appointments

# Register your models here.

admin.site.register(Invoice)
admin.site.register(Prescription)
admin.site.register(Appointments)