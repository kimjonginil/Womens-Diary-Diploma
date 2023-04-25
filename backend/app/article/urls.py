from django.urls import path
from article import views


urlpatterns = [
    path('articles', views.ArticlesPage, name='articles'),
    path('article/<int:pk>', views.ArticleDetail, name='article-detail'),
    path('blog', views.BlogPage, name='blog')
]
