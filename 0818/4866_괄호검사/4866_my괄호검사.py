import sys
sys.stdin = open('input.txt')

T = int(input())

for test_case in range(T):

    target = input()
    tmp = []

    for i in range(len(target)):

        if (target[i] == '(') or (target[i] == ')') or (target[i] == '{') or (target[i] == '}'):

            if not tmp:
                tmp.append(target[i])

            elif target[i] == '(':
                tmp.append(target[i])

            elif target[i] == ')':
                if tmp[-1] == '(':
                    tmp.pop(-1)
                else:
                    tmp.append(target[i])

            elif target[i] == '{':
                tmp.append(target[i])
            elif target[i] == '}':
                if tmp[-1] == '{':
                    tmp.pop(-1)

                else:
                    tmp.append(target[i])

    if tmp:
        result = 1
    else:
        result = 0


    print(f'#{test_case} {result}')
