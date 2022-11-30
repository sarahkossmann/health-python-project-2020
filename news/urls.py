from . import views
from django.urls import path

urlpatterns = [
    path('news/', views.news, name='news'),
    path('news-detail/<int:key>/', views.news_detail, name='news-detail'),
]