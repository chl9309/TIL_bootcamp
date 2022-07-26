## 1. Built-in 함수

Python에서 기본으로 사용할 수 있는 built-in 함수를 최소 5가지 이상 작성하시오.

> print() , input() , int() , float() , max() , min() 등

## 2. 홀수만 담기

range와 slicing을 활용하여 1부터 50까지의 숫자 중, 홀수로만 이루어진 리스트를 만드시오.

```python
lis = list(range(51))
odd_lis = lis[1::2]
print(odd_lis)
```

## 3. 반복문으로 네모 출력

두 개의 정수 n과 m이 주어졌을 때, 가로의 길이가 n, 세로의 길이가 m인 직사각형 형태를 별(*) 문자를 이용하여 출력하시오. 단, 반복문을 사용하여 작성하시오.

```python
n = 5
m = 9

for i in range(m):
    for j in range(n):
        print('*',end='')
    print('')
```

## 4. 조건 표현식

주어진 코드의 조건문을 조건 표현식으로 바꾸어 작성하시오.

```python
temp = 36.5

print('입실 불가') if temp >= 37.5 else print('입실 가능')
```

## 5. 정중앙 문자

문자열을 전달 받아 해당 문자열의 정중앙 문자를 반환하는 get_middle_char 함수를 작성하시오. 단, 문자열의 길이가 짝수일 경우에는 정중앙 문자 2개를 반환한다.

```python
def get_middle_char(x):

    if int(len(x)) % 2:

        y = int(len(x)) // 2
        return x[y]

    else:

        y = int(len(x) / 2)
        return x[y-1:y+1]


get_middle_char('ssafy') # => a

get_middle_char('coding') # => di
```

> **y = int(len(x) / 2)**  함수를 
> 
> **y = int(len(x)) / 2** 로 작성하면 동작이 되지 않았음
> 
> 실험해보니 **int자료형이 float로** 바뀌었었음
