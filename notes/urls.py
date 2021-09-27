from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('delete', views.delete, name='delete'),
    path('update', views.update, name='update'),
    path('tags', views.tags, name='tags'),
    path('filter', views.tags, name='filter'),
    path('filter_post', views.filter, name='filter_post'),
    path('filter_delete', views.filter_delete, name='filter_delete'),
    path('filter_update', views.filter_update, name='filter_update'),
]