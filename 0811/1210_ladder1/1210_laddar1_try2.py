import sys

sys.stdin = open('input.txt')

T = int(input())
for test_case in range(T):

    a = [list(map(int, input().split())) for _ in range(100)]
    x, y = 0, 0
    result = 0
