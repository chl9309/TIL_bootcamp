import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for test_case in range(T):

    N = int(input())
    data = [list(map(int, input().split())) for _ in range(N)]

    max_fuel = 999999999999

    for i in range





