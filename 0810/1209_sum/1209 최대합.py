import sys

sys.stdin = open('input.txt')

T = 10

for test_case in range (1, T+1):
    test_num = int(input())
    a = [list(map(int, input().split())) for _ in range(100)]

    maximum, sum = 0, 0

    for i in range(100):
        for j in range(100):
            sum += a[i][j]

        if maximum < sum:
            maximum = sum
        sum = 0

    for i in range(100):
        for j in range(100):
            sum += a[j][i]

        if maximum < sum:
            maximum = sum
        sum = 0

    for i in range(100):
        sum += a[i][i]

    if maximum < sum:
        maximum = sum
    sum = 0

    for i in range(100):
        sum += a[i][99-i]

    if maximum < sum:
        maximum = sum

    print(f'#{test_case} {maximum}')
