from django.urls import path
from django.contrib.hello import views

app_name = 'hello'

urlpatterns = [
    path('', views.hello_world, name='hello_world'),
]
