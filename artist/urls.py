from django.urls import path
from .views import artist

urlpatterns = [
    path('artist/<name>/', artist),
]

