import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for test_case in range(T):

    N, M = map(int, input().split())
    data = list(map(int, input().split()))
    student = [{i+1} for i in range(N)]

    data2 = []
    for i in range(0, 2*M, 2):
        data2.append([data[i], data[i+1]])

    for i in range(len(data2)):
        flag = False

        for j in range(len(student)):
            if data2[i][0] in student[j]:

                for k in range(len(student)):
                    if (data2[i][1] in student[k]) and j != k: # 자기 자신을 지목하는 엣지케이스 예방

                        student[j] = student[j].union(student[k])
                        student.remove(student[k])

                        flag = True
                        break
            if flag:
                break

    result = len(student)
    print(f'#{test_case+1} {result}')
