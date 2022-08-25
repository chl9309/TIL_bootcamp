import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for test_case in range(T):

    N, M = map(int, input().split())
    cheese = list(map(int, input().split()))
    fire = [0] * N
    front, rear = -1, -1

    while len(cheese) > 1:





