
1. 아래의 설명을 읽고 T/F 여부를 작성하시오.


- EventTarget.addEventListener(type, listener)에서 listener 위치에 콜백 함수를 정의한다.
이때 콜백 함수의 첫 번째 매개변수에는 발생한 이벤트에 대한 정보를 담고 있는 Event 객체가 전달된다.

- event.preventDefault 메서드를 통해 이벤트의 기본 동작을 취소할 수 있다.


2. DOM Event에는 다양한 종류의 Event가 존재한다.
아래 제시된 Event들이 각각 어떤 시점에 발생하는지 다음 [MDN 문서](https://developer.mozilla.org/ko/docs/Web/Events)를 참고하여 간단하게 작성하시오.

click, mouseover, mouseout, keydown, keyup, load, scroll, change, input

3. 다음은버튼을클릭했을때, 콘솔창을통해메시지를확인하는코드이다.
(a), (b), (c)에들어갈코드를작성하시오.

```javascript
const button = document.__(a)__('button')

button.__(b)__(__(c)__, function () {
  console.log(;Button clicked!')
})
```