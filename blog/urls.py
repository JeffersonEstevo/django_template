
from django.urls import path
from blog import views # from blog import views (mesma coisa)

# blog/
urlpatterns = [
    path('', views.blog),
    path('exemplo/', views.exemplo),
]