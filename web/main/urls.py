from django.urls import URLPattern, path
from . import views


app_name = 'main'
urlpatterns = [
    path('', views.index, name='index'),
    path('<slug:autozal_slug>/', views.autozal, name='autozal'),
    path('<slug:autozal_slug>/<int:rack_number>', views.rack, name='rack'),
    path('<slug:autozal_slug>/<int:rack_number>/equipment-add', views.EquipmentAddView.as_view(), name='equipment-add'),
]