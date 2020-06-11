
from django.urls import path
from . import views
urlpatterns = [
    path('', views.blood_news , name='blood_news' ),
    
]
