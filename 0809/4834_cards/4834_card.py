import sys

sys.stdin = open('sample_input.txt')

T = int(input())

for test_case in range(1, T + 1):

    N = int(input())
    a = list(map(int, list(input())))
    count = [0] * 9

    for i in range(N):
        for j in range(1, 10):

            if a[i] == j:
                count[j-1] += 1

    max_num, max_count = 0, 0

    for k in range(9):

        if count[k] >= max_count:
            max_count = count[k]
            max_num = k+1

    print(f'#{test_case} {max_num} {max_count}')