import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for test_case in range(T):

    N = int(input())
    data = list(map(int, input().split()))
    stadard_nord = [0] * (N+1)
    nord = [0] * (N+1)

    for i in range(N+1):

        stadard_nord[i] = i // 2

    data.insert(0, 0)

    while True:

        flag = True
        for k in range(1, (N//2)+1):

            if (k*2 <= N) and (data[k] > data[k*2]):
                data[k], data[k*2] = data[k*2], data[k]
                flag = False
                break   # 이 break 문은 없으면 바꾼 뒤에 위에서 탐색을 다시 하는게 아닌
                # 그 상황에서 이어서 또 탐색하므로 필요

            if (k*2 + 1 <= N) and data[k] > data[k*2 + 1]:
                data[k], data[k*2 + 1] = data[k*2 + 1], data[k]
                flag = False
                break

        if flag:
            break

    result = 0
    now = N

    while now:

        now = stadard_nord[now]
        result += data[now]

    print(f'#{test_case+1} {result}')
