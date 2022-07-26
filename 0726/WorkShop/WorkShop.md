# WorkShop


### 무엇이 중복일까
문자열을 전달 받아 해당 문자열에서 중복해서 나타난 문자들을 담은 list를 반환하는 duplicated_letters 함수를 작성하시오.

```python
def duplicated_letters(data):

    data_list = data.split()
    duplicated_no = []
    duplicated_yes = []

    for i in range(len(data_list)):

        for j in range(len(duplicated_no)):

            if data_list[i] == duplicated_no[j]:

                duplicated_yes.append(data_list[i])
            
            else:

                duplicated_no.append(data_list[i])

    return duplicated_yes



duplicated_letters('apple') # => ['p']
duplicated_letters('banana') # => ['a', 'n']
```

> 작동이 안되므로 수정 필요
> 이 알고리즘으론 중복이 3개 이상이면 그 중복 횟수만큼 출력을 함




### 소대소대
문자열을 전달 받아 해당 문자열을 소문자와 대문자가 번갈아 나타나도록 변환하여 반환하는 low_and_up 함수를 작성하시오. 이때, 전달 받는 문자열은 알파벳으로만 구성된다.

```python
def low_and_up(data):

    data = list(data)
    result= []

    for i in range(len(data)):
        
        j = data[i]
        
        if i % 2:
            result.append(j.upper())
            
        else:
            result.append(j.lower())
    
    return result


low_and_up('apple') # => aPpLe
low_and_up('banana') # => bAnAnA
```









### 솔로 천국 만들기
정수 0부터 9까지로 이루어진 list를 전달 받아, 연속적으로 나타나는 숫자는 하나만 남 기고 제거한 list를 반환하는 lonely 함수를 작성하시오. 이때, 제거된 후 남은 수들이 담긴 list의 요소들은 기존의 순서를 유지해야 한다.

```python
def lonely(data):

    result = []
    result.append(data[0])
    for i in range(1,len(data)):

        if i == 0:
            result.append(data[i])

        else:
            if data[i] == data[i-1]:

                pass
            else:
                result.append(data[i])

    return result



lonely([1, 1, 3, 3, 0, 1, 1]) # => [1, 3, 0, 1]
lonely([4, 4, 4, 3, 3]) # => [4, 3]
```