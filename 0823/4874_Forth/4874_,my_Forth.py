import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for test_case in range(T):

    data = list(input().split())
    stack = []
    result = ''
    pos = True

    for char in data:

        if char.isnumeric():
            stack.append(int(char))

        elif char in '*/+-':
            if len(stack) > 1:
                if type(stack[-1]) == int and type(stack[-2]) == int:
                    x = stack.pop()
                    y = stack.pop()
                    if char == '*':
                        stack.append(int(y) * int(x))
                    elif char == '/':
                        if x != 0:
                            stack.append(int(y) // int(x))
                        else:
                            pos = False

                    elif char == '+':
                        stack.append(int(y) + int(x))
                    elif char == '-':
                        stack.append(int(y) - int(x))
                else:
                    pos = False

            else:
                pos = False

        elif char == '.':
            if len(stack) == 1:
                if type(stack[-1]) == int:
                    result = result + str(stack.pop())
                else:
                    pos = False
            else:
                pos = False

        else:
            pos = False

    if pos:
        print(f'#{test_case+1} {result}')
    else:
        print(f'#{test_case+1} error')
