1. M:N True or False
각 문항을 읽고 맞으면 T, 틀리면 F를 작성하고, 틀렸다면 그 이유도 함께 작성하시오.

1) Django에서 N:1 관계는 ForeignKeyField를 사용하고,
M:N 관계는 ManyToManyField를 사용한다.

 - T

2) ManyToManyField를 설정하고 만들어지는 테이블 이름은
“앱이름_클래스이름_지정한 필드이름”의 형태로 만들어진다. 

  - T?

3) ManyToManyField의 첫번째 인자는 참조할 모델, 
두번째 인자는 related_name이 작성 되는데 두 가지 모두 필수적으로 들어가야 한다.

  - F : 필수적이지 않다.
  - related_name 은 역참조 매니저 명이 충돌하는 경우에 한해서만 필수적으로 설정하여야하고, 그 외에는 선택적으로 ㅓㄹ정할 수 있다..
  - 역참조 매니저명이 추돌하는 경우란, 모델A의 모델 B가 이미 N:1의 광계를 맺고 있다고 가정하였을때 A와 B 간의 M:N 관계도 설정되었을 때, 모델 A가 역참조 모델인 B를 관리하는 역참조 매니저 명을 별도로 설정하지 않았을 때를 의미한다. 즉 A b_set 이 N:1 과 M:N 모두에 대한 역참조 매니저가 될 때를 말한다.

2. Like in templates
아래 빈 칸 (a)와 (b)에 들어갈 코드를 각각 작성하시오.

```python
class Article(models.Model):
    ...
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_articles')
```
```html
<!-- articles/index.html -->

{% for article in articles %}
  <p>{{ article.title }} </p>
  <form action="{% url 'articles:likes' article.pk %}" method="POST">
    {% csrf_tokken %}
    {% if __(a)__ in __(b)__ %}
      <button>좋아요 취소</button>
    {% else %}
      <button>좋아요</button>
    {% endif %}
  </form>
  <span>{{ __(b)__|length }}명이 이 글을 좋아합니다.</span>
{% endfor %}
```
- a = request.user

- b = article.like_users.all


3. Follow in views
모델 정보가 다음과 같을 때 빈칸 a, b, c, d, e에 들어갈 코드를 각각 작성하시오.

```python
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    followings = models.ManyToManyField('self', symmetrical=False, related_name='followers')
```
```python
app_name = 'accounts'
urlpatterns = [
  ...,
  path('<int:user_pk>/follow/', views.follow, name='follow'),
]
```
```python

```
- a = user_pk
- b = followers
- c = filter
- d = remove
- e = add


4. User AttributeError
다음과 같은 에러 메시지가 발생하는 이유와
이를 해결하기 위한 방법과 코드를 작성하시오. 

```python
# accounts/forms.py

from django.contrib.auth.forms import UserCreationForm


class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = UserCreationForm.Meta.Fields

```



5. related_name
아래의 경우 ForeignKey 혹은 ManyToManyField에 related_name을
필수적으로 작성해야 한다. 그 이유를 설명하시오. 


6. follow templates
person 변수에는 view함수에서 넘어온 유저 정보가 담겨 있고,
모델 정보가 아래와 같을 때
빈칸 a, b, c, d, e에 들어갈 알맞은 코드를 각각 작성하시오.

- a = person.followers.all
- b = person.followings.all
- c = request.user
- d = person
- e = person.pk
