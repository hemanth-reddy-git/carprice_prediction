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
# Register your models here along with custome interface(cardataadmin)
admin.site.register(cardata,cardataadmin)


