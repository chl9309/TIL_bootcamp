import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for test_case in range(T):

    N = int(input())
    data = []
    for _ in range(N):

        data_now = list(map(int, input().split()))
        data.append(data_now)

print(data)





