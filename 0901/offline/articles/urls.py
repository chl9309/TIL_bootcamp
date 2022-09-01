# 경로 관리하는 파일
from django.urls import path
# django는 항상 경로를 명시적으로 표기할 것을 권장
from . import views


# app 이름 등록
# app_name 변수명은 반드시 지켜야 한다.
app_name = 'articles'

urlpatterns = [
    # 경로 이름 설정을 통해서
    # 추후에 경로가 바뀌게 되더라도 경로 이름으로 호출할 것이기 때문에
    # 불필요한 작업을 줄일 수 있다.
    path('index/', views.index, name='index'),
    # 게시글 생성 페이지
    path('new/', views.new, name='new'),
    path('create/', views.create, name='create'),
]
