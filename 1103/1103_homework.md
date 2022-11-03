## 1. 아래의 설명을 읽고 T/F 여부를 작성하시오.


- Vue는 컴포넌트 간 양방향 데이터 흐름을 지향하기 때문에
부모, 자식 컴포넌트 간의 데이터 전달 및 수정이 자유롭다.

  - F : 부모에서 자식으로 상속시키는 방향이다

- v-on 디렉티브는 해당 요소 또는 컴포넌트에서 특정 이벤트 발생 시 전달 받은 함수를 실행한다.

  - T

- 부모 컴포넌트는 props를 통해 자식 컴포넌트에게 이벤트를 보내고,
  자식 컴포넌트는 emit을 통해 부모 컴포넌트에게 데이터를 전달한다.

  - T

## 2. Vue는 단방향 데이터 흐름을 지향하는 프론트엔드 프레임워크다. 공식문서를 참고하여 그 이유를 서술하시오. [링크](https://kr.vuejs.org/v2/guide/components.html#%EB%8B%A8%EB%B0%A9%ED%96%A5-%EB%8D%B0%EC%9D%B4%ED%84%B0-%ED%9D%90%EB%A6%84), [대체 링크](https://vue2.hphk.io/v2/guide/components-props.html#%EB%8B%A8%EB%B0%A9%ED%96%A5-%EB%8D%B0%EC%9D%B4%ED%84%B0-%ED%9D%90%EB%A6%84)


- 자식의 데이터가 부모에게 전달 되는 것을 막아 자식요소가 의도치 않게 부모 요소 상태를 변경해 혼란을 일으키는 것을 방지하기 위해


## 3. 아래와 같은 Vue 프로젝트에서 2개의 버튼이 동작하는 것을 비교하여 .native 수식어의 역할을 작성하시오.


```vue
// App.vue

<template>
  <div ind="app">
    <hello-World @click="onClick"></hello-World>
    <hello-World @click.native="onClick"></hello-World>
  </div>
</template>

<script>
import HelloWorld from '@/components/HelloWorld.vue'

export default {
  name: 'App',
  components: {
    HelloWorld,
  },
  methods: {
    onClick: function () {
      console.log('Hello!')
    }
  }
}
</script>

<style>

</style>
```
```vue
<template>
  <div>
    <button>버튼</button>
  </div>
</template>

<script>
export default {
  name: 'HelloWorld',
}
</script>
```

- .navtiv 는 



4. 다음은 자식 컴포넌트에서 이벤트를 발생시켜 부모 컴포넌트의 함수를 실행하는 코드이다. 빈칸 (a), (b), (c)에 들어갈 코드를 작성하시오.


- TodoListInput 컴포넌트의 버튼을 누르면 add-todo 이벤트가 발생한다. (이벤트 발생 시 data의 text 값도 함께 전달한다.)


- TodoList 컴포넌트에서 add-todo 이벤트를 청취하면, onAddTodo 메서드를 실행한다.


- onAddTodo 메서드에서는 TodoListInput 컴포넌트에서 전달받은 값을 console.log 함수를 통해 출력한다.


```vue
// TodoListInput.vue

<template>
  <div>
    <input type="text" v-model="inputData">
    <button @click="onClick">추가</button>
  </div>
</template>

<script>
export default {
  name: 'TodoListInput',
  data: function () {
    return {
    inputData: '',
    }
  },
  methods: {
    onClick: function () {
      __(a)__('add-todo', this.inputData)
    },
  },
}
</script>
```

```vue
// TodoList.Vue
<template>
  <div>
    <todo-list-input __(b)__></todo-list-input>
  </div>
</template>

<script>
import TodoListInput from '@/components/TodoListInput';

export default {
  name: 'MyTodoLIst',
  components: {
    TodoLIstInput,
  },
  methods: {
    __(c)__
  }
}
</script>

<style>

</style>
```

- (a) : this.$emit

- (b) : 

- (c) : 
