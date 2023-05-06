from staffpage import views 
from django.urls import path

urlpatterns = [
    path('uploadnew', views.uploadnew, name="uploadnew")
]