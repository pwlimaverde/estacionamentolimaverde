from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('sistema/', include('core.urls')),
    path('admin/', admin.site.urls),
]
