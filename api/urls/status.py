from django.urls import path
from api.views import StatusListView, StatusDetailView, StatusCreateView, StatusUpdateView

urlpatterns = [
    path('status/', StatusListView.as_view(), name='status-list'),
    path('status/<int:pk>/', StatusDetailView.as_view(), name='status-detail'),
    path('status/criar/', StatusCreateView.as_view(), name='status-create'),
    path('status/atualizar/<int:pk>/', StatusUpdateView.as_view(), name='status-update'),
]
