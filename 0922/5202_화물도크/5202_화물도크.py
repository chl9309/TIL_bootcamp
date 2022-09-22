import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for test_case in range(T):

    N = int(input())
    s = []
    e = []
    for i in range(N):

        s_now, e_now = map(int, input().split())
        s.append(s_now)
        e.append(e_now)




