from django.contrib import admin
from django.contrib.admin import ModelAdmin

from .models import Autozal,Equipment,Rack,Port,Commutation
# Register your models here.


admin.site.register(Rack)
admin.site.register(Equipment)
admin.site.register(Commutation)
admin.site.register(Port)

@admin.register(Autozal)
class AutozalAdmin(ModelAdmin):
    fields = ['name', 'floor', 'desc']