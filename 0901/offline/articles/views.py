from django.shortcuts import render
from .models import Article

# Create your views here.
# 사용자의 모든 요청 정보가 첫번쨰 인자로 전달된다.
def index(request):
    # Class.manager.QuerySet API
    # Article.objects.내가 보낼 요청
    # all() -> 함수 호출
    # 함수호출? return 값이 있다.
    articles = Article.objects.all()
    context = {
        'articles': articles
    }
    # view 함수의 일은
    # 사용자 request에 대한 response이며,
    # 일반적으로 그 응답은 html과 같은 문서를 보내주는 일이다.
    # django MTV design pattern
    # T = template
    # templates 폴더는 모든 app들이 동일한 이름으로 사용하고 있다.
    # 같은 경로가 만들어지게 된다.
    # pages/templates/index.html
    # articles/templates/index.html
    # return render(request, 'templates/articles/index.html')
    return render(request, 'articles/index.html', context)

def new(request):
    return render(request, 'articles/new.html')

def create(request):
    # 사용자가 요청할떄 보낸
    # GET 방식으로 요청하면서 보낸 정보를 가져와야한다.
    # 사용자요청정보를 담고있는 request의 GET 이라고 하는 곳에 담겨있다.
    # key:value형태로 key = input tag name attrs
    title = request.GET.get('title') # input value
    content = request.GET.get('content') 
    # title과 content에 해당하는 게시글을 생성
    article = Article()
    # article 객체의 title 속성에 사용자가 입력한 제목을 담는다.
    article.title = title
    article.content = content
    # --- 이전까지는 그냥 python ---
    # db에 반영하는 행위 save() 메서드가 해줄것이다.
    article.save()

    '''
    두번째 방법
    article = Article(title=title, content=content)
    article.save()

    세번째 방법
    Article.objects.create(title=title, content=content)
    '''
    return render(request, 'articles/create.html')