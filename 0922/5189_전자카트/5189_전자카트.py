import sys
sys.stdin = open('sample_input.txt')


def nPr(i, n):

    if i == n:
        elec_sum = 0
        for x in range(n-1):
            elec_sum += data[stage[x]][stage[x+1]]
        elec_sum += data[stage[n-1]][stage[0]]

        global min_electric
        if elec_sum < min_electric:
            min_electric = elec_sum

    else:
        for j in range(i, n):
            stage[i], stage[j] = stage[j], stage[i]
            nPr(i+1, n)
            stage[i], stage[j] = stage[j], stage[i]


T = int(input())
for test_case in range(T):

    N = int(input())
    data = [list(map(int, input().split())) for _ in range(N)]

    stage = list(range(N))
    min_electric = 9999999

    nPr(0, N)

    print(f'#{test_case+1} {min_electric}')



