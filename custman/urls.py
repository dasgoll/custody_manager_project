from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('accounts.urls')),
    path('employees/', include('employees.urls')),
    path('admin/', admin.site.urls),
]
