# def fibo(n):
#     lst = [1, 1]
#     if n < 2:
#         return lst[n]
#     while len(lst) < n:
#         lst.append(lst[-1] + lst[-2])
#     print(lst)
#     return lst[-1]
#
# print(fibo(100))

def fibo(n):
    if n < 2:
        return n
    if lst[n]:
        return lst[n]
    lst[n] = fibo(n-1) + fibo(n-2)
    print(lst)
    return lst[n]

n = 100
lst = [0] * (n+1)
print(fibo(n))