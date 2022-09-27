import sys
sys.stdin = open('sample_input.txt')


def charge(x, cnt):

    if x == 1:

        return cnt

    for i in range(1, x):

        if i + Mi[i-1] >= x:

            return charge(i, cnt+1)


T = int(input())
for test_case in range(T):

    Mi = list(map(int, input().split()))
    N = Mi.pop(0)

    result = charge(N, 0)

    print(f'#{test_case+1} {result-1}')
