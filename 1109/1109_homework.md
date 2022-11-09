### 1. 아래의 설명을 읽고 T/F 여부를 작성하시오.


- UX와 UI는 동일한 의미로 많이 사용한다.

    - F : 유저 인터페이스와 사용자 경험의 차이

- UX 는 직감으로 결정되는 것이 아니라 하나의 학문으로 연구되는 중요한 분야이다.

    - T

- URL 라우팅은 Server에서만 할 수 있으며 SPA로 개발하는 Front에서는 필요없다.

    - F : vue에서 확장을 깔면 가능

- Django의 variable routing 처럼 주소로 전달된 값을 사용할 수 있다.

    - T


### 2. Vue Router에서 설정하는 history mode가 무엇을 뜻하는지 서술하시오.

- 방문했던 페이지를 재요청이 아닌 기록으로 가지고 있던 페이지로 다시 출력 하는 것

### 3. 다음 localhost:8080/about 경로를 통하여 views/AboutView.vue 컴포넌트를 보여주기 위한 코드이다. 코드의 빈 칸 (a), (b), (c)를 채우시오.

```javascript
import Vue from 'vue'
import VueRouter from 'vue-router'
__(a)__

Vue.use(VueRouter)
const routes = [
  {
    path:__(b)__
    name: 'about',
    __(c)__: HomeView
  },

]
```

- (a) : import AboutView from '@/views/AboutView 

- (b) : '/about',

- (c) : component
