from django.urls import URLPattern, path
from main.views import views
from main.views import equipment_views


app_name = 'main'
urlpatterns = [
    path('', views.index, name='index'),
    path('<slug:autozal_slug>/', views.autozal, name='autozal'),
    path('<slug:autozal_slug>/<int:rack_number>/', views.rack, name='rack'),
    path('edit/equipment-add/', equipment_views.EquipmentAddView.as_view(), name='equipment-add'),
    path('edit/equipment-update/<str:pk>/', equipment_views.EquipmentUpdateView.as_view(), name='equipment-update'),
    path('edit/equipment-delete/<str:pk>/', equipment_views.EquipmentDeleteView.as_view(), name='equipment-delete'),
]