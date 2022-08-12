import sys

sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):

    word = input()

    print(f'#{tc} {word}')


    result = list(reversed(word))

    print(f'#{tc} {result}')

    for idx in range(len(word)-1, -1, -1):

        result += word[idx]

    print(f'#{tc} {result}')