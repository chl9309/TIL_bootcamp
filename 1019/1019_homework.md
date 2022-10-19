1. 아래의 설명을 읽고 T/F 여부를 작성하시오.

- let & const 키워드로 선언한 변수와 var 키워드로 선언한 변수의 유일한
차이점은 변수의 유효범위이다.

    - F

- “값이 없음”을 표현하는 값으로 null과 undefined 두 종류가 있으며,
둘 다 typeof 연산자에서 undefined가 반환된다.

    - F

- for ...  in 문은 배열의 요소를 직접 순회하므로 배열의 각 요소를 
활용하는 경우에 주로 활용한다.

    - F

- ‘==’ 연산자는 두 변수의 값과 타입이 같은지 비교하고 같다면 true 
아니면 false를 반환한다.

    - F

2. 아래 같이 numbers 배열이 주어졌을 때, 아래 요구사항들에 맞도록 코드를 작성하시오.

```javascript
const numbers = [1, 2, 3, 4, 5]
```

- for ... of 문을 사용하여 배열의 각 요소를 출력하시오.

```javascript
for (const i of numbers) {
    console.log(i)
}
```

- for ... of 문을 사용하여 배열의 각 요소에 10을 더한 요소들로 구성된 새로운 배열을 생성하시오.

```javascript
for (const i of numbers)
    i += 10
    console.log(i)

```

- for ... of 문을 사용하여 배열의 각 요소들 중 홀수 요소 들로만 구성된 새로운 배열을 생성하시오.

```javascript
for (const i of numbers) {
    const new_numbers = []
    if (i % 2 === 1) {
        new_nubers.append(console.log(i))
    }
}
```

- for ... of 문을 사용하여 배열의 각 요소들을 모두 더한 값을 구하시오.

```javascript
const numbers_add = 0
for (const i of numbers) {
    numbers_add += numbers
}
```
