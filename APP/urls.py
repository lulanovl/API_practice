from django.urls import path, include
from .views import Newton

urlpatterns = [

    path('', Newton)
]