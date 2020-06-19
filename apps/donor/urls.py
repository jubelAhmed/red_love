from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('org/', views.OrganisationView.as_view(), name='organisation'),

]
