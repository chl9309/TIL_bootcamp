import sys
sys.stdin = open('input.txt')


def field_move(field):
    new_field = [[0] * 100 for _ in range(100)]

    for i in range(100):
        for j in range(100):

            if field[i][j] == 1:
                if i == 100:
                    if not field[i+1][j]:
                        field[i+1][j] = 1
                        field[i][j] = 0

            elif field[i][j] == 2:




T = int(input())
for test_case in range(T):

    field = [list(map(int, input().split())) for _ in range(100)]


