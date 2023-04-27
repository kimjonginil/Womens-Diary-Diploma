import datetime

from django.core.cache import cache
from django.http import HttpResponse
from django.shortcuts import render

from account.models import User


def update_visit_duration(duration):
    today = datetime.date.today()
    key = f'visit_duration_{today}'
    total_duration = cache.get(key, 0)
    cache.set(key, total_duration + duration, 1)  # store data for 1 day
    return total_duration + duration


def get_average_visit_duration():
    today = datetime.date.today()
    key = f'visit_duration_{today}'
    total_duration = cache.get(key, 0)
    num_users = User.objects.count()
    return total_duration / num_users if num_users else 0


def update_articles_count(request):
    user_id = request.user.id
    key = f'articles_count_{user_id}'
    count = cache.get(key, 0)
    cache.set(key, count + 1, 1)  # store data for 1 day
    return count + 1


def get_average_articles_count():
    num_users = User.objects.count()
    total_count = sum(cache.get(f'articles_count_{user.id}', 0) for user in User.objects.all())
    return total_count / num_users if num_users else 0


def analytics_view(request):
    if request.user.is_superuser:
        average_visit_duration = get_average_visit_duration()
        average_articles_count = get_average_articles_count()
        context = {
            'average_visit_duration': average_visit_duration,
            'average_articles_count': average_articles_count,
        }
        return render(request, 'main/analytics.html', context)
    return HttpResponse('', status=404)
