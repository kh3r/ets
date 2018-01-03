from django.contrib import admin
from inventory.models import Equipment, Calibration, Warranty

admin.site.register(Equipment)
admin.site.register(Calibration)
admin.site.register(Warranty)
