T = int(input())
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    N = int(input())

    a = [[0]*N for _ in range(N)]
    x = 1
    i, j = 0, 0
    cnt = N-1

    a[0][0] = x
    while 0<N:

        while 0<cnt:
            x += 1
            j += 1
            a[i][j] = x
            cnt -= 1

        N -= 1
        cnt = N

        while 0<cnt:
            x += 1
            i += 1
            a[i][j] = x
            cnt -= 1

        cnt = N

        while 0<cnt:
            x += 1
            j -= 1
            a[i][j] = x
            cnt -= 1

        N -= 1
        cnt = N

        while 0<cnt:
            x += 1
            i -= 1
            a[i][j] = x
            cnt -= 1

        cnt = N
    print(f'#{test_case}')
    for pt in range(N):
        print(f'{a[pt]}')