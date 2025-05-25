# V1_Okoyotl/urls.py

from django.contrib import admin
from django.urls import path, include

from django.http import HttpResponse

def home(request):
    return HttpResponse("Bienvenido a la API Okoyotl")

urlpatterns = [
    path('', home),
    path('admin/', admin.site.urls),
    path('', include('Okoyotl.urls')),
]

