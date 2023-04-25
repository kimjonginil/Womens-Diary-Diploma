from django.urls import path
from tests import views


urlpatterns = [
    path('tests', views.TestsPage, name='tests'),
    path('test/<int:pk>', views.TestsDetail, name='tests-detail')
]
