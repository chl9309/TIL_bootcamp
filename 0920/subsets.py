from itertools import combinations
arr = [1, 2, 3]
print(list(combinations(arr, 1)))
print(list(combinations(arr, 2)))
print(list(combinations(arr, 3)))

subsets = [[]]

for num in arr:
    size = len(subsets)
    for y in range(size):
        subsets.append(subsets[y]+[num])
print(subsets)

import copy

result = []


def recur(subset, i, arr):
    if i == len(arr):
        result.append(copy.copy(subset))
        return
    else:
        subset.append(arr[i])
        i += 1
        recur(subset, i, arr)
        subset.pop()
        recur(subset, i, arr)


recur([], 0, arr)
# print(result)

arr = [1,2,3]
result = []
for i in range(1<<len(arr)):
    subset = []
    for j in range(len(arr)):
        if i & (1<<j):
            subset.append(arr[j])
    result.append(subset)
# print(result)