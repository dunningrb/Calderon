from django.urls import path
from query.views import IndexView, AboutView, QueryView

app_name = 'query'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('about/', AboutView.as_view(), name='about'),
    path('query', QueryView.as_view(), name='query'),
]
