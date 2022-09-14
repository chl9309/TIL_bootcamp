import sys
sys.stdin = open('input.txt')


def preorder_traverse(T):
    if T:
        print(T, end=' ')
        preorder_traverse(c1[T])
        preorder_traverse(c2[T])


def inorder_traverse(T):
    if T:
        inorder_traverse(c1[T])
        print(T, end=' ')
        inorder_traverse(c2[T])


def postorder_traverse(T):
    if T:
        postorder_traverse(c1[T])
        postorder_traverse(c2[T])
        print(T, end=' ')


V = int(input())
E = V-1
data = list(map(int, input().split()))
c1 = [0] * (V + 1)
c2 = [0] * (V + 1)

for i in range(E):

    p = data[2*i]
    c = data[2*i + 1]

    if not c1[p]:
        c1[p] = c

    else:
        c2[p] = c

print(preorder_traverse(1))
print(inorder_traverse(1))
print(postorder_traverse(1))
