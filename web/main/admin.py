from django.contrib import admin
from django.contrib.admin import ModelAdmin

from .models import Autozal,Equipment,Rack,Port,Complex, Vlan
# Register your models here.


admin.site.register(Rack)
admin.site.register(Equipment)
admin.site.register(Vlan)

@admin.register(Autozal)
class AutozalAdmin(ModelAdmin):
    fields = ['name', 'floor', 'desc']

@admin.register(Complex)
class ComplexAdmin(ModelAdmin):
    fields = ['name']

@admin.register(Port)
class PortAdmin(ModelAdmin):
    list_display = ['__str__', 'id', 'busy']