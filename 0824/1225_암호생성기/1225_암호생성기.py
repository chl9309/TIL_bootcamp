import sys
sys.stdin = open('input.txt')

for _ in range(10):

    test_case = int(input())
    data = list(map(int, input().split()))

    front = 0
    end = len(data) - 1


    tmp = 999
    this = 1

    while tmp < 1:


