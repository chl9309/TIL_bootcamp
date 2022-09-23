import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for test_case in range(T):

    day_pay, month_pay, quarter_pay, year_pay = map(int, input().split())
    plan = list(map(int, input().split()))

    month_cost = [0] * 12

    for i in range(12):
        if (plan[i] * day_pay) <= month_pay:
            month_cost[i] = plan[i] * day_pay

        else:
            month_cost[i] = month_pay

    min_cost = sum(month_cost)
    j = 0
    while j < 11:

        if sum(plan[j:j + 2]) > quarter_pay:
            if j < 9:
                if (sum(plan[j + 1:j + 3]) > sum(plan[j:j + 2])) and (sum(plan[j + 2:j + 4]) > sum(plan[j:j + 2])):
                    min_cost -= sum(plan[j:j + 2])
                    min_cost += quarter_pay
                    j += 2
            elif j < 10:
                if sum(plan[j + 1:j + 3]) > sum(plan[j:j + 2]):
                    min_cost -= sum(plan[j:j + 2])
                    min_cost += quarter_pay
                    j += 2
            elif j == 10:
                min_cost -= sum(plan[j:j + 2])
                min_cost += quarter_pay
                j += 2
        j += 1

    j = 1

    while j < 11:

        if sum(plan[j:j + 2]) > quarter_pay:
            if j < 9:
                if (sum(plan[j + 1:j + 3]) > sum(plan[j:j + 2])) and (sum(plan[j + 2:j + 4]) > sum(plan[j:j + 2])):
                    min_cost -= sum(plan[j:j + 2])
                    min_cost += quarter_pay
                    j += 2
            elif j < 10:
                if sum(plan[j + 1:j + 3]) > sum(plan[j:j + 2]):
                    min_cost -= sum(plan[j:j + 2])
                    min_cost += quarter_pay
                    j += 2
            elif j == 10:
                min_cost -= sum(plan[j:j + 2])
                min_cost += quarter_pay
                j += 2
        j += 1

    j = 2
    while j < 11:

        if sum(plan[j:j + 2]) > quarter_pay:
            if j < 9:
                if (sum(plan[j + 1:j + 3]) > sum(plan[j:j + 2])) and (sum(plan[j + 2:j + 4]) > sum(plan[j:j + 2])):
                    min_cost -= sum(plan[j:j + 2])
                    min_cost += quarter_pay
                    j += 2
            elif j < 10:
                if sum(plan[j + 1:j + 3]) > sum(plan[j:j + 2]):
                    min_cost -= sum(plan[j:j + 2])
                    min_cost += quarter_pay
                    j += 2
            elif j == 10:
                min_cost -= sum(plan[j:j + 2])
                min_cost += quarter_pay
                j += 2
        j += 1

    if min_cost > year_pay:
        min_cost = year_pay

    print(f'#{test_case+1} {min_cost}')
