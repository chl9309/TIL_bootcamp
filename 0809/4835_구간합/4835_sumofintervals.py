import sys

sys.stdin = open('sample_input.txt')

T = int(input())

for test_case in range(1, T+1):
    N, M = map(int, input().split())
    v = list(map(int, input().split()))

    maximum, minimum = 0,0

    for x in range(M+1):
        minimum += v[x]
    for i in range(N-M+1):
        sum = 0
        for j in range(i, i+M):
            sum += v[j]

        if sum > maximum:
            maximum = sum
        if sum < minimum:
            minimum = sum

    result = maximum - minimum

    print(f'#{test_case} {result}')