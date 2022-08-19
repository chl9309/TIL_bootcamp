import sys
sys.stdin = open('input.txt', encoding='utf-8')

T = int(input())

for test_case in range(T):

    N, K = map(int, input().split())
    puzzle = [list(map(int, input().split())) for _ in range(N)]
    result = 0
    i, j = -1, -1
    while i < N-1:
        i += 1
        while j < N-K:
            j += 1



            if puzzle[i][j] == 1:
                cnt = 0
                while :
                    if puzzle[i][j+k]:
                        cnt += 1

                    else:
                        if cnt == K:
                            result += 1
                            j+



