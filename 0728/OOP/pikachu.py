from cmath import pi
from re import L
from xml.etree.ElementTree import PI
from wiki.pokemon import Pokemon



class Pikachu(Pokemon):
    no = 25

    def __init__(self, name, lv=5):

        super().__init__(name, lv)
        self.skill = '전기 충격'

    def attack(self):
        return '찌릿 찌릿'
    
    def walk():
        return '뚜벅 뚜벅'


class Metamon(Pokemon):
    no = 132

    def __init__(self, name, lv=1):
        super().__init__(name, lv)
        self .skill = '변신'


    def attack(self):
        return '쮸오옹'

    def eat(self):
        return '쩌업'


class Child(Pikachu, Metamon):
    pass

class Brother(Metamon, Pikachu):
    pass



ch = Child('메타몽')
print(ch.name)
print(ch.skill)
print(ch.attack())
print(ch.eat())
print(Pikachu.bell_population)
print(Metamon.bell_population)
print(Child.bell_population)


pikachu = Pikachu('피카츄')

#print(pikachu.info)
#print(pikachu.skill)
#print(Pokemon.population)
#print(Pikachu.bell_population)

metamon = Metamon('메타몽')

#print(metamon.info)
#print(metamon.skill)
#print(Pokemon.population)
#print(Metamon.bell_population)