from django.urls import path
from analytics import views


urlpatterns = [
    path('', views.analytics_view, name='analytics')
]