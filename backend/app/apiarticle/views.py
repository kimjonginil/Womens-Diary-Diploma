from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer, MultiPartRenderer, TemplateHTMLRenderer
from rest_framework.response import Response

from article.models import Article
from .serializers import ArticleSerializer


@csrf_exempt
@api_view(['GET', 'POST'])
@renderer_classes([JSONRenderer, MultiPartRenderer, TemplateHTMLRenderer])
def ArticleListCreateView(request):
    if request.user.is_superuser:
        if request.method == "GET":
            articles = Article.objects.all()
            serializer = ArticleSerializer(articles, many=True)
            return Response(serializer.data)

        if request.method == 'POST':
            serializer = ArticleSerializer(data=request.data, context={'request': request})
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    else:
        return HttpResponse('', status=404)


@csrf_exempt
def ArticleDetailView(request, pk):
    if request.user.is_superuser:
        try:
            article = Article.objects.get(pk=pk)
        except:
            return HttpResponse(status=404)

        if request.method == 'PUT':
            data = JSONParser().parse(request)
            serializer = ArticleSerializer(article, data=data)

            if serializer.is_valid():
                serializer.save()
                return JsonResponse(serializer.data, status=201)

            return JsonResponse(serializer.errors, status=400)
        if request.method == 'DELETE':
            article.delete()

            return HttpResponse(status=204)
    else:
        return HttpResponse(status=404)
