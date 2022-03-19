from django.urls import path
from Shop import views


urlpatterns = [
    path('', views.home, name="home")
]
