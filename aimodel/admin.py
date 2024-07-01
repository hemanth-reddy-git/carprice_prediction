from django.contrib import admin
from .models import cardata

class cardataadmin(admin.ModelAdmin):
    list_display = (
        'onroad_price',
        'year',
        'km',
        'condition',
        'economy',
        'model_prediction',
    )
    search_fields = ('year','condition')

admin.site.register(cardata,cardataadmin)

# Register your models here.
