import sys

sys.stdin = open('sample_input.txt')


T = int(input())


for test_case in range(1, T+1):

    K, N, M = map(int, input().split())

    charge_list = list(map(int, input().split()))
    charge_count = 0
    energy = K
    gogo, possible = False, False

    for i in range(N):
        gogo, possible = False, False

        for j in range(M-1, -1, -1):

            if i < charge_list[M-1]:
                if energy >= charge_list[j]-i:
                    if i <= charge_list[j]:
                        gogo = True
                        break
                    else:
                        continue
                else:
                    gogo = False
            else:
                if energy > N-i:
                    possible = True
                else:
                    gogo = False


        if possible:
            break
        elif gogo:
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
