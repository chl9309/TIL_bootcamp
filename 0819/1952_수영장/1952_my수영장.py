import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for test_case in range(T):

    day, month, third, year = map(int, input().split())
    plan = list(map(int, input().split()))
    cnt = [0, 0, 0, 0]
    result = 0
    tmp = 0
    tmp2 = 0
    month_plan = [0] * 12

    for day_sum in range(12):
        tmp += plan[day_sum]

    cnt[0] = tmp
    minimum = tmp * day

    for month_try in range(12):

        if (plan[month_try] * day) >= month:
            cnt[0] -= plan[month_try]
            cnt[1] += 1
            month_plan[month_try] = 1
    tmp3 = 0
    for third_try in range(12):

        if third_try <10:
            for x in range(3):
                if month_plan[third_try]:
                    tmp3 += month
                else:
                    tmp3 += (plan[third_try] * day)
        elif third_try == 10:
            for x in range(2):
                if month_plan[third_try]:
                    tmp3 += month
                else:
                    tmp3 += (plan[third_try] * day)
        elif third_try == 11:
                if month_plan[third_try]:
                    tmp3 += month
                else:
                    tmp3 += (plan[third_try] * day)

        #if tmp3 <=

    print(cnt)


