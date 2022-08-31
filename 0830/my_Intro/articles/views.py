from cmath import pi
from multiprocessing import context
from django.shortcuts import render
import random

# Create your views here.
def index(request):
    # template을 = return
    return render(request, 'index.html')

def greeting (request):
    name = 'Alice'
    foods = ['파스타', '짬뽕', '비빔밥']
   
    context = {
    'name' : name,
    'foods': foods
    }
   
    return render(request, 'greeting.html', context)

def dinner (request):
    dinner = ['키보드 주문', '관리비 내기', '윈도우 설치하기']

    pick = random.choice(dinner)

    wallet = []

    context = {
    'dinner' : dinner,
    'pick' : pick
    }

    return render(request, 'dinner.html', context )

def throw(request):

    return render(request, 'throw.html')

def catch(request):
    print(dir(request))
    print(request.GET)
    print(request.GET.get('username'))
    username = request.GET.get('username')
    context = {
        'username' : username
    }

    return render(request, 'catch.html', context)



def profile(request, name):

    return(request, 'profile')