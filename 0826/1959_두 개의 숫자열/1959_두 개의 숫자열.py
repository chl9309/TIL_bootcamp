import sys
sys.stdin = open('input.txt')

T = int(input())
for test_case in range(T):
    N, M = map(int, input().split())
    Ai = list(map(int, input().split()))
    Bj = list(map(int, input().split()))
    maxx = 0

    if N >= M:
        long, long_list, short, short_list = N, Ai, M, Bj
    else:
        long, long_list, short, short_list = M, Bj, N, Ai

    for i in range(long-short+1):
        tmp = 0
        for j in range(short):
            tmp += (long_list[i+j] * short_list[j])
        if tmp >= maxx:
            maxx = tmp

    print(f'#{test_case+1} {maxx}')
