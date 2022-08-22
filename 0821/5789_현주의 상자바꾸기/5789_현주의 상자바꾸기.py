import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for test_case in range(T):

    N, Q = map(int, input().split())
    box = [0] * N

    for i in range(1, 1+Q):

        L, R = map(int, input().split())
        temp = [i] * (R-L+1)
        box[L-1:R] = temp

    print(f'#{test_case+1}', end=' ')
    for j in range(len(box)-1):
        print(f'{box[j]}', end=' ')
    print(f'{box[-1]}')
