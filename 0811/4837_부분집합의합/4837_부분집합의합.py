import sys

sys.stdin = open('sample_input.txt')

T = int(input())
for test_case in range(T):

    N, K = list(map(int, input().split()))

    a = []
    for ele in range(12):
     a.append(ele + 1)
    sub_a = []
    cnt = 0

    for i in range(2**12):
        for j in range(12):
            if i & (2**j):
                sub_a.append(a[j])
        sub_sum = 0
        for k in range(len(sub_a)):
            sub_sum += sub_a[k]

        if len(sub_a) == N:
            if sub_sum == K:
                cnt += 1
        sub_a = []


    print(f'#{test_case+1} {cnt}')
