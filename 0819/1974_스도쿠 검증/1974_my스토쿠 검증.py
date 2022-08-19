import sys
sys.stdin = open('input.txt')


def sudoku_check(sudoku):
    check = [0] * 9

    for i in range(9):
        for j in range(9):

            now = sudoku[i][j] - 1
            check[now] += 1

        if not all(check):
            return 0
        check = [0] * 9

    for i in range(9):
        for j in range(9):

            now = sudoku[j][i] - 1
            check[now] += 1

        if not all(check):
            return 0
        check = [0] * 9

    for i in range(0, 9, 3):
        for j in range(0, 9, 3):

            for x in range(3):
                for y in range(3):

                    now = sudoku[i+x][j+y] - 1
                    check[now] += 1

            if not all(check):
                return 0
            check = [0] * 9

    return 1

T = int(input())

for test_case in range(T):

    sudoku = [list(map(int, input().split())) for _ in range(9)]

    result = sudoku_check(sudoku)

    print(f'#{test_case+1} {result}')
