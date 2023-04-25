from django.urls import path
from account import views


urlpatterns = [
    path('sign-in', views.SignIn, name='sign-in'),
    path('sign-out', views.SignOut, name='sign-out')
]
