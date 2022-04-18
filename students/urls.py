from django.urls import path
from . import views

urlpatterns = [
    path('create', views.create_view),
    path('detail', views.detail_view),
]
