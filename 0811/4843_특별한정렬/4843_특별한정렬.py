import sys

sys.stdin = open('sample_input.txt')

T = int(input())

for test_case in range(T):

    N = int(input())
    a = list(map(int, input().split()))
    dmp = 0

    for i in range(N-1):
        dmp = i
        for j in range(i+1, N):


            if i % 2:
                if a[j] < a[dmp]:
                    dmp = j
            else:
                if a[j] > a[dmp]:
                    dmp = j

        a[i], a[dmp] = a[dmp], a[i]


    print(f'#{test_case+1}', end=' ')
    for x in range(10):
        print(a[x], end=' ')
    print()
