from django.urls import path, include

from api_v1.views import get_csrf_token_view, article_list_view, article_last_view

app_name = 'api_v1'


article_api_urls = [
    path('', article_list_view, name='article-list'),
    path('last/', article_last_view, name='article-last'),
]


urlpatterns = [
    path('csrf/', get_csrf_token_view, name='get-csrf-token'),
    path('articles/', include(article_api_urls)),
]
