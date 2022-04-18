from django.urls import URLPattern, path
from main.views import views
from main.views import equipment_views, port_views


app_name = 'main'
urlpatterns = [
    path('', views.index, name='index'),
    path('<slug:autozal_slug>/', views.autozal, name='autozal'),
    path('<slug:autozal_slug>/<int:rack_number>/', views.rack, name='rack'),
    path('<slug:autozal_slug>/<int:rack_number>/<str:place>', views.equipment, name='equipment-detail'),
    path('edit/equipment-add/', equipment_views.EquipmentAddView.as_view(), name='equipment-add'),
    path('edit/equipment-update/<int:pk>/', equipment_views.EquipmentUpdateView.as_view(), name='equipment-update'),
    path('edit/equipment-delete/<int:pk>/', equipment_views.EquipmentDeleteView.as_view(), name='equipment-delete'),
    path('edit/port-update/<int:pk>', port_views.port_update, name='port-update'),
    path('edit/port-clear/', port_views.port_clear, name='port-clear'),

    path('ajax/port-dest/equip', port_views.get_equip_dropdown, name='port-dest-equip'),
    path('ajax/port-dest/ports', port_views.get_port_dropdown, name='port-dest-ports'),
]