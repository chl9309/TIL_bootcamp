import sys
sys.stdin = open('input.txt')

T = int(input())
for test_case in range(T):

    word = input()
    stack = []
    result = ''

    for char in word:
        if char in '/*+-()':
            if not stack:
                stack.append(char)
            elif char == '(':
                stack.append(char)
            elif char in '/*':
                while stack and stack[-1] in '/*':
                    result += stack.pop()
                stack.append(char)
            elif char in '+-':
                while stack and stack[-1] != '(':
                    result += stack.pop()
                stack.append(char)
            elif char == ')':
                while stack and stack[-1] != '(':
                    result += stack.pop()
                stack.pop()
        else:
            result += char

    print(f'#{test_case+1} {result}')
# ? 마지막 연산자 출력 안 됌 나중에 수정하길
