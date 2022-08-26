import sys
sys.stdin = open('input.txt')

T = int(input())
for test_case in range(T):

    N = int(input())
    farm = [list(map(int, input().split()))]

    half = (N+1) // 2
    full_sum = 0

    for i in range(N):
        for j in range(N):
            full_sum += farm[i][j]

    for i in range(half):
        for j in range()