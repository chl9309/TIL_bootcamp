nums = list(range(1, 10001))
generator_nums = []

for i in range(1, 10001):
    tmp = i
    for j in str(i):
        tmp += int(j)
    generator_nums.append(tmp)

nums = set(nums)
generator_nums = set(generator_nums)

self_nums = list(nums - generator_nums)
self_nums.sort()

for i in self_nums:
    print(i)
