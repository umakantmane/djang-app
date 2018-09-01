from django.shortcuts import render, redirect,HttpResponse
from student.forms import StudentForm
from student.models import Student
from django.contrib.auth.decorators import login_required

@login_required(login_url='/sites/signin')
def create(request):

    form = StudentForm()
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            #form.save()
            stu = Student()
            stu.stu_name = form.cleaned_data['stu_email'].split('@')[0]
            stu.stu_email = form.cleaned_data['stu_email']
            stu.stu_address = form.cleaned_data['stu_address']
            stu.save()
            return  redirect(index)

    return render(request, 'stu/create.html',{'form':form})

@login_required(login_url='/sites/signin')
def index(request):

    #return HttpResponse("<html></html>")
    data = Student.objects.all()
    return render(request, 'stu/index.html',{'data':data})

def update(request, id):

    data = Student.objects.get(id=id)

    form = StudentForm(instance=data)
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=data)
        if form.is_valid():
            #form.save()
            stu = Student()
            stu.id = id
            stu.stu_name = form.cleaned_data['stu_email'].split('@')[0]
            stu.stu_email = form.cleaned_data['stu_email']
            stu.stu_address = form.cleaned_data['stu_address']
            stu.save()
            return redirect(index)

    return render(request, 'stu/update.html', {'form': form})


def delete(request, id):
    data = Student.objects.get(id=id)
    data.delete()
    return redirect(index)

def view(request, id):

    data = Student.objects.get(id=id)
    #select * from student where id=id
    return render(request, 'stu/view.html', {'data':data})