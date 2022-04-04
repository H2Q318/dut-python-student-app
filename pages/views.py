from django.shortcuts import render

# Create your views here.


def home_view(request):
    context = {
        'name': 'Hung', 
        'skills': ['html', 'css', 'django'],
        'content': '<div class="alert alert-primary" role="alert">Hello Django</div>'
    }
    return render(request, 'home.html', context)


def contact_view(request):
    return render(request, 'contact.html')


def about_view(request):
    return render(request, 'about.html')
