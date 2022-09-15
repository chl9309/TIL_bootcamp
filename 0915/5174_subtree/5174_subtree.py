import sys
sys.stdin = open('sample_input.txt')

def inorder(x):

    if x:
        global result
        result += 1

        inorder(c1[x])
        inorder(c2[x])


T = int(input())
for test_case in range(T):

    E, N = map(int, input().split())
    data = list(map(int, input().split()))

    c1 = [0] * (E + 2)
    c2 = [0] * (E + 2)
    result = 0

    for i in range(E):

        p = data[i*2]
        c = data[i*2 + 1]

        if not c1[p]:
            c1[p] = c

        else:
            c2[p] = c

    inorder(N)

    print(f'#{test_case+1} {result}')
