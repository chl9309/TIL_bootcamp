import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for test_case in range(T):

    N = int(input())
    pos = False
    house_list = [list(map(int, input().split())) for _ in range(N)]
    result = -1

    for i in range(-15, 16):
        for j in range(-15, 16):
            cnt = 0
            long_cnt = 0
            for n in range(N):

                if ((abs(house_list[n][0]-i)) + (abs(house_list[n][1]-j))) <= house_list[n][2]:
                    cnt += 1
                    long_cnt += (abs(house_list[n][0]-i)) + (abs(house_list[n][1]-j))

            if cnt == N:
                pos = True
                if result == -1:
                    result = ((abs(house_list[n][0] - i)) + (abs(house_list[n][1] - j)))
                elif result > ((abs(house_list[n][0]-i)) + (abs(house_list[n][1]-j))):

                    result = ((abs(house_list[n][0]-i)) + (abs(house_list[n][1]-j)))

    if not pos:
        for i in range(-15, 16):
            for j in range(-15, 16):
                for x in range(-15, 16):
                    for y in range(-15, 16):
                        for n in range(N):
                            if (i != house_list[n][0]) and (j != house_list[n][1] ):
                                if (x != house_list[n][0]) and (y != house_list[n][1] ):
                                    pass



    print(f'#{test_case} {result}')