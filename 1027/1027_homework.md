## 1. 아래의 설명을 읽고 T/F 여부를 작성하시오.


- Event Loop는 Call Stack이 비워지면 Task Queue의 함수를 Call Stack으로 할당하는 역할을 한다.

  - T

- XMLHttpRequest(XHR)는 AJAX 요청 instance를 생성하는 Web API이다. XHR객체를 활용하여 브라우저와 서버 간의 네트워크 요청을 전송할 수 있다.

  - T

- axios는 XHR(XMLHttpRequest)을 보내고 응답 결과를 Promise 객체로 반환해주는 라이브러리이다.

  - T


## 2. 아래의 코드가 실행되었을 때 Web API, Task Queue, Call Stack 그리고 Event Loop에서 어떤 동작이 일어나는지 서술하시오.


```javascript
console.log('Hello SSAFY!')

setTimeout(function () {
  console.log('I am from setTimeout')
}, 1000)

console.log('Bye SSAFY!')
```

  - 'Hello SSAFY!'가 콜 스택에 먼저 담기고 아웃풋으로 출력 된다.
  - 그 후 setTimeout이 콜스택에 담겼다가 웹api로 옮겨간다.
  - 'Bye SSAFY!'가 콜스택에 담기고 웹api에서 시간을 쓰는 setTimeout은 계속 시간이 흐른다.
  - 'Bye SSAFY!'가 아웃풋으로 출력되고 시간이 다 경과된 setTimeout은 태스크 큐에 담겨있다가 콜 스택이 비면 콜 스택으로 옮겨진다. 그리고 내부의 'I am from setTimeout'를 아웃풋으로 출력한다.
