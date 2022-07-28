# HomeWork

### Type Class
Python은 객체 지향 프로그래밍 언어이다. Python에서 기본적으로 정의되어 있는 클래스를 최소 5가지 이상 작성하시오.

1. class int
2. class str
3. class float
4. class complex
5. class bool


### Magic Method
아래에 제시된 매직 메서드들이 각각 어떠한 역할을 하는지 간단하게 작성하시오.
```
__init__, __del__, __str__, __repr__
```

1. __init__
    - 클래스의 인스턴스가 생성 된 후 호출된다. 그리고 호출자에게 반환된다.
    -

2. __del__
    - 인스턴스가 파괴될 때 호출된다.

3. __str__
    - 호출자와 내장함수 그리고 문자열을 표현하기 위한 메서드 반환값은 str
    - print 를 할때 나오는 사람이 볼 출력 값

4. __repr__
    - 문자열을 계산하는 내장함수의 표현
    - 단독 변수로 출력 한 컴퓨터가 볼 리턴, 즉 아웃풋 값

### Instance Method
.sort() 와 같이 문자열, 리스트, 딕셔너리 등을 조작 할 때 사용하였던 것들은 클래스에 정의된 메서드들이었다. 이처럼 문자열, 리스트, 딕셔너리 등을 조작하는 메서드를 최소 3가지 이상 그 역할과 함께 작성하시오.

1. .append()
    - 문자열 삽입을 위한 메서드
2. .min()
    - 최솟값을 반환하기 위한 매서드
3. .split()
    - 문자열을 쪼개기 위한 매서드



### 오류의 종류
아래에 제시된 오류들이 각각 어떠한 경우에 발생하는지 간단하게 작성하시오.
```
ZeroDivisionError, NameError, TypeError, IndexError, KeyError, ModuleNotFoundError, ImportError
```

1. ZeroDivisionError
    - 0 으로 나누는 값은 컴퓨터가 무한루프에 빠지기 때문에 예외적으로 금지시켜 놓은 항목이다.
2. NameError
    - namespace에 이름이 존재하지 않으면 발생하는 사항이다.
3. TypeError
    - 적용시키고자 하는 것에 자료타입이 맞지 않으면 발생하는 사항이다.
4. IndexError
    - 인덱스의 범위가 벗어난 경우 발생하는 사항이다.
5. KeyError
    - 해당 key가 존재하지 않는 경우 발생하는 사항이다.
6. ModuleNotFoundError
    - import 하려는 모듈이 존재하지 않을때 발생하는 사항이다.
7. ImportError
    - import 하려는 모듈은 존재하지만 존재하지 않는 클래스와 함수를 가져오려는 경우에 발생하는 사항이다.