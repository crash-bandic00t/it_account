from django.urls import URLPattern, path
from main.views import views
from main.views import equipment_views, port_views


app_name = 'main'
urlpatterns = [
    path('', views.index, name='index'),
    path('commutation/', views.commutation, name='commutation'),
    path('<slug:autozal_slug>/', views.autozal, name='autozal'),
    path('<slug:autozal_slug>/<int:rack_number>/', views.rack, name='rack'),
    path('<slug:autozal_slug>/<int:rack_number>/<str:place>', views.equipment, name='equipment-detail'),
    path('edit/equipment-add/', equipment_views.EquipmentAddView.as_view(), name='equipment-add'),
    path('edit/equipment-update/<int:pk>/', equipment_views.EquipmentUpdateView.as_view(), name='equipment-update'),
    path('edit/equipment-delete/<int:pk>/', equipment_views.EquipmentDeleteView.as_view(), name='equipment-delete'),
    path('edit/port-update/<int:pk>', port_views.PortUpdateView.as_view(), name='port-update'),

]