from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('get_query', views.get_query, name='query'),
    path('about/', views.about, name='about'),
    path('delete/<dictionary_id>', views.delete, name='delete'),
    path('content', views.content, name='content'),
]
