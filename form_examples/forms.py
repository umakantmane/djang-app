from django import forms
from django.core.validators import ValidationError

def validateName(value):
    if value.isdigit():
        raise ValidationError('Digits not allowed!')

def validateEmail(email):
    if email.split('@')[1] != 'mytectra.com':
        raise ValidationError('Invalid email!')

class EmployeeForm(forms.Form):

    city_data = (
        ('', '--Select options--'),
        ('bng','Bangalore1'),
        ('Pune', 'Pune'),
        ('Mysore', 'Mysore'),
        ('Hyderabad', 'Hyderabad'),
        ('Chennai', 'Chennai'),
    )
    gn = (
        ('m', 'Male'),
        ('f', 'Female')
    )

    is_active = forms.CharField(widget=forms.CheckboxInput)
    gender = forms.ChoiceField(choices=gn, widget=forms.RadioSelect)
    emp_name = forms.CharField(
        min_length=8,
        max_length=20,
        label='Employee Name',
        error_messages={
            'required':'Employee name cannot blank!',
            'min_length':'new error message'
        }
    )
    emp_email = forms.EmailField()
    emp_address = forms.CharField(widget=forms.Textarea)
    emp_city = forms.ChoiceField(choices=city_data)
    password1 = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput)
    pincode = forms.RegexField(regex='([0-9]+){6,}')
    file = forms.FileField()

    def clean(self):

        form_data = self.cleaned_data

        if 'emp_name' in form_data:
            if form_data['emp_name'].isdigit():
                self.errors['emp_name'] = ['Invalid name!']

        if 'emp_email' in form_data:
            if form_data['emp_email'].split('@')[1] !='mytectra.com':
                self.errors['emp_email'] = ['invalid email!']

        if 'password1' in form_data and 'password2' in form_data:

            if form_data['password1'] != form_data['password2']:
                self.errors['password1'] = ['password mismatch!']

        return form_data

