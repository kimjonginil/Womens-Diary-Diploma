from rest_framework import serializers
from article.models import Article


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ['id', 'image', 'title', 'description', 'image_url']
