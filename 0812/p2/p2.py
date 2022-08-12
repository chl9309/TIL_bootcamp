def itoa(num):
    pass

    # 넘겨 받은 정수를 0이 되기 전까지 계속 반복
    # 1의 자리 수 부터 끊어서 문자열로 변환
    # atoi -> ord(char) -('0')

    # 만약 처음 넘겨 받은 값이 음수였다면
    # 문자열 앞에 '-'를 붙여서 반환한다.

    a = abs(num)
    print(len(a))

    result = ''
    for i in range(len(a)):
        dum = a % 10
        a //= 10
        result += chr(dum)
    return result


def itoa2(num):
    negative = False
    if num < 0:
        negative = True
        num = -num
    if not num:
        return '0'
    result=0
    while num:
        remainder = num%10
        result += chr(ord('0' + remainder))
        num = num // 10

    if negative:
        return '-' +result
    else:
        return result

print(itoa2(3))
print(itoa2(0))
print(itoa2(-3))
