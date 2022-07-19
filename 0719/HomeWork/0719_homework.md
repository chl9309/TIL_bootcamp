## 1. Mutable & Immutable

주어진 컨테이너들을 각각 변경 가능한 것(mutable)과
변경 불가능한 것(immutable)으로 분류하시오.

```
String , List, Tuple, Range, Set, Dictionary
```

- 변경 가능 한 것 : String , List, Tuple, Range, Set, Dictionary.key -> String, List, Tuple, set

- 변경 불가능 한 것 : Range, DIctionary -> 전원



- mutable : strng, tuple, range

- immutalbe : list, dictionary, set

## 2. Dictionary 만들기

반 학생들의 정보를 이용하여 key는 이름, value는 나이인 dictionary를 만드시오.
내 자리를 기준으로 앞, 뒤, 좌, 우에 앉아 있는 학생의 정보를 참고하시오.

```python
학생 = {'임보라' : 26 , '최창근' : 27, '한상현' : 30}
```

## 3. 평균 구하기

주어진 list에 담긴 숫자들의 평균값을 출력하시오.

```python
score = [80, 89, 99, 83]
avg = sum(score) / len(score)
```
