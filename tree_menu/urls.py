from django.urls import path
from .views import test_page

urlpatterns = [
    path('', test_page, name='home'),
    path('about/', test_page, name='about'),
    path('services/', test_page, name='services'),
    path('services/consulting/', test_page, name='consulting'),
    path('services/development/', test_page, name='development'),
]
