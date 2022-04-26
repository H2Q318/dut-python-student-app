from django.urls import path
from . import views

urlpatterns = [
    path('', views.list_view, name='list'),
    path('create', views.create_view, name='create'),
    path('<int:id>/detail', views.detail_view, name='detail'),
    path('<int:id>/update', views.update_view, name='update'),
    path('<int:id>/delete', views.delete_view, name='delete'),
]