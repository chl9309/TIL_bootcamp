import sys
sys.stdin = open('sample_input.txt')


def merge(arr):
    if len(arr) == 1:
        return arr

    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]

    left = merge(left)
    right = merge(right)

    l_idx = r_idx = k = 0
    while l_idx < len(left) and r_idx < len(right):


T = int(input())
for test_case in range(T):

    N = int(input())
    nums = list(map(int, input().split()))

    result = 0






