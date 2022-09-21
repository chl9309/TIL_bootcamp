import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for test_case in range(T):

    N = int(input())
    minsum = 9999999999
    for i in range(N):
        x = N - i

        for j in range(N):
            y = N - j

