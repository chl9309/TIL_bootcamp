import sys
sys.stdin = open('input.txt')


def order(x):
    a = nord_data[x]
    if not a.isdigit():
        left = int(order(c1[x]))
        right = int(order(c2[x]))

        if a == '+':
            result = left + right
            return result
        elif a == '-':
            result = left - right
            return result
        elif a == '*':
            result = left * right
            return result
        elif a == '/':
            result = left // right
            return result

    return nord_data[x]


for test_case in range(10):

    N = int(input())
    stadard_nord = [0] * (N + 1)
    nord = [0] * (N + 1)
    nord_data = [0]
    c1 = [0] * (N + 1)
    c2 = [0] * (N + 1)

    for i in range(N):
        data = list(input().split())
        nord_data.append(data[1])

        if len(data) == 4:

            c1[i+1] = int(data[2])
            c2[i+1] = int(data[3])


    print(f'#{test_case+1} {order(1)}')
