def index(request):
    return request

def path(url, func):
    print(func(url))
    return
# print(index('사용자의 요청 정보'))

path('index/', index)

# 파이썬은 모든 것들이 객체

def my_func(a, b): # 3, 4
    return a + b # 3 + 4

c = my_func(3, 4) # 7
# print(c)

d = my_func
print(d)
print(d(3, 4))