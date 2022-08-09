import sys

sys.stdin = open('input.txt')

T = 10

for test_case in range(1, T + 1):

    N = int(input())
    A = list(map(int, input().split()))
    result = 0
    big = 0
    for i in range(2, N-2):

        if A[i] >= A[i-2]:
            if A[i] >= A[i-1]:
                if A[i] >= A[i+1]:
                    if A[i] >= A[i+2]:

                        if A[i-2] < A[i-1]:
                            if A[i-1] < A[i+1]:
                                if A[i+1] < A[i+2]:
                                    big = A[i+2]
                                else:
                                    big = A[i+1]
                            else:
                                if A[i-1] < A[i+2]:
                                    big = A[i+2]
                                else:
                                    big = A[i-1]
                        else:
                            if A[i-2] < A[i+1]:
                                if A[i+1] < A[i+2]:
                                    big = A[i+2]
                                else:
                                    big = A[i+1]
                            else:
                                if A[i-2] < A[i+2]:
                                    big = A[i+2]
                                else:
                                    big = A[i-2]

                        result += (A[i] - big)

    print(f'#{test_case} {result}')