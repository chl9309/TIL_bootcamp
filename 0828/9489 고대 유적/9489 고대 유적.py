import sys
sys.stdin = open('input1.txt')

T = int(input())
for test_case in range(T):

    N, M = map(int, input().split())
    world = [list(map(int, input().split())) for _ in range(N)]
    maxx = 0

    for i in range(N):
        cnt = 0
        for j in range(M):

            if world[i][j]:
                cnt += 1
            else:
                if cnt > maxx:
                    maxx = cnt
                cnt = 0

        if cnt > maxx:
            maxx = cnt
        cnt = 0

    cnt = 0

    for i in range(M):
        cnt = 0
        for j in range(N):
            if world[j][i]:
                cnt += 1
            else:
                if cnt > maxx:
                    maxx = cnt
                cnt = 0

        if cnt > maxx:
            maxx = cnt


    print(f'#{test_case+1} {maxx}')


