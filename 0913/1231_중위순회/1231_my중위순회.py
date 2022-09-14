import sys
sys.stdin = open('input.txt')

def inorder_traverse(T):
    if T:
        inorder_traverse(l[T])
        result.append(c[T])
        inorder_traverse(r[T])

    return


for test_case in range(10):

    subroot, cha, left, right = 0, 0, 0, 0
    N = int(input())
    c, l, r = [0] * (N + 1), [0] * (N + 1), [0] * (N + 1)

    for _ in range(N):

        data = input().split()
        if len(data) < 4:

            data.extend([0] * (4 - len(data)))

        subroot, cha, left, right = data
        c[int(subroot)] = cha
        l[int(subroot)] = int(left)
        r[int(subroot)] = int(right)

    result = []
    inorder_traverse(1)
    print(f'#{test_case +1}', ''.join(result))
