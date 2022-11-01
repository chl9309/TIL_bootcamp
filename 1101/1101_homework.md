1. 아래의 설명을 읽고 T/F 여부를 작성하시오.


- 동일한 요소에 v-for와 v-if 두 디렉티브가 함께 작성된 경우, 매 반복 시에 v-if의 조건문으로 요소의 렌더링 여부를 결정한다.

  - T

- v-for는 key 속성과 함께 작성하는 것을 권장한다.

  - T

- v-bind 는 HTML class 속성에서는 오직 하나의 data와 연결할 수 있다.

  - F : v-bind:class "data" 는 하나만 되지만 조건, 다중 바인딩은 여러개 가능


2. method와 computed의 개념과 그 차이에 대해서 간단히 서술하시오.

- 메서드는 뷰 인스턴스가 가지고 있는 매서드로서 매서드의 기능으로 작동하지만
컴퓨티드는 결과값을 캐싱하고 있다가 결과값이 변경될 때만 재 호출 되는 기능을 가졌다.



3. 다음은 홀수 데이터만 렌더링하는 Vue Application의 예시이다. 빈칸 (a), (b), (c)에 들어갈 코드를 작성하시오.


```html
<body>
  <div id="app">
    <div __(a)__="(num, __(b)__) in __(c)__" :key="__(b)__">
      <p>{{ num }}</p>
    </div>
  </div>

  <script src="https://cdn.jsdelivr.net/npm/vue@2/dist/vue.js"></script>
  <script>
    const app = new Vue({
      el: '#app',
      data: {
        nums: [1, 2, 3, 4, 5, 6],
      },
      computed: {
        oddNumbers: function () {
          return this.nums.filter((num) => {
            return num % 2 == 1
          })
        }
      }
    })
  </script>
</body>
```

- a = v-for

- b = nums?

- c = oddNumbers?
