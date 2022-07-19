# # HomeWork



### 1. Python 예약어



- 예약어 : 파이썬 내부에 미리 정해져 있는 각종 연산자 등을 의미한다.

```python
import keyword
keyword.list
```



### 2. 실수 비교



- 부동소수점 비교는 math 패키지를 불러와서 math의  isclose라는 비교함수를 사용하여 비교한다

```python
import math
num1 = 0.1 * 3
num2 = 0.3

math.isclose(num1,num2)
```





### 3. 이스케이프 시퀀스



```python
print('\n , \t , \\')
```

1. 줄바꿈 = '\n'

2. 탭 = '\t'

3. 백슬래시 = '\\\'

 

### 4. String Interpolation



```python
name = '철수'
print('안녕, {name}야') #3.6.x이후
print('안녕, {}야'.format(name)) #3.5.x 까
```



### 5.형 변환

```python
str(1)
int('30')
int(5)
bool('50')
int('3.5)    #에러 코드
```

### 6.네모 출력

두 개의 정수 n과 m이 주어졌을 때, 가로의 길이가 n, 세로의 길이가 m인 직사각형 형태의 별(*) 문자를 이용하여 출력하시오. 단, 반복문은 사용할 수 없다.



```python
n = 5
m = 9


print((('*' * n)) + \n ) * m)
```







### 7.이스케이프 시퀀스 응용



```python
print('\"파일은 c:\\Windows\\Users\\내문서\\Python에 저장이 되었습니다.\" 나는 생각했다. \'cd를 써서 git bash로 들어가 봐야지\"')
```





### 8.근의 공식



```python
(-b + ((b**2) - 4*a*c)**(1/2)) / 2*a
(-b - ((b**2) - 4*a*c)**(1/2)) / 2*a
```








