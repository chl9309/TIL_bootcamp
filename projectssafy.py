
lis = list(map(int, input().split(',')))

lis_2 = []

for i in lis:
    if lis_2[-1:] != [i]:

        lis_2.append(i)
print(lis)    
print(lis_2)

