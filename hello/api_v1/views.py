from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import ensure_csrf_cookie
import json

from article.models import Article


@ensure_csrf_cookie
def get_csrf_token_view(request):
    if request.method == 'GET':
        return HttpResponse()
    return HttpResponse(status=405)


def article_list_view(request):
    if request.method == 'GET':
        fields = ('id', 'title')
        articles = list(Article.objects.all().values(*fields))

        response = HttpResponse(json.dumps(articles))
        response['Content-Type'] = 'application/json'

        return response
    elif request.method == 'POST':
        article_data = json.loads(request.body)
        article = Article.objects.create(**article_data)

        return JsonResponse({'id': article.id}, status=201)


def article_last_view(request):
    if request.method != 'GET':
        return HttpResponse('Method not allowed', status=405)

    fields = ('title', 'id')
    articles_count = 3
    articles = Article.objects.all().order_by('-created_at').values(*fields)[:articles_count]
    print(list(articles))

    return JsonResponse(list(articles), safe=False)

