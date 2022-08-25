import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for test_case in range(T):

    V, E = map(int, input().split())
    gansun = [list(map(int, input().split())) for _ in range(E)]
    S, G = map(int, input().split())
    nord = []
    for nord_num in range(1, V+1): nord.append(nord_num)

    visited = [False] * V
    queue = []

    queue.append(S)
    while queue:

        t = queue.pop(0)
        if not visited

    print()
