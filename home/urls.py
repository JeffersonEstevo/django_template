
from django.urls import path
from . import views 

app_name = 'home'

# home/
urlpatterns = [
    path('', views.home, name='home'),
]