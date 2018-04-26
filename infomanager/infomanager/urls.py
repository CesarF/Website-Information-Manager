from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('websites/', include('websites.urls')),
    path('admin/', admin.site.urls),
]
