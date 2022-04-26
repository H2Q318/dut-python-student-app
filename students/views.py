from django.shortcuts import redirect, render, get_object_or_404
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


def update_view(request, id):
    student = get_object_or_404(Student, id=id)
    form = StudentForm(request.POST or None, instance=student)
        
    if request.method == 'POST':
        form.save()
        return redirect('/students')
    
    context = {
        'form': form
    }
    return render(request, 'update.html', context)

        
def delete_view(request, id):
    student = get_object_or_404(Student, id=id)
    form = StudentForm(request.POST or None, instance=student)
        
    if request.method == 'POST':
        student.delete()
        return redirect('/students')
    
    context = {
        'student': student
    }
    return render(request, 'delete.html', context)


def detail_view(request, id):
    student = get_object_or_404(Student, id=id)
    
    context = {
        'student': student
    }
    return render(request, 'detail.html', context)


def list_view(request):
    students = Student.objects.all()
    
    context = {
        'students': students
    }
    return render(request, 'list.html', context)