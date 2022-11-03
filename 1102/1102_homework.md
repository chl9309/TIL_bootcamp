
## 1. 아래의 설명을 읽고 T/F 여부를 작성하시오.



- JS 는 브라우저를 조작할 수 있는 유일한 언어이며 브라우저 밖에서 구동할 수 없다.

  - F : Node.js 로 구동 가능

- Data의 흐름을 파악하기 쉽게 하기 위해 Props & emits 를 활용하여 부모-자식간 Data를 전달한다.

  - T

- emit 은 부모 컨텐츠로의 data를 전달할 수 있으며 조상 컴포넌트로 데이터를 바로 보낼 수는 없다.

  - T


## 2. 다음 Vue component 에서 (a), (b), (c)에 알맞은 코드를 작성하시오.

```html
<template>
  <div id="app">
    <HelloWorld/>
    <h1>{{ message }}</h1>
  </div>
</template>

<script>
import __(a)__ from './components/HelloWorld.vue'


export default {
  name: 'App',
  data() {
    __(b)__ {
      message: 'Message'
    }  
  },
  __(c)__{
    HelloWorld  
  }
}
</script>
```

- (a) : HelloWorld

- (b) : components:

- (c) : methods:


## 3. 다음은 자식 컴포넌트는 부모에서 문자열 데이터가 전달되고 있다. 이 때 부모의 문자열 데이터만 전달 받고 이를 출력하기위해 빈 칸 (a), (b), (c)를 작성하시오.


```html
<template>
  <div class="hello">
    <h1>{{__(a)__}}</h1>
  </div>
</template>


<script>
export default {
  name: 'HelloSsafy',
  __(b)__ {
    msg: __(c)__
  }
}
</script>
```

- (a) : msg

- (b) : props

- (c) : String