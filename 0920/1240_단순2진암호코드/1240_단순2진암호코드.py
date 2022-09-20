import sys
sys .stdin = open('input.txt')

T = int(input())
for test_case in range(T):

    N, M = map(int, input().split())
    data = [input() for _ in range(N)]
    password = []
    flag = False

    for i in range(N):
        for j in range(M-1, 0, -1):

            if data[i][j] == '1':
                password_point = [i, j]
                flag = True
                break

        if flag:
            break

    password = data[i][j-55:j]
    decoding = []
    for k in range(0, 65, 7):
        nowdata = password[k: k+7]
        if password[k: k+7] == '0001101':
            decoding.append(0)
        elif password[k: k+7] == '0011001':
            decoding.append(1)
        elif password[k: k+7] == '0010011':
            decoding.append(2)
        elif password[k: k+7] == '0111101':
            decoding.append(3)
        elif password[k: k+7] == '0100011':
            decoding.append(4)
        elif password[k: k+7] == '0110001':
            decoding.append(5)
        elif password[k: k+7] == '0101111':
            decoding.append(6)
        elif password[k: k+7] == '0111011':
            decoding.append(7)
        elif password[k: k+7] == '0110111':
            decoding.append(8)
        elif password[k: k+7] == '0001011':
            decoding.append(9)

    print(decoding)
print(len('110010100011010001101011110110111001001100100110111011'))


