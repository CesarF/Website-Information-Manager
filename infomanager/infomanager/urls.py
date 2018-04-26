from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('sites/', include('websites.urls')),
    path('admin/', admin.site.urls),
]
