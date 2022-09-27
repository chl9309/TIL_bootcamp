import sys
sys.stdin = open('sample_input.txt')


def nPr(arr, r):
    p = []

    if r > N:
        return p
    if r == 1:
        for i in arr:
            p.append([i])
    elif r > 1:
        for i in range(N):
            ans = [i for i in arr]
            ans.remove(arr[i])
            for j in nPr(ans, r-1):
                p.append([arr[i]]+j)

    return p



T = int(input())
for test_case in range(T):

    N = int(input())
    Vij = [list(map(int, input().split()) for _ in range(N))]

    min_cost = 99999999

    arr = [0] * N
    for a in range(N):
        arr[a] = a+1

    print(arr)
    print(nPr(arr, N))



