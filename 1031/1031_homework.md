## 1. 아래의 설명을 읽고 T/F 여부를 작성하시오.


- SPA는 Single Pattern Application의 약자이다.

  - F : Single page Application 이다.

- SPA는 웹 애플리케이션에 필요한 모든 정적 리소스를 한 번에 받고,  이후부터는 페이지 갱신에 필요한 데이터만 전달받는다.

  - T

- Vue.js에서 말하는 ‘반응형’은 데이터가 변경되면 이에 반응하여, 연결된 DOM이 업데이트 되는 것을 의미한다.

  - F : 디바이스의 변경에 따라 적절히 변경 되는 것이 반응형이다.

- v-bind 디렉티브는 “@“, v-on 디렉티브는 “:” shortcut(약어)을 제공한다.

  - F : v-bind 의 디렉티브가 ':', v-on의 디렉티브가 '@' 이다

- v-model 디렉티브는 input, textarea, select 같은 HTML 요소와 단방향 데이터 바인딩을 이루기 때문에 v-model 속성값의 제어를 통해 값을 바꿀 수 있다.

  - T



## 2. MVVM은 무엇의 약자이고, 해당 패턴에서 각 파트의 역할은 무엇인지 간단히 서술하시오.

  - MVVM은 View, Model, View Model 세 개의 약자이다.

  - View - DOM : 우리 눈에 보이는 부분을 담당한다.
  - Model - JSON : 실제 데이터를 담당한다.
  - View Model - Vue : View를 위한 Model 이다. View와 Model 사이를 연결 해주는 역할을 한다.



## 3. 다음의 빈칸 (a), (b), (c)에 들어갈 코드를 작성하시오.

```html
<div id="app">
  {{ __(a)__ }}
</div>

<script>
  const app = __(b)__({
    el: __(c)__,
    data: {
      message: 'Hello World',
    },
  })
</script>
```

  - (a) : message
  - (b) : new Vue
  - (c) : '#app'
