from django.contrib import admin
from . import models
# Register your models here.

@admin.register(models.GatherItem)
class GatherItemAdmin(admin.ModelAdmin):
    save_as = True
    list_display = (
        'pk',
        'temperature',
        'humidity',
        'bmpTemperature',
        'bmpPressure',
        'bmpAltitude',
        'concentration',
        'ugm3',
    )

    list_display_links = (
        'pk',
        'temperature',
        'humidity',
        'bmpTemperature',
        'bmpPressure',
        'bmpAltitude',
        'concentration',
        'ugm3',
    )


