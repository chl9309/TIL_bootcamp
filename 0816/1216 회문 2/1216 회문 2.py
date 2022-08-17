import sys

sys.stdin = open('input.txt')

T = 10

for _ in range(T):
    test_case = input()
    a = [input() for _ in range(100)]
    a_rev = list(zip(*a))
    result = 0

    for i in range(1, 101):
        # if result >
        for j in range(100):
            for k in range(101-i):
                b = a[j][k:k+i+1]
                if b == b[::-1]:
                    if result <= i:
                        result = i

    for i in range(1, 101):
        for j in range(100):
            for k in range(101-i):
                b = a_rev[j][k:k+i+1]
                if b == b[::-1]:
                    if result <= i:
                        result = i


    print(f'#{test_case} {result+1}')



    ## 이미 검색 된 result 값 보다 적은 i 값은 검색 할 필요가 없다
    ## 그것을 생각하고 조건문을 추가해보자

    ## 어짜피 제일 큰 값을 찾는 것이다. i를 작은 것 부터 검색 해 나갈 것이 아니라
    ## 큰 값에서 부터 하나씩 내려오면서 검색하다가 한 번이라도 회문을 통과하면 그것이 가장 큰 값이다.

    ## 열 조사할때도 이미 구해진 값보다 낮은 값은 검사 할 필요가 없다