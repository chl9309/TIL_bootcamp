#num = int(input())
#div = []
#for i in range(num):
#    
#    div += list(i) if num % i == 0 else
#
#print(div)


#
#def leap_year(year):
#
#    this_year = True
#
#    if year % 4:
#
#        this_year = False
#
#    else:
#
#        if year % 100:
#
#            this_year = True
#
#        else:
#
#            if year % 400:
#
#                this_year = False
#            
#            else:
#
#                this_year = True
#
#    if this_year:
#
#        result = f'{year}은 윤년입니다.'
#
#    else:
#
#        result = f'{year}은 윤년이 아닙니다'
#
#    return result
#
#
#print(leap_year(2021))
#print(leap_year(2020))








#def duplicated_letters(data):
#
#    data_list = data.split()
#    duplicated_no = []
#    duplicated_yes = []
#
#    for i in range(len(data_list)):
#
#        for j in range(len(duplicated_no)):
#
#            if data_list[i] == duplicated_no[j]:
#
#                duplicated_yes.append(data_list[i])
#            
#            else:
#
#                duplicated_no.append(data_list[i])
#
#    return duplicated_yes
#
#
#
#print(duplicated_letters('apple')) # => ['p']
#print(duplicated_letters('banana')) # => ['a', 'n']




#def low_and_up(dataorigin):
#
#    data = dataorigin.split()
#    result= []
#
#    for i in range(len(data)):
#        
#        j = data[i]
#        if i % 2:
#
#            result.append(j.lower())
#            
#        
#        else:
#
#            result.append(j.upper())
#            
#    
#    return result
#
#
#print(low_and_up('apple')) # => aPpLe
#print(low_and_up('banana')) # => bAnAnA


#
#def lonely(data):
#
#    result = []
#    
#    i= 1
#
#    while i < len(data):
#
#        if i == 0:
#            
#            result.append(data[i])
#
#        else:
#            
#            if data[i] == result[i-1]:
#
#                pass
#            else:
#                result.append(data[i])
#
#        i += 1
#
#    return result
#
#
#
#lonely([1, 1, 3, 3, 0, 1, 1]) # => [1, 3, 0, 1]
#lonely([4, 4, 4, 3, 3]) # => [4, 3]



#def salt(density , gram):
#
#    result = density * gram / 100
#
#    return result
#saltlist = []
#saltwaterlist = []
#i =0
#while i<5:
#
#    x = input()
#
#    if x == 'Done':
#        break
#    
#    den , gr = int(x[: x.split('%')]), int(x[x.find(' ') + 1 : x.find('g')])
#
#    saltlist.append(salt(den , gr))
#    saltwaterlist.append(gr)
#
#salt_result = sum(saltlist)
#saltwater_result = sum(saltwaterlist)
#
#print(f'{salt_result},{saltwater_result}')
#
#


#from ast import Str
#
#
#class Doggy:
#
#    birth_of_dog = 0
#    num_of_dog = 0    
#    
#    def __init__(self, name, breed):
#        self.name = name
#        self.breed = breed
#
#    def bark():
#        print('bow! wow!')
#
#    def get_status():
#        print(Doggy.birth_of_dog, Doggy.num_of_dog)
#
#
#Doggy.get_status()
#        
#
#
#bool


class Animal:
    def __init__(self, name):
        self.name = name
    
    def walk(self):
        print(f'{self.name}! 걷는다!')
    
    def eat(self):
        print(f'{self.name}! 먹는다!')



class Dog(Animal):

    def __init__(self, name):
        super().__init__(name)

    def run(self):
        print(f'{self.name}! 걷는다!')
    
    def brak(self):
        print(f'{self.name}! 짖는다!')


class Bird(Animal):
    
    def __init__(self, name):
        super().__init__(name)

    def fly(self):
        print(f'{self.name}! 푸드덕!')


dog = Dog('꼽이')
dog.run() # 꼽이! 달린다!
dog.brak() # 꼽이! 짖는다!

bird = Bird('구구')
bird.walk() # 구구! 걷는다!
bird.eat() # 구구! 먹는다!
bird.fly() # 구구! 푸드덕! 