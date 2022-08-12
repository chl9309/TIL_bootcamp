import sys
sys.stdin = open('test_input.txt', encoding='utf-8')



for test_case in range(10):
    tc = int(input())
    search = input()
    target = input()

    result = 0

    for i in range(len(target)-len(search)+1):
        cnt = 0
        for j in range(len(search)):

            if search[j] == target[i+j]:
                cnt += 1
            else:
                break

            if cnt == len(search):
                result += 1



    print(f'#{test_case+1} {result}')
