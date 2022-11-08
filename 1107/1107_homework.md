## 1. 아래의 설명을 읽고 T/F 여부를 작성하시오.



- Vue 프로젝트에서 상태 관리를 하기 위해서는 반드시 Vuex를 설치해야 한다.

  - F : 기본적으로 props emit 을 통한 단방향 흐름 형식으로 데이터를 관리 할 수 있다.

- mutations는 반드시 state를 수정하기 위해서만 사용되어야 한다.

  - T

- mutations는 store.dispatch로, actions는 store.commit으로 호출할 수 있다.

  - F

- state는 data의 역할, getters는 computed와 유사한 역할을 담당한다.

  - T


---------
## 2. Vuex에서 State, Getters, Mutations, Actions의역할을각각서술하시오.


  - State : 

  - Getters : 

  - Mutations : 

  - Actions : 이 곳에 정의한 메서드들을 활용하여서 데이터 전처리 로직 등을 정의한다.
              mutations와는 달리 state의 값을 직접 변경하는 로직은 작성하지 않을 것이다.
              context 객체를 인자로 받아서 store.js 파일 내에 정의 된 모든 요소에 접그 할 수 있고, 메서드 호출도 가능하지만 state의 변경 요청은 mutations를 통해 진행 할 것 이다.
              actions 에서는 비동기 요청들도 같이 처리를 할 것 인데, state의 변경은 mutations를 통해서만 변경 할 것이므로, data의 예기치 못 한 변경 혹은 비동기 처리가 모두 완료되고 난 이후의 정제된 data를 mutations에게 넘기는 역할을 한다.


---------
## 3. 컴포넌트에 작성된Todo App 관련코 드를 Vuex의 Store로 옮기고자 한다. 빈 칸(a), (b), (c), (d)에 들어갈 코드를 작성하시오.



```javascript
export default {
  name: 'TodoLIst',
  data: function() {
    return {
      todoList: [],
      status: 'all',
    }
  },
  computed: {
    todoLIstByStatus: function() {
      return this.todoLIst.filter((todo) => {
        // status 값에 따라 todoList를 필터링합니다.
      })
    },
  },
  methods: {
    addTodo: function() {
      // 새로운 todo를 todoList에 추가합니다.
    },
  },
}
```
```javascript
export default net vuex.Store({
  __(a)__ {
    todoList: [],
    status: 'all',
  },
  __(b)__: {
    todoListByStatus: function(__(d)__) {
      // ...
    },
  },
  __(c)__: {
    addTodo: function(__(d)__) {
      // ...
    },
  },
})
```


- (a) : 

- (b) : 

- (c) : 

- (d) : 

---------
## 4. Vue Life Cycle Hook을 참고하여, 다음Vue application을 실행했을때, console 창에 출력되는 메시지를 작성하시오.


```vue
<script>
export default {
  name: 'HelloWorld',
  created: function () {
    console.log('crated!')
  },
  mounted: function () {
    console.log('mounted!')
  },
  updated: function () {
    console.log('updated!')
  },
};
</script>
```

```
'created!'
'mounted!'
```

- updated는 data에 변화가 발생하고나서 DOM이 변경되는 시점에 실행된다.
