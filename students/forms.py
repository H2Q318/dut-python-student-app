from django import forms
from .models import Department, Student

class StudentForm(forms.ModelForm):
    code = forms.CharField(
        label='MSSV', 
        widget=forms.TextInput(attrs={'class': 'form-control'})
        )
    
    name = forms.CharField(
        required=False, 
        widget=forms.TextInput(attrs={
                'class': 'form-control', 
                'placeholder': 'Họ & tên'
            })
        )
    
    address = forms.CharField(
        initial='Vietnam', 
        widget=forms.Textarea(attrs={
                'class': 'form-control',
                'rows': '10'
            })
        )
    
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={
                'class': 'form-control'
            })
        )
    
    class Meta:
        model = Student
        fields = [
            'code',
            'name',
            'address',
            'email',
            'department',
        ]
        
    def clean_code(self, *args, **kwargs):
        code = self.cleaned_data.get('code')
        if not code.isnumeric():
            raise forms.ValidationError('Code must be numeric')
        return code
    
    def clean_email(self, *args, **kwargs):
        email = self.cleaned_data.get('email')
        if not email.endswith('dut.udn.vn'):
            raise forms.ValidationError('Email should end with dut.udn.vn')
        return email
        
class RawStudentForm(forms.Form):
    code = forms.CharField(
        label='MSSV', 
        widget=forms.TextInput(attrs={'class': 'form-control'})
        )
    name = forms.CharField(
        required=False, 
        widget=forms.TextInput(attrs={
            'class': 'form-control', 
            'placeholder': 'Họ & tên'
            })
        )
    address = forms.CharField(
        initial='Vietnam', 
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'rows': '10'
            })
        )