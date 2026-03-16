from django.urls import path
from . import views

# url
urlpatterns = [
    path('',views.home, name='home'),
]