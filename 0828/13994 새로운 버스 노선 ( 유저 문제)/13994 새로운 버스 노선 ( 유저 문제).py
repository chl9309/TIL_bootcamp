import sys
sys.stdin = open('sample_in.txt')

T = int(input())
for test_case in range(T):

    N = int(input())
    busstop = [0] * 1000

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
                for i in range(A, B):

                    if A%2:
                        if not i%4:
                            busstop[i] +=1
                            busstop[B] +=1
                    else:
                        if (not A%3) and (A%10):
                            busstop[i] +=1

    #print(busstop)
    result = max(busstop)

    print(f'#{test_case} {result}')



