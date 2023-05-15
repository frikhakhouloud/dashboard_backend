
from django.contrib import admin
from order_past.models import Order_files
from order_past.models import Order_past_per_divsion
from order_past.models import Order_past_per_organisme
from order_past.models import Order_past_per_cp
from order_past.models import Order_past_per_errors



# Register your models here.
admin.site.register(Order_files)
admin.site.register(Order_past_per_divsion)
admin.site.register(Order_past_per_organisme)
admin.site.register(Order_past_per_cp)
admin.site.register(Order_past_per_errors)

