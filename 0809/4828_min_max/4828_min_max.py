import sys

sys.stdin = open('sample_input.txt')

T = int(input())


for test_case in range(1, T+1):

    N = int(input())
    a = list(map(int, input().split()))

    minimum, maximum, result = a[0], 0, 0

    for i in range(N):

        if a[i] > maximum:
            maximum = a[i]

    for j in range(N):

        if a[j] < minimum:
            minimum = a[j]


    result = maximum - minimum

    print(f'#{test_case} {result}')