from django.contrib import admin
from django.urls import path, include
from peminjaman.views import api_root  # <--- pastikan import dari app peminjaman

urlpatterns = [
    path('', api_root, name='api-root'),  # Root welcome page
    path('admin/', admin.site.urls),
    path('api/', include('peminjaman.urls')),  # API routes
]