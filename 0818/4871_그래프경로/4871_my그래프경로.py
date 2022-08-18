import sys
sys.stdin = open('input.txt')

T = int(input())

for test_case in range(T):

    V, E = map(int, input().split())

    nord = []
    for _ in range(E):
        nord += list(map(int, input().split()))

    S, G = map(int, input().split())

    memo = [list([0] * V) for _ in range(V)]

    print(memo)

