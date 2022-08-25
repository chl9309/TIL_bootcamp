import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for test_case in range(T):

    N, M = map(int, input().split())
    data = list(map(int, input().split()))
    front, rear = 0, N-1

    for i in range(M):
        front = (front + 1) % N
        rear += (rear + 1) % N

    result = data[front]
    print(f'#{test_case+1} {result}')
