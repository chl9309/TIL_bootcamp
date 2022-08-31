import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for test_case in range(T):

    N, Kmin, Kmax = map(int, input().split())
    score = list(map(int, input().split()))
    pos = False
    result = -1

    for i in range(N):
        for j in range(i, N):
            if score[i] > score[j]:
                score[i], score[j] = score[j], score[i]

    min_score = score[0]
    max_score = score[-1]

    for x in range(min_score, max_score-1):
        for y in range(x+1, max_score):
            A, B, C = [], [], []
            for z in range(N):
                if score[z] <= x:
                    A.append(score[z])
                elif score[z] <= y:
                    B.append(score[z])
                else:
                    C.append(score[z])

            if (len(A) >= Kmin) and (len(A) <= Kmax):
                if (len(B) >= Kmin) and (len(B) <= Kmax):
                    if (len(C) >= Kmin) and (len(C) <= Kmax):
                        if result == -1:
                            result = max(len(A), len(B), len(C)) - min(len(A), len(B), len(C))
                        else:
                            tmp = max(len(A), len(B), len(C)) - min(len(A), len(B), len(C))
                            if result > tmp:
                                result = tmp



    print(f'#{test_case+1} {result}')
