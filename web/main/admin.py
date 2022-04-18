from django.contrib import admin
from django.contrib.admin import ModelAdmin

from .models import Autozal,Equipment,Rack,Port,Category
# Register your models here.


admin.site.register(Rack)
admin.site.register(Equipment)

@admin.register(Autozal)
class AutozalAdmin(ModelAdmin):
    fields = ['name', 'floor', 'desc']

@admin.register(Category)
class CategoryAdmin(ModelAdmin):
    fields = ['name']

@admin.register(Port)
class PortAdmin(ModelAdmin):
    list_display = ['__str__', 'id', 'busy']