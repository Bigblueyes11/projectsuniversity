from django.shortcuts import render

def index(request):
    data ={
        'title':'Главная страница',
        'values':['People','Car','Pizza'],
        'obj': {
            'car':'Lada',
            'name':'Ramon',
            'age':'20'
        }
    }
    return render(request, 'main/index.html', data)

def about(request):
    return render(request, 'main/about.html')