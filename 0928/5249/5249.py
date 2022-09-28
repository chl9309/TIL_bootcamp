import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for test_case in range(T):

    V, E = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(E)]

    arr.sort(key=lambda x: x[2])

    



