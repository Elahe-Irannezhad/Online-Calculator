from django.urls import path, include
from django.contrib import admin

urlpatterns = [
    path('', include('calculator.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('admin/', admin.site.urls),
]
