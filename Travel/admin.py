from django.contrib import admin
from .models import Package
from .models import Order

# Register your models here.
admin.site.register(Package)
admin.site.register(Order)