import sys
sys.stdin = open('input.txt', encoding='utf-8')


def puzzle_cnt(n, k, puzzlee):

    resultt = 0

    for i in range(n):
        cnt = 0
        for j in range(n):

            if puzzlee[i][j]:
                cnt += 1
                if j == n-1:
                    if cnt == k:
                        resultt += 1

            else:
                if cnt == k:
                    resultt += 1
                cnt = 0

    return resultt


T = int(input())

for test_case in range(T):

    N, K = map(int, input().split())
    puzzle = [list(map(int, input().split())) for _ in range(N)]
    puzzle_rev = list(zip(*puzzle))

    result = puzzle_cnt(N, K, puzzle) + puzzle_cnt(N, K, puzzle_rev)

    print(f'#{test_case+1} {result}')
