import sys

sys.stdin = open('sample_input.txt')

T = int(input())

for test_case in range(T):

    N, M = map(int, input().split())
    a = [list(input().split()) for _ in range(N)]
    result = ''

    for j in range(N):
        for i in range(0, N-M+1):
            x = a[j][0][i: i+M]
            y = a[j][0][i+M:i-N-1:-1]

            if x == y:
                result = x

    for i in range(N):
        x = []
        for k in range(0, N-M+1):
            for j in range(k, k+M):
                x += a[j][0][i]

        z = ''.join(x)

        if z == y[::-1]:
            result = z

    print(f'#{test_case+1} {result}')
