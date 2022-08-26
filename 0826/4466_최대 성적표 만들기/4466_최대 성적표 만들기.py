import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for test_case in range(T):

    N, K = map(int, input().split())
    score = list(map(int, input().split()))
    max_sum = 0

    for i in range(K):
        maxx = 0

        for j in range(len(score)):
            if score[j] >= maxx:
                maxx = score[j]
                maxx_idx = j

        max_sum += maxx
        score.pop(maxx_idx)

    print(f'#{test_case+1} {max_sum}')
