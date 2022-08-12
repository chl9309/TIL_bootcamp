import sys

sys.stdin = open('GNS_test_input.txt')

T = int(input())

for test_case in range(T):

    trash, l = map(str, input().split())
    l = int(l)
    target = list(input().split())

    dic_trans = {_:0 for _ in target}

    for i in target:
        dic_trans[i] += 1

    for j in dic_trans:
        result




    #print(trash'\n')

    #print(dic_trans)
