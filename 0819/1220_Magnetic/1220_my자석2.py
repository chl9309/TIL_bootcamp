import sys
sys.stdin = open('input.txt')

for test_case in range(10):

    N = int(input())
    field = [list(map(int, input().split())) for _ in range(N)]
    cnt = 0

    for i in range(N):
        tmp = []
        pan = False
        for j in range(N):

            if field[j][i]:
                tmp.append(field[j][i])

        for k in range(len(tmp)):

            if tmp[k] == 1:
                pan = True

            else:
                if pan:
                    cnt += 1
                    pan = False

    #print(tmp)
    print(f'#{test_case+1} {cnt}')
