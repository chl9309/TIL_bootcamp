import sys

sys.stdin = open('sample_input.txt')

T = int(input())

for test_case in range(T):

    str1 = input()
    str2 = input()
    result, max = 0, 0

    str1_set = list(set(str1))

    for i in range(len(str1_set)):
        count = 0
        for j in range(len(str2)):

            if str1_set[i] == str2[j]:
                count += 1

        if count >= max:
            result = str1_set[i]
            max = count

    print(f'#{test_case} {max}')

