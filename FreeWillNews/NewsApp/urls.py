from NewsApp import views as news_view
from userAut import views as user_views
from django.urls import path

urlpatterns = [
    path('', news_view.home, name="home" ),
    path('faq', news_view.faq, name="faq" ),
    path('contact', news_view.contact, name="contact" ),
    path('sampleNew', news_view.sampleNew, name="sampleNew" ),
]
