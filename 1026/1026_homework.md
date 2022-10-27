## 1. 아래의 설명을 읽고 T/F 여부를 작성하시오.


- JavaScript는 single threaded 언어로 한 번에 한 가지 일 밖에 처리하지 못한다.

  - F : 비동기식이라 동시 일 처리 가능

- setTimeout은 브라우저의 Web API를 사용하는 함수로, Web API에서 동작이 완료되면 Call Stack에 바로 할당된다.

  - T


## 2. JavaScript에서 동기와 비동기 함수의 차이점을 서술하시오.

- 동기 함수는 모든 일을 순서대로 처리하지만 비동기 함수는 앞의 순서가 끝나지 않아도 동시에 작업이 이뤄진다.
- 동기 함수는 함수의 결과를 기다리지만 비동기함수는 기다리지 않고 병렬적으로 다음 함수를 처리한다.


## 3. 다음은 axios를 사용하여 API 서버로 요청을 보내고, 정상적으로 응답이 왔을 때 응답 데이터를 출력하는 코드이다. (a), (b), (c)에 들어갈 코드를 작성하시오.


```javascript
axios.__(a)__('https://api.exapmple.com/data')
  .__(b)__(function (response) {
    console.log(__(c)__)
  })
```

  - a : get
  - b : then
  - c : response.data
