
from django.urls import path
from blog import views # from blog import views (mesma coisa)

app_name = 'blog'

# blog/
# Django URLs:
# https://docs.djangoproject.com/en/5.0/topics/http/urls/
urlpatterns = [
    path('', views.blog, name='home'),
    path('post/<int:id>', views.post, name='post'),
    path('exemplo/', views.exemplo, name='exemplo'),
]