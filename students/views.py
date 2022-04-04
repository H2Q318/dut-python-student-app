from django.shortcuts import render
from .models import Student

# Create your views here.

def detail_view(request):
    student = Student.objects.get(id=1)
    context = {
        'student': student
    }
    return render(request, 'detail.html', context)