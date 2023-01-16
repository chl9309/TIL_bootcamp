data = [0] * 10000
x = list(range(1, 10001))

for i in range(1, 10001):

    a = chr(i)
    data[i] += (int(a[j]) for j in range(len(a)))
    data[i] += i

for k in range(1, 10001):
    pass