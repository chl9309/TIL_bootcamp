import sys

sys.stdin = open('sample_input.txt')

T = int(input())
for test_case in range(T):

    P, Pa, Pb = map(int, input().split())
    cnt_a, cnt_b = 0, 0

    l, r = 1, P


    while l <= r:
        c = (l + r) // 2
        if Pa > c:
            l = c + 1

        elif Pa < c:
            r = c - 1

        else:
            break

        cnt_a += 1

    l, r = 1, P
    c = (l + r) // 2

    while l <= r:
        c = (l + r) // 2
        if Pb > c:
            l = c + 1

        elif Pb < c:
            r = c - 1

        else:
            break

        cnt_b += 1

    if cnt_a < cnt_b:
        result = 'A'
    elif cnt_a > cnt_b:
        result = 'B'
    else:
        result = 0

    print(f'#{test_case+1} {result}')
