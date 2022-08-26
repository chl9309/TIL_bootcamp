import sys
sys.stdin = open('input.txt')

T = int(input())
for test_case in range(T):

    N, M, K = map(int, input().split())
    consumer = list(map(int, input().split()))
    sec = -1
    bread = 0
    result = True

    for i in range(N):
        for j in range(i, N):
            if consumer[i] > consumer[j]:
                consumer[i], consumer[j] = consumer[j], consumer[i]

    #print(consumer)

    while consumer:

        sec += 1
        if sec:
            if not sec % M:
                bread += K

        while sec in consumer:
            if bread < 1:
                result = False
                break

            consumer.pop(0)
            bread -= 1

        if not result:
            break

    pos = 'Possible' if result else 'Impossible'
    print(f'#{test_case+1} {pos}')
