from django.urls import path,include
from .views import AudioCreateView
from rest_framework import routers

router= routers.DefaultRouter()
router.register('temp',AudioCreateView)

urlpatterns = [
    path("",include(router.urls))
]