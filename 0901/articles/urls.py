# 경로 관리하는 파일
from django.urls import path
# django는 항상 경로를 명시적으로 ㅍ기할 것을 권장
from . import views


# app 이름 등록
# app_name 변수명은 반드시 지켜야 한다.
app_name = 'articles'


urlpatterns = [
     path('index/', views.index, name='index')
]
