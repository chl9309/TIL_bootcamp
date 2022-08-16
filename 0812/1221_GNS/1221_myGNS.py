import sys

sys.stdin = open('GNS_test_input.txt')

T = int(input())

for test_case in range(T):

    trash, l = map(str, input().split())
    l = int(l)

    target = list(input().split())
    translate = [0] * l
    result = [0] * l
    for i in range(l):

        if target[i] =="ZRO":
            translate[i] = 0
        elif target[i] =="ONE":
            translate[i] = 1
        elif target[i] =="TWO":
            translate[i] = 2
        elif target[i] =="THR":
            translate[i] = 3
        elif target[i] =="FOR":
            translate[i] = 4
        elif target[i] =="FIV":
            translate[i] = 5
        elif target[i] =="SIX":
            translate[i] = 6
        elif target[i] =="SVN":
            translate[i] = 7
        elif target[i] =="EGT":
            translate[i] = 8
        elif target[i] =="NIN":
            translate[i] = 9


    for x in range(l-1, 1, -1):
        for y in range(x):
            if translate[y] > translate[y+1]:
                translate[y], translate[y+1] = translate[y+1], translate[y]


    for j in range(l):
        if translate[j] == 0:
            result[j] = "ZRO"
        elif translate[j] == 1:
            result[j] = "ONE"
        elif translate[j] == 2:
            result[j] = "TWO"
        elif translate[j] == 3:
            result[j] = "THR"
        elif translate[j] == 4:
            result[j] = "FOR"
        elif translate[j] == 5:
            result[j] = "FIV"
        elif translate[j] == 6:
            result[j] = "SIX"
        elif translate[j] == 7:
            result[j] = "SVN"
        elif translate[j] == 8:
            result[j] = "EGT"
        elif translate[j] == 9:
            result[j] = "NIN"



    print(f'{trash}')
    for k in range(l):
        print(f'{result[k]} ', end='')


