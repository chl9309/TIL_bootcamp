import sys

sys.stdin = open('input.txt')

T = int(input())

for tc in range(T):
    N = int(input())
    a = [list(map(int, input().split())) for _ in range(N)]

    di = [0, 0, -1, 1]
    dj = [-1, 1, 0, 0]

    for i in range(1, N):
