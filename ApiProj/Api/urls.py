
from django.urls import path
from .views import TodoApi

urlpatterns = [
    path('api/', TodoApi.as_view()),
    
]
