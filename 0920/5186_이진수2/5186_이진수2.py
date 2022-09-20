import sys
sys. stdin = open('sample_input.txt')

T = int(input())
for test_case in range(T):

    N = float(input())
    bin_num = []
    a = 0

    while a < 13 and N:
        a += 1

        if N >= (2**-a):
            bin_num.append(1)
            N -= (2**-a)

        else:
            bin_num.append(0)

    if N:
        result = 'overflow'

    else:
        result = ''.join([str(_) for _ in bin_num])

    print(f'#{test_case+1} {result}')

