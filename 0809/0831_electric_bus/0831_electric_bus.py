import sys

sys.stdin = open('sample_input.txt')


T = int(input())


for test_case in range(1, T+1):

    K, N, M = map(int, input().split())

    charge_list = list(map(int, input().split()))
    charge_count = 0
    energy = K
    gogo, possible = True, True

    for i in range(N):
        for j in range(M-1,0,-1):

            if i<charge_count[M]:
                if energy > charge_list[j]-i:
                    gogo = True
                    break
                else:
                    gogo = False
            else:
                gogo

        if gogo:
            energy -= 1
        else:
            for k in range(M):

                if N == charge_list[k]:
                    energy = K
                    charge_count += 1
                    possible = True
                    break
                else:
                    possible = False


    if possible:
        print(f'#{test_case} {charge_count}')
    else:
        print(f'#{test_case} 0')