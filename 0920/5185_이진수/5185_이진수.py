import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for test_case in range(T):

    bit, hex_num = input().split()
    bin_num = []

    for i in hex_num:
        bin_list = []

        if i.isnumeric():
            now_num = int(i)

        else:
            now_num = int(ord(i)) - 55

        for j in range(4):

            bin_list.insert(0, now_num % 2)
            now_num //= 2

        bin_num.append(''.join([str(_) for _ in bin_list]))
    result = ''.join(bin_num)

    print(f'#{test_case+1} {result}')
