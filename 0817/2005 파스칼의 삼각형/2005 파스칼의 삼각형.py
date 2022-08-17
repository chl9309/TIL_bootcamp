import sys
sys.stdin = open('input.txt')


def pascal(num):
    if num == 1:

        p = [1]

    else:
        p = []
        for i in range(num):
            if (i == 0) or (i == num - 1):
                p.append(1)
            else:
                a = pascal(num - 1)
                p.append(a[i - 1] + a[i])

    return p

def pascal_print (num):

    if num > 1:
        pascal_print(num - 1)

    print(pascal(num))
    return


T = int(input())
for test_case in range(T):

    N = int(input())

    print(f'#{test_case + 1}')
    pascal_print(N)




