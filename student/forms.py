from django import forms
from student.models import Student

class StudentForm(forms.ModelForm):
    #stu_name = forms.CharField(min_length=8, max_length=20)
    stu_address  = forms.CharField(widget=forms.Textarea)
    class Meta:
        model = Student
        #fields = '__all__'
        fields = ('stu_email', 'stu_address')

