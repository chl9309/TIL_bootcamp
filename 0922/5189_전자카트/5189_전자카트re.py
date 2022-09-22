import sys
sys.stdin = open('sample_input.txt')


def nPr(i, n):

    if i == n and p[0] == 0:
        elec_sum = 0
        for x in range(n-1):
            elec_sum += data[p[x]][p[x+1]]
        elec_sum += data[p[n-1]][p[0]]

        global min_electric
        if elec_sum < min_electric:
            min_electric = elec_sum

    else:
        for j in range(n):
            if used[j] == 0:
                used[j] = 1
                p[i] = stage[j]
                nPr(i+1, n)
                used[j] = 0


T = int(input())
for test_case in range(T):

    N = int(input())
    data = [list(map(int, input().split())) for _ in range(N)]

    stage = list(range(1, N))
    min_electric = 9999999
    used = [0] * (N-1)
    p = [0] * (N-1)
    nPr(0, N-1)

    print(f'#{test_case+1} {min_electric}')
