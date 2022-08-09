import sys

sys.stdin = open('input.txt')

T = 10

for test_case in range(1, T+1):

     N = int(input())
     a = list(map(int, input().split()))

     result = 0

     while N > 0:
        maximum, minimum = 0, 101
        max_idx, min_idx = 0, 0

        for i in range(100):
            if maximum <= a[i]:
                maximum = a[i]
                max_idx = i
        for j in range(100):
            if minimum >= a[j]:
                minimum = a[j]
                min_idx = j

        if maximum - minimum <= 1:
            break

        a[max_idx] -= 1
        a[min_idx] += 1
        N -= 1

     for i in range(100):
         if maximum <= a[i]:
             maximum = a[i]
             max_idx = i
     for j in range(100):
         if minimum >= a[j]:
             minimum = a[j]
             min_idx = j
     result = a[max_idx] - a[min_idx]

     print(f'#{test_case} {result}')