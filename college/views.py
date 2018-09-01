from django.shortcuts import render

from college.forms import formExample

# Create your views here.


def helloCollege(request):

    form = formExample()
    print(form)

    d1 = {
        'form':form
    }
    return render(
        request,
        'college_example.html',
        d1
    )