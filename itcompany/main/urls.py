from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'), # type: ignore
    path('contact/', views.contact, name='contact'), # type: ignore
    path('contact/success/', views.contact_success, name='contact_success'), # type: ignore
]