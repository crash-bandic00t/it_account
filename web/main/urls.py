from django.urls import URLPattern, path
from . import views


app_name = 'mainapp'
urlpatterns = [
    path('', views.index, name='index'),
]