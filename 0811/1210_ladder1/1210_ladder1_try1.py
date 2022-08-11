import sys

sys.stdin = open('input.txt')


for test_case in range(1,11):
    T = int(input())
    a = [list(map(int, input().split())) for _ in range(100)]
    x, y = 0, 0
    result = 0

    for start in range(100):

        if a[0][start] == 1:
            x, y = start, 0
        else:
            continue

        while y < 99:

            if x != 99:
                if a[y][x+1]:
                    while a[y][x+1] == 1:
                        if x == 99:
                            break
                        x += 1
                    y += 1
                    continue

            if x != 0:
                if a[y][x-1]:

                    while a[y][x-1] == 1:
                        if x == 0:
                            break
                        x -= 1
                    y += 1
                    continue

            y += 1
            continue

        if a[y][x] == 2:
            result = start
            break
        else:
            continue


    print(f'#{test_case} {result}')