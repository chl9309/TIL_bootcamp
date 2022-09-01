from django.db import models

# Create your models here.

## article table 생성하기 위한 클래스 하나 정의
class Article(models.Model):
    # 제목과 내용  filed (column) 생성
    # 스키마 타이틀 50자 제한
    title = models.CharField(max_length=50)
    content = models.TextField()
