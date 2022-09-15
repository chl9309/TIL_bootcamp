import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for test_case in range(T):

    N, M, L = map(int, input().split())
    stadard_nord = [0] * (N + 1)
    nord = [0] * (N + 1)

    for i in range(N+1):

        stadard_nord[i] = i // 2

    for j in range(M):

        leaf_nord, data = map(int, input().split())
        nord[leaf_nord] = data

    for k in range(N, 0, -1):

        nord[stadard_nord[k]] += nord[k]

    print(f'#{test_case+1} {nord[L]}')
