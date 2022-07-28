# 여기에 필요한 모듈을 추가합니다.
from multiprocessing import BoundedSemaphore
import random
import json
from socket import SOMAXCONN

from pip import main

class Lotto:
    # 2-2. 생성자 작성
    def __init__(self):
        
        self.number_lines = []

    # 2-3. n 줄의 로또 번호를 생성하는 인스턴스 메서드
    def generate_lines(self, n):
        pass
        number_lines = []
        for i in range(n):
            lotto_numbers = list(random.sample(range(1,46), 6))
            lotto_numbers.sort()
            self.number_lines.append(lotto_numbers)

        #line_nubers = [sorted(list(random.sample(range(1,46), 6))) for _ in range(n)]
        ## [표현식] => [num for num i in range(10)]
        # a = [0,1,2,3,4,5,6,7,8,9]
        # return line_numbers
    # 3-2. 회차, 추첨일, 로또 번호 정보를 출력하는 인스턴스 메서드
    def print_number_lines(self, draw_number):
        
        year, month, day = self.get_draw_date(draw_number)

        print('==========================================')
        print(f'             제 {draw_number} 회 로또')
        print('==========================================')
        print(f'추첨일 : {year}/{month}/{day}')
        print('==========================================')
        
        for i in range(len(self.number_lines)):
            
            print(f'{chr(65+i)} : {self.number_lines[i]}')
            

    # 4-2. 해당 회차의 당첨 번호와 당첨 결과를 출력하는 인스턴스 메서드
    def print_result(self, draw_number):
        
        main_numbers , bonus_number = self.get_lotto_numbers(draw_number)

        print('==========================================')
        print(f'당첨 번호 : {main_numbers} + {bonus_number}')
        print('==========================================')

        for i in range(len(self.number_lines)):
            same_main_counts, is_bonus = self.get_same_info(main_numbers, bonus_number, self.number_lines[i])
            ranking = self.get_ranking(same_main_counts, is_bonus)
            print(ranking)
            if ranking == 1:
                print_ranking = '1등 당첨!'
            elif ranking == 2:
                print_ranking = '2등 당첨!'
            elif ranking == 3:
                print_ranking = '3등 당첨!'
            elif ranking == 4:
                print_ranking = '4등 당첨!'
            elif ranking == 5:
                print_ranking = '5등 당첨!'
            elif ranking == -1:
                print_ranking = '낙첨'

 
            if is_bonus:
                print(f'{chr(65+i)} : {same_main_counts}개 일치 + 보너스 일치 ({print_ranking})')

            else:
                print(f'{chr(65+i)} : {same_main_counts}개 일치 ({print_ranking})')


        

    # 3-3. 해당 회차 추첨일의 년, 월, 일 정보를 튜플로 반환하는 스태틱 메서드
    @staticmethod
    def get_draw_date(draw_number):
        pass
        
        date_json = open(f'./data/lotto_{draw_number}.json' , encoding='utf-8')
        split_data = json.load(date_json)
        date_info = split_data.get('drwNoDate')
        year, month, day = date_info.split('-')
        
        return year, month, day

    # 4-3. 해당 회차 당첨 번호의 메인 번호와 보너스 번호가 담긴 튜플을 반환하는 스태틱 메서드
    @staticmethod
    def get_lotto_numbers(draw_number):
        
        main_numbers = []
        date_json = open(f'./data/lotto_{draw_number}.json' , encoding='utf-8')
        split_data = json.load(date_json)
        for i in range(1,7):
            
            main_numbers.append(split_data[f'drwtNo{i}']) #get 은 값이 없어도 None 값을 들고오고 리스트 좌표는 값이 없으면 에러를 뿜는다.
            
        main_numbers.sort()
        bonus_number = split_data.get('bnusNo')

        return main_numbers, bonus_number

    # 4-4. 한 줄의 로또 번호와 메인 번호가 일치하는 개수와 보너스 번호 일치 여부가 담긴 튜플을 반환하는 스태틱 메서드
    @staticmethod
    def get_same_info(main_numbers, bonus_number, line):
        
        same_main_counts = 0
        is_bonus = False
        for i in range(len(main_numbers)):
            for j in range(len(line)):
                if main_numbers[i] == line[j]:
                    same_main_counts += 1

        for k in range(len(line)):
            if bonus_number == line[k]:
                is_bonus = True
    

        return same_main_counts, is_bonus

    # 4-5. 당첨 결과를 정수로 반환하는 스태틱 메서드
    @staticmethod
    def get_ranking(same_main_counts, is_bonus):
        
        
        if same_main_counts == 6:
            ranking = 1
        
        elif same_main_counts == 5:
            ranking = 2 if is_bonus else 3
        
        elif same_main_counts == 4:
            ranking = 4
        
        elif same_main_counts == 3:
            ranking = 5
        
        else:
            ranking = -1

        return ranking


#value = 3 if n>3 else 1: