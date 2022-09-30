import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for test_case in range(T):

    N, M, C = map(int, input().split())
    tong = [list(map(int, input().split())) for _ in range(N)]

    honey_1, honey_2 = 0, 0

    for j in range(N):
        for i in range(N-M+1):
            select1 = tong[j][i:i+M]
            for k in range(j, N):
                for l in range(N-M+1):
                    select2 = tong[k][l:l+M]






