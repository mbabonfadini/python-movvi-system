from django.contrib import admin
from django.urls import path, include


 
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('api.urls.usuario')),
    path('api/v1/', include('api.urls.filial')),
    path('api/v1/', include('api.urls.setor')),
    path('api/v1/', include('api.urls.status')),
    path('api/v1/', include('api.urls.cargo')),
    path('api/v1/', include('api.urls.role')),
    path('api/v1/', include('api.urls.usuario_role')),
    path('api/v1/', include('api.urls.tipo_senha')),
    path('api/v1/', include('api.urls.tipo_operacao_frete')),
    path('api/v1/', include('api.urls.solicitacao_tipo')),
    path('api/v1/', include('api.urls.solicitacao')),
]