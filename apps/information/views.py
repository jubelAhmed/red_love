from django.shortcuts import render
from .models import BloodInformation
# Create your views here.

def blood_news(request):
    information = BloodInformation.objects.filter(status=True)
    context = {
        'information' : information,
        'nbar':'news',
    }
    return render(request,'information/news.html',context)

