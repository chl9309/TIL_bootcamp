from django.shortcuts import render

# Create your views here.
# 사용자의 모든 요청 정보가 첫번째 인자로 전달된다.
def index(request):
    # view 함수의 일은
    # 사용자 request에 대한 respone이며,
    # 일반적으로 그 응답은 html과 같은 문서를 보내주는 일이다.\
    # django MTV design pattern
    # T = template
    # templates 폴더는 모든 app들이 동일한 이름으로 사용하고 있다.
    # rkxdms rudfhrk aksemfdjwlrp ehlsek.
    
    
    return render(request, 'articles/index.html')
