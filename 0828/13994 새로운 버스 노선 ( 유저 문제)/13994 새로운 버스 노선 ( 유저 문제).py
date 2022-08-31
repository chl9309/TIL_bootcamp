import sys
sys.stdin = open('sample_in.txt')

T = int(input())
for test_case in range(T):

    N = int(input())
    busstop = [0] * 1001

    for bus_num in range(N):

        bustype, A, B = map(int, input().split())

        if bustype == 1:

            for i in range(A, B+1):
                busstop[i] += 1

        elif bustype == 2:

            for i in range(A, B+1, 2):
                busstop[i] += 1
            if (B-A) % 2:
                busstop[B] += 1

        elif bustype == 3:

            if A % 2:
                for i in range(A+1, B+1):
                    busstop[A] += 1
                    busstop[B] += 1
                    if A % 2:
                        if not i % 4:
                            busstop[i] += 1

                    else:
                        if (not i % 3) and (i % 10):
                            busstop[i] += 1

    result = max(busstop)

    print(f'#{test_case+1} {result}')
