from django.urls import path
from django.views.static import serve

from app import settings
from .views import ArticleListCreateView, ArticleDetailView


urlpatterns = [
    path('', ArticleListCreateView),
    path('<int:pk>', ArticleDetailView),
    path('media/<path:path>/', serve, {'document_root': settings.MEDIA_ROOT})
]
