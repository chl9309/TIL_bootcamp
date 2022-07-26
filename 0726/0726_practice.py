import random  # 랜덤 모듈 활용

print("================================")
print("        Battle Ship Game        ")
print("            START !!            ")
print("================================")

# 필요에 따라 추가적으로 함수를 만들어 자유롭게 활용할 수 있습니다.
# 각자의 해역에 배를 위치시키는 함수
def set_ship(index, sea):
    
    sea[index] = 1
    sea[index+1] = 1
    sea[index+2] = 1


player_sea = [0] * 15  # 플레이어의 해역
player_attacked = [False] * 15  # 플레이어의 공격 위치 기록

computer_sea = [0] * 15  # 컴퓨터의 해역
computer_attacked = [False] * 15  # 컴퓨터의 공격 위치 기록

round = 1  # 게임 라운드

# 1. 게임 준비
while True:

    player_ship = False


    

    # 1-1) 플레이어의 배 시작 위치 고르기
    while True:
        player_index = int(input('배를 위치시킬 시작점을 고르세요:'))
    # 1-2) 범위를 벗어난 시작점을 고른 경우
        if player_index < 0 or player_index > 14:
            print('-----해당 위치에는 배를 둘 수 없습니다.-----')
        else:
            break
        

# 1-3) 컴퓨터의 배 시작 위치를 랜덤으로 지정합니다.
    computer_index = int(random.randrange(0,14))
# 1-4) 플레이어와 컴퓨터의 해역에 각각 배 위치시키기
    set_ship(player_index ,player_sea)

    set_ship(computer_index ,computer_sea)

    break


# 2. 라운드 진행
while True:
    
    # 2-1) 플레이어 공격

    print('< Information Board >')
    print(f'플레이어의 해역: {player_sea}')
    print(f'플레이어의 공격 기록: {player_attacked}')


    # 2-2) 플레이어의 공격 위치 선택
    player_attack_index = int(input('공격할 위치를 선택하세요: '))

    # 2-3) 플레이어의 공격이 성공한 경우
    if computer_sea[player_attack_index]:
        print(f'<{round}라운드 결과!>')
        print(f'컴퓨터의 해역 : {computer_sea}')
        print(f'플레이어는 컴퓨터의 해역 {player_attack_index}번째 칸을 공격하였고, 컴퓨터의 배는 피격되었습니다.')
        print(f'게임이 종료되었습니다! {round}라운드 만에 플레이어의 승리입니다!')
        break


    # 2-4) 플레이어의 공격이 실패한 경우
    else:
        player_attacked[player_attack_index-1] = True
        

    # 2-5) 컴퓨터의 공격 위치 지정
    
    while True:
        computer_attack_index = int(random.randrange(0,16))

    # 컴퓨터가 공격하지 않은 위치를 나타내는 리스트
        if computer_attacked[computer_attack_index-1]:
            pass
        else:
            computer_attacked[computer_attack_index-1] = True
            break
    

    # 2-6) 컴퓨터의 공격이 성공한 경우
    if player_sea[computer_attack_index]:
        print(f'<{round}라운드 결과!>')
        print(f'플레이어는 컴퓨터의 해역 {player_attack_index}번째 칸을 공격하였으나, 공격에 실패하였습니다!')
        print(f'컴퓨터의 해역 {computer_attack_index}번째 칸을 공격하였고, 플레이어의 배는 피격되었습니다.')
        print(f'게임이 종료되었습니다! {round}라운드 만에 컴퓨터의 승리입니다!')
        break
    # 2-7) 컴퓨터의 공격이 실패한 경우
    else:
        print(f'플레이어는 컴퓨터의 해역 {player_attack_index}번째 칸을 공격하였으나, 공격에 실패하였습니다!')
        print(f'컴퓨터는 플레이어의 해역 {computer_attack_index}번째 칸을 공격하였으나, 공격에 실패하였습니다!')
