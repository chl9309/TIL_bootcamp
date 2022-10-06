from django import forms
from .models import Article, Comment

class ArticleForm(forms.ModelForm):
    
    # ArticleForm class 가 어떻게 정의 되는지
    # 그 정보는 Meta class에 넣는다
    class Meta:
        model = Article
        fields = '__all__'

class CommentForm(forms.ModelForm):
    
    class Meta:
        model = Comment
        # field = '__all__'
        exclude = ('article', )