from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('lightAPI', views.lightView)
urlpatterns = [
    path(' ', include(router.urls)),
]
