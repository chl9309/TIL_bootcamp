import sys

sys.stdin = open('sample_input.txt')

T = int(input())
for test_case in range(T):

    N = int(input())
    a = [[0] * 10 for _ in range(10)]

    for c_in in range(N):
        r1, c1, r2, c2, color = map(int, input().split())

        for i in range(r1, r2+1):
            for j in range(c1, c2+1):

                a[j][i] += color
    cnt = 0
    for x in range(10):
        for y in range(10):

            if a[y][x] == 3:
                cnt += 1

    print(f'#{test_case+1} {cnt}')
