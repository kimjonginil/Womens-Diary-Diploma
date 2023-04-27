from django.urls import path
from tests import views


urlpatterns = [
    path('tests', views.TestsPage, name='tests'),
    path('test/<int:pk>', views.TestsDetail, name='tests-detail'),
    path('test/<int:pk>/pass', views.quiz, name='quiz'),
    path('quiz/result/<int:result_id>/', views.quiz_result, name='quiz_result'),
]
