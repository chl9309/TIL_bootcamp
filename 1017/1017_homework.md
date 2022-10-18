## 1. 아래의 설명을 읽고 T/F 여부를 작성 후 이유를 설명하시오.


- JSON 포맷의 데이터로 응답하기 위해서는 반드시 DRF를 사용해야 한다.
    - F : DRF는 사용하기 편하게 해주는 프레임워크지 필수는 아니다.
        - django가 기본적ㅇ로 제공해주는 core를 활용하여서도 직렬화 가능하며,
        JSON으로 응답하기 위한 JSON Response도 제공한다.

- DRF가 제공하는 기본 Form을 통해서만 여러 HTTP Method를 테스트 해볼 수 있다.
    - F : DRF를 사용하지 않는 기존 방식으로도 테스트가 가능하다.
        - DRF는 FORM을 제공합니다. 각 요청 하단에 어떤 요청들을 보낼 것 인지 method 별로 처리 가능하다.
        - 단, POST Man이라는 응용프로그램을 통해서 요청 보낼 수도 있고 python requests 사용해서도 보내 볼 수 있다.

- api_view 데코데이터에 작성되지 않은 HTTP Method 요청에 대해서 “500 Internal Server Error” 를 응답한다.
    - F
        - 405 Method not Allowed

- Serializers는 Queryset 객체를 JSON 포맷으로 변환 할 수 있는 python 데이터 타입으로 만들어준다.
    - T


## 2. REST API 디자인 가이드

REST API 디자인 설계 시 가장 중요한 항목을 2가지로 요약한다면,
“정보의 자원을 표현해야 하는 __(a)__와
자원의 대한 행위를 표현하는__(b)__”라고 할 수 있다.”
빈칸 a, b에 들어갈 알맞은 답을 작성하시오.

    - a : URI
    - b : HTTP Method


## 3. 아래에서 빈칸 a, b, c, d, e 에 들어갈 코드를 작성하시오.

해당 view 함수는 유효성 검사를 통과 했을 경우
serializer 데이터와 http status code 201를 반환하며,
유효성 검사를 통과하지 못했을 경우 http status code 400을 반환한다.

```python
from rest_framework import status


@api_view(__(a)__)
def create_article(request):
    serializer = ArticleSerializer(__(b)__)
    if serializer.is_valid(__(c)__):
        serializer.save()
        return Response(__(d)__, __(e)__)
```

    - a : ['POST']
    - b : data=request.data
    - c : raise_exception=True
    - d : serializer.errors
    - e : status=status.HTTP_400_BAD_REQUEST
