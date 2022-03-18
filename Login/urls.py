from django.urls import path
from Login import views
app_name = 'Login'
urlpatterns = [
    path('register/', views.register, name="register"),
]
