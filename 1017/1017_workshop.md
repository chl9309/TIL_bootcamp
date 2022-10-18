## 1. Model

- admin 페이지 혹은 [django-seed](https://github.com/Brobin/django-seed) 라이브러리를 활용하여 5개의 데이터를 생성한다.


## 2. serializers

- ArticleListSerializer
  - 모든 게시글 정보를 반환하기 위한 ModelSerializer
  - Id, title 필드 정의

- ArticleSerializer
  - 게시글 상세 정보를 반환 및 생성하기 위한 ModelSerializer
  - 모든 필드 정의


## 3. url & views

- GET articles/ 
  - 모든 게시글의 id와 title 컬럼을 JSON 데이터 타입으로 응답한다.

- POST articles/ 
  - 검증에 성공하는 경우 새로운 게시글의 정보를 DB에 저장하고,
    저장된 게시글의 정보를 응답한다.
  - 검증에 실패하는 경우 400 Bad Request 예외를 발생시킨다.

- GET articles/<article_pk>/ 
  - 특정 게시글의 모든 컬럼을 JSON 데이터 타입으로 응답한다.

- PUT & DELETE articles/<article_pk>/ 
  - PUT 요청인 경우 특정 게시글의 정보를 수정한다.
    - 검증에 성공하는 경우 수정된 게시글의 정보를 DB에 저장한다.
    - 검증에 실패할 경우 400 Bad Request 예외를 발생시킨다.
    - 수정이 완료되면 수정한 게시글의 정보를 응답한다.
  - DELETE 요청인 경우 특정 게시글을 삭제한다.
    - 삭제가 완료되면 삭제한 게시글의 id를 응답한다.


❖ 해당 조건을 만족하는 views.py, serializers.py 코드를 마크다운에 작성하여 제출하시오.


## views.py

```python

```


## serializers.py

```python

```