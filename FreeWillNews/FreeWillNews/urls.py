from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("NewsApp.urls")),
    path('userAut/', include("userAut.urls")),
    path('userAut/', include("django.contrib.auth.urls")),
    path('staffpage/', include("staffpage.urls")),
]   
