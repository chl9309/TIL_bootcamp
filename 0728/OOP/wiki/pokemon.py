# class 정의를 위해 class Class_Name
#from curses import meta
#from re import L


class Pokemon:
    #푸키먼들이 공통적으로 가지는 속성들
    # 클래스 변수
    info = '푸키먼'
    population = 0 # 포켓몬들의 수 , 태어날 때 마다 증가
    bell_population = 0
    # 생성자
    def __init__(self, name, lv=1):
        self.name = name
        self.lv = lv =1
        self.skill = '몸통 박치기'
        self.info = name[:2]*2
        Pokemon.population += 1
        self.increase()

    def attack(self):
        return self.skill

    @classmethod
    def increase(cls):
        cls.bell_population += 1
#pikachu = Pokemon('피카츄')
#metamon = Pokemon('메타몽', lv=5)
#
#print (pikachu.name, metamon.lv)
#print (metamon.name, metamon.lv)
#print (pikachu.info, metamon.info)

