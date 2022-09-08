from django.shortcuts import render, redirect
# from .models import User
from django.contrib.auth import get_user_model
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
# from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from .forms import CustomUserCreationForm

# user 객체
User = get_user_model()

# Create your views here.
def index(request):
    # 각 app/templates/accounts/ 폴더 경로 안쪽 탐색
    # html을 사용자에게 render 해서 보내준다.
    # Article.objects.all()
    # users = UserModel.objects.all()
    users = User.objects.all() # <QuerySet <UserObject(1)>,>
    context = {
        'users': users,
    }


    return render(request, 'accounts/index.html', context)


def signup(request):
    # 회원가입이란
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        print(form)
        # 생성
        # 사용자가 보내온 요청에 따라서 (함께 보낸 정보들을 토대로) 새 유저 생성

        if form.is_valid():
            user = form.save()
            auth_login(request, user)

            # return redirect('articles :index' )
            return redirect('accounts:index')



    else:

        # 조회
        # 회원 정보를 입력해서 요청을 보낼 수 있는 form 태그가 있는 페이지가 필요하다.

        form = CustomUserCreationForm()
        print(form)

    context = {
        'form' : form
    }

    return render(request, 'accounts/signup.html', context)


def logout(request):
    auth_logout(request)

    return redirect('accounts:index')



def login(request):
    if request.method == 'POST':

        form  = AuthenticationForm(request, request.POST)
        # 사용자가 보낸 데이터를 토대로 form 설정
        # form에 들어있는 데이터 유효성 검사
            # db에 ㅓㅈ장은 -> sesstion만 할거고,
            # 그건 login 함수가 해준다.
        if form.is_valid():

            auth_login(request, form.get_user())
            return redirect('accounts:index')

    else:
        # 로그인이란..
        # 내 계정 정보를 입력하여
        # 내 서버에 나를 인증하는 페이지..
        form = AuthenticationForm() # 인증 폼

    context = {
        'form' : form
    }
    return render(request, 'accounts/login.html', context)


