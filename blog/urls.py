
from django.urls import path
from blog import views # from blog import views (mesma coisa)

app_name = 'blog'

# blog/
urlpatterns = [
    path('', views.blog, name='home'),
    path('exemplo/', views.exemplo, name='exemplo'),
]