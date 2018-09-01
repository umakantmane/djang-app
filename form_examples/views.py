from django.shortcuts import render
from form_examples.forms import EmployeeForm

def empForm(request):

    form = EmployeeForm()

    if request.method == 'POST':
        form  = EmployeeForm(request.POST)
        if form.is_valid():
            pass

    return render(request, 'emp_form.html', {'form':form})

