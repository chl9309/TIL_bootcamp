
## 1. 평균 점수 구하기

key 값으로 과목명, value 값으로 점수를 가지는 dictionary를 전달 받아, 전체 과목의
평균 점수를 반환하는 함수 get_dict_avg 함수를 작성하시오.

```python

def get_dict_avg(test_score):

    score = test_score.value()
    
    result = sum(score) / len(score)

    retrun result

get_dict_avg({
'python' : 80,
'web' : 83,
'algorithm' : 90,
'django' : 89,
}) # => 85.5
```





## 2. 혈액형 분류하기


여러 사람의 혈액형(A, B, AB, O)에 대한 정보가 담긴 list를 전달 받아, key는 혈액형의
종류, value는 사람 수인 dictionary를 반환하는 count_blood 함수를 작성하시오.


```python
def count_blood(blood_list):

    blood = list(set(blood_list))
    human_count = []

    for i in range(len(blood)):

        human_count += blood_list.count(blood[i])

    for j in reange(len(blood)):

        result += {blood[j] : human_count[j]}

    return result

    

count_blood([
'A', 'B', 'A', 'O', 'AB', 'AB’,
'O', 'A', 'B', 'O', 'B', 'AB’,
]) # => {'A': 3, 'B': 3, 'O': 3, 'AB': 3}
```

------

교수님 코드


```python
def count_blood(type):
    result = {}

    for blood in type:

        if result.get(boold):
            result[blood] += 1

        else
            result(blood) = 1

    return result

```


```python

def count_blood(type):
    result = {}

    for blood in type:
        result[blood] = result.get(blood, 0) + 1
    return result

```
