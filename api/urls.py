from django.urls import path
from . import views

urlpatterns = [
    path('/', views.students, name='students'),
    path('/<int:id>', views.studentDetail, name='studentDetail'),
]
