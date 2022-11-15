# HomeWork

### 아래의 설명을 읽고 T/F 여부를 작성하시오.



- 동적으로 인자를 주소로 전달했을 때 해당 변수에 접근하는 방법은 $router.params 를 이용해서 접근할 수 있다.

  - T

- 전체 route가 아닌 특정 route에 대해서만 가드를 설정하고 싶을 때 beforRouteUpdate() 를 사용한다.

  - 

- 라우터 가드의 콜백 함수의 인자는 to, from, next 에 대한 값을 인자로 받는다.

  - T

- 사용자가 요청한 리소스가 존재하지 않을 때 404 NOT FOUND 페이지를 표시할 수 있다.

  - T


### lazy loading 를 사용하는 이유를 다음 [공식 문서](https://v3.router.vuejs.org/kr/guide/advanced/lazy-loading)에서 확인하여 작성하시오.


- JavaScript 번들이 상당히 커져 페이지로드 시간에 영향을 줄 수 있습니다.

- 각 라우트의 컴포넌트를 별도의 단위로 분할하고 경로를 방문할 때 로드하는 것이 효율적이다.



### 다음은 요청하는 경로가 없을 때 Not Found 404 페이지를 보여주기 위한 코드이다. 코드의 빈 칸을 작성하시오.


```javascript
{
  path: __(a)__
  __(b)__ { name: 'NotFound404'}
},
```

- a : '*',

- b : redirect: