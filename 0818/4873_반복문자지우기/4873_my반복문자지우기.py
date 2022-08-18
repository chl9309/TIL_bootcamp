import sys
sys.stdin = open('input.txt', encoding='utf-8')
T = int(input())

for test_case in range(T):

    target = input()
    tmp = []

    for i in range(len(target)):

        if not tmp:
            tmp.append(target[i])

        elif target[i] == tmp[-1]:
            tmp.pop(-1)

        else:
            tmp.append(target[i])

    result = len(tmp)
    print(f'#{test_case+1} {result}')
