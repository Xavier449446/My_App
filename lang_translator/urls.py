from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='translator-home'),
    path('about/', views.about, name='translator-about'),
    path('temp/', views.temp, name='translator-temp')
]