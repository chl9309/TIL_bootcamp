

1. 아래의 설명을 읽고 T/F 여부를 작성 후 이유를 설명하시오.


- URI는 정보의 자원을 표현하고, 자원에 대한 행위는 HTTP Method로 표현한다.
  - T

- HTTP Method는 GET과 POST 두 종류 뿐이다.
  - F : PUT, DELETE 등의 다른 Method도 있다.

- 'https://www.fifa.com/worldcup/teams/team/43822/create/'는 계층 관계를 잘 표현한 RESTful한 URI라고 할 수 있다.
  - 


2. 다음의 HTTP status code의 의미를 간략하게 작성하시오.

- 200
- 400
- 401
- 403
- 404
- 500


3. 아래의 모델을 바탕으로 ModelSerializer인 StudentSerializer class를 작성하시오.

```python
class Student(models.Model):
  name = models.TextField()
  age = models.CharField(max_length=20)
  address = models.TextField()
```

``` python
class StudentSerializer():
    
```



4. Serializers의 의미를 DRF(Django REST Framework) [공식 문서](https://www.django-rest-framework.org/)를 참고하여 간단하게 설명하시오.
