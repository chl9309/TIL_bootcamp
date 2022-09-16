import sys
sys.stdin = open('input.txt')

for test_case in range(10):

    leng, start = map(int, input().split())
    data = list(map(int, input().split()))

    full_list = [[0] * leng for _ in range(leng)]

    for i in range(0, leng, 2):

        full_list[data[i]][data[i+1]] = 1



print(full_list)

