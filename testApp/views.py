from django.shortcuts import render

# Create your views here.


def helloDjango(request):

    return render(request, 'hello.html')


def helloPython(request):
    #print(request.method)
    #http://localhost:8000/test_app/hello_python?name=raj&email=raj@gmail.com
    print(request.GET)
    print(request.GET['email'])
    return render(request, 'hello_python.html')