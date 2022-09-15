import sys
sys.stdin = open('sample_input.txt')


def inorder(x):

    if x:

        inorder(standard_nord_c1[x])
        global now
        now += 1
        nord[x] = now
        inorder(standard_nord_c2[x])


T = int(input())
for test_case in range(T):

    N = int(input())

    standard_nord_c1 = [0] * (N+1)
    standard_nord_c2 = [0] * (N+1)
    nord = [0] * (N+1)
    now = 0

    for i in range(N+1):

        if (i*2) <= N:
            standard_nord_c1[i] = i*2

            if (i*2 + 1) <= N:
                standard_nord_c2[i] = i * 2 + 1
    standard_nord_c2[0] = 0

    inorder(1)

    print(f'#{test_case+1} {nord[1]} {nord[N//2]}')
