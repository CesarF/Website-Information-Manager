from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('websites/', include('websites.urls')),
    path(r'^jet/', include('jet.urls', 'jet')),
    path(r'^jet/dashboard/', include('jet.dashboard.urls', 'jet-dashboard')),
    path('admin/', admin.site.urls),
]
