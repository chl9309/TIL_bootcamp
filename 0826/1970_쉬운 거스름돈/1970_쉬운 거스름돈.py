import sys
sys.stdin = open('input.txt')

T = int(input())
for test_case in range(T):

    N = int(input())
    money = [0] * 8

    while N >= 50000:
        N -= 50000
        money[0] += 1
    while N >= 10000 and N < 50000:
        N -= 10000
        money[1] += 1
    while N >= 5000 and N < 10000:
        N -= 5000
        money[2] += 1
    while N >= 1000 and N < 5000:
        N -= 1000
        money[3] += 1
    while N >= 500 and N < 1000:
        N -= 500
        money[4] += 1
    while N >= 100 and N < 500:
        N -= 100
        money[5] += 1
    while N >= 50 and N < 100:
        N -= 50
        money[6] += 1
    while N >= 10 and N < 50:
        N -= 10
        money[7] += 1


    print(f'#{test_case+1}', *money)
