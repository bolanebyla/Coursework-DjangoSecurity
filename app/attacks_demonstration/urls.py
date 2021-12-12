from django.urls import path
from . import views

app_name = 'attacks_demonstration'

urlpatterns = [
    path('xss/', views.XssCreateView.as_view()),
    path('xss/<pk>/', views.XssDetailView.as_view(), name='xss_detail'),
    path('index/', views.index)
]
