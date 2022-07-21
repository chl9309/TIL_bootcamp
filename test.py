num = int(input())
div = []
for i in range(num):
    
    div += list(i) if num % i == 0 else

print(div)