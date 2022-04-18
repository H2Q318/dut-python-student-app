from django.shortcuts import render
from .models import Student
from .forms import StudentForm, RawStudentForm

# Create your views here.

# def create_view(request):
#     my_form = RawStudentForm()
    
#     if request.method == 'POST':
#         my_form = StudentForm(request.POST)
#         if my_form.is_valid():
#             print(my_form.cleaned_data)
#             Student.objects.create(**my_form.cleaned_data)    
#         else:
#             print(my_form.errors)    
    
#     context = {
#         'form': my_form
#     }
#     return render(request, 'create.html', context)


# def create_view(request):
#     if request.method == 'POST':
#         new_code = request.POST.get('code')
#         print(new_code)
#         # Student.objects.create(code=new_code)    
#     context = {}
#     return render(request, 'create.html', context)


def create_view(request):
    form = StudentForm(request.POST or None)
        
    if form.is_valid():
        form.save()
        form = StudentForm
    
    context = {
        'form': form
    }
    return render(request, 'create.html', context)


def detail_view(request):
    student = Student.objects.get(id=1)
    context = {
        'student': student
    }
    return render(request, 'detail.html', context)