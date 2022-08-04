import re


def turn(temperatures):
    pass
    # 여기에 코드를 작성합니다.
    x = []
    y = []
    z = []
    for i in range(len(temperatures)):
        
        x = temperatures[i]
        
        if int(x[0]) >= int(x[1]):
            
            y.append(x[0])
            z.append(x[1])
        else:
            y.append(x[1])
            z.append(x[0])

    result = {'maximum' : y , 'minimum' : z}
    
    return result    

    


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    temperatures = [
        [9, 3],
        [9, 0],
        [11, -3],
        [11, 1],
        [8, -3],
        [7, -3],
        [-4, -12]
    ]
    print(turn(temperatures)) 
    # {
    #     'maximum': [9, 9, 11, 11, 8, 7, -4], 
    #     'minimum': [3, 0, -3, 1, -3, -3, -12]
    # }
