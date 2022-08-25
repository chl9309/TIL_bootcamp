import sys
sys.stdin = open('sample_input.txt')


def search():
    for x in range(N):
        for y in range(N):
            if data[x][y] == 2:
                return x, y


T = int(input())

for tc in range(T):
    N = int(input())
    data = [list(map(int, input())) for _ in range(N)]

