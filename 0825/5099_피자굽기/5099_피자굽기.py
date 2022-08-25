import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for test_case in range(T):

    N, M = map(int, input().split())
    cheese = list(map(int, input().split()))
    fire = []

    for _ in range(N):
        fire.append([cheese.pop(0), _+1])

    cnt = N + 1

    while len(fire) > 1:

        fire[0][0] //= 2

        if fire[0][0]:
            tmp = fire.pop(0)
            fire.append(tmp)

        else:
            trash = fire.pop(0)
            if cheese:
                tmp = [cheese.pop(0), cnt]
                cnt += 1
                fire.append(tmp)

    result = fire[0][1]
    print(f'#{test_case+1} {result}')
