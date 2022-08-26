import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for test_case in range(T):

    N, K = map(int, input().split())
    homework = list(map(int, input().split()))
    student = list(range(1, N+1))
    result = []
    for i in range(1, N+1):
        if i not in homework:
            result.append(i)

    print(f'#{test_case+1} ', *result)
