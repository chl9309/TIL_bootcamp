import sys

sys.stdin = open('input.txt')

T = int(input())

for test_case in range(T):

    N, M = map(int, input().split())
    paris = [list(map(int, input().split())) for _ in range(N)]

    maximum = 0

    for i in range(N-M+1):
        for j in range(N-M+1):

            attack = 0
            for k in range(M):
                for m in range(M):
                    attack += paris[i+k][j+m]

            if attack > maximum:

                maximum = attack

    print(f'#{test_case} {maximum}')
