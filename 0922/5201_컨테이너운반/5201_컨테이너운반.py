import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for test_case in range(T):

    N, M = map(int, input().split())

    wi = list(map(int, input().split()))
    ti = list(map(int, input().split()))

    wi.sort(reverse=True)
    ti.sort(reverse=True)
    work_sum = 0
    work_space = [True] * N
    truck_space = [True] * M
    work = False

    for i in range(M):
        for j in range(N):
            if ti[i] >= wi[j] and work_space[j] and truck_space[i]:
                work_space[j] = False
                truck_space[i] = False
                work_sum += wi[j]
                work = True
                break

    if work:
        result = work_sum
    else:
        result = 0

    print(f'#{test_case} {result}')
