from re import X


def over(scores):
    pass
    # 여기에 코드를 작성합니다.

    y = 0
    for i in range(len(scores)):

        if 60 <= scores[i]:
            
            
            y += 1

    return y

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    scores = [30, 60, 90, 70]
    print(over(scores)) # 3
