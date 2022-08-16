import sys

sys.stdin = open('sample_input.txt')

T = int(input())

for test_case in range(T):

    str1 = input()
    str2 = input()
    X, Y = len(str1), len(str2)
    result = 0

    for i in range(Y-X+1):

        if str1 == str2[i:i+X]:
            result += 1

    print(f'#{test_case} {result}')
