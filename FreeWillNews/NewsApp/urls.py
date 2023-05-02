from NewsApp import views
from django.urls import path

urlpatterns = [
    path('', views.home, name="home" ),
    path('faq', views.faq, name="faq" ),
    path('contact', views.contact, name="contact" ),
    path('login', views.login, name="login" ),
    path('sampleNew', views.sampleNew, name="sampleNew" ),
]
