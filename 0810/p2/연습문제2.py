import sys

sys.stdin = open('input.txt')

T = int(input())

for test_case in range(T):

    a = list(map(int, input().split()))
    N = len(a)
    a_sum = 0
    cnt = 0
    for i in range(1<<N):
        for j in range(N):
            if i & (1<<j):

                a_sum += a[j]

        if not a_sum:
            cnt += 1
        a_sum = 0

    print (f'#{test_case + 1} {cnt}')

