from django.shortcuts import render

# Create your views here.


def index(request):
    x={'name': 'Jomanah', 'age': 25}
    return render(request, 'pages/index.html', x)

def index2(request):
    return render(request, 'pages/index2.html')