from django.urls import path
from . import views

app_name = 'news'

urlpatterns = [
    path('create/', views.NewsCreateView.as_view(), name='create'),
    path('', views.NewsListView.as_view(), name='list'),
]
