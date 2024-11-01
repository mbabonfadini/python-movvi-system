from django.contrib import admin
from django.urls import path, include


 
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('api.urls.usuario')),
    path('api/v1/', include('api.urls.filial')),
    path('api/v1/', include('api.urls.setor')),
]