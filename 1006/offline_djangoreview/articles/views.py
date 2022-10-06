from xml.etree.ElementTree import Comment
from django.shortcuts import render, redirect
from .models import Article
from .forms import ArticleForm, CommentForm

# Create your views here.
def index(request):
    # request에는 모든 요청 정보들이 들어있다.
    # path 함수에 views.index 함수 정보 넘겨 주면서
    # path 함수 내부에서 호출할 때 첫번째 인자 남겨준다.
    
    
    # 모든 게시물
    # Modesl.Manger.Query Set API
    # <Query SET [<Article object(1)>, ]>
    articles = Article.objects.all()
    context = {
        'articles': articles,
    }
    
    return render(request, 'articles/index.html', context)

def create(request):
    # 사용자가 POST 요청을 보냈다면, 게시글을 생성 해 줄 것이다.
    if request.method == 'POST':
        #사용자가 POST 요청을 보낼때 같이 보내 ㄴ정보를  model 에 대한 정보와 form 에 대한정보를
        # 모두 가지고 있ㄴ는 아티클폼 에게 사용자 요청을 같이 념겨준다
        form = ArticleForm(request.POST)
        # 사용자가 보낸 정보가 정상적인 데이터인지 확인
        if form.is_valid():
            form.save()
            return redirect('articles:index')
    else:
        form = ArticleForm()
        
    context = {
        'form' : form,
    }
    return render(request, 'articles/create.html', context)

def detail(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    form = CommentForm()
    context = {
        'article' : article,
        'form' : form,
    }

    return render(request, 'articles/detail.html', context)


def comment_create(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.article = article
            comment.save()
    
    return redirect('articles:detail', article_pk)

def deelete(request):
    pass