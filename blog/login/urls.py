from django.urls import include, path
from . import views

app_name = 'login'

urlpatterns = [
    path('', views.index, name='index'),
    ]