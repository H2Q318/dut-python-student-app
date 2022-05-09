from django.contrib import admin
from .models import Student, Department, Course

class StudentAdmin(admin.ModelAdmin):
    list_display = ('code', 'name', 'department')
    list_filter = ('department',)

# Register your models here.
admin.site.register(Student, StudentAdmin)
admin.site.register(Department)
admin.site.register(Course)