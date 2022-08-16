import sys

sys.stdin = open('sample_input.txt')

T = int(input())

for test_case in range(T):

    A, B = input().split()
    result, i, X, Y = 0, 0, len(A), len(B)

    while i < X:
        if A[i:i+Y] == B:
            i += len(B)-1
        result += 1
        i += 1

    print(f'#{test_case+1} {result}')
