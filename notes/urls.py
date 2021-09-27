from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('delete', views.delete, name='delete'),
    path('update', views.update, name='update'),
    path('tags', views.tags, name='tags'),
    path('filter', views.tags, name='filter'),
]