import sys
sys.stdin = open('input.txt')

for _ in range(10):

    test_case = int(input())
    data = list(map(int, input().split()))

    front = 0
    end = len(data) - 1

    tmp = data[0]
    this = 0
    brk = False

    while tmp > 0:

        for i in range(1, 6):

            data[this] -= i
            if data[this] < 1:
                data[this] = 0
                brk = True
                break

            this = (this + 1) % len(data)

        if brk:
            break

    result = []
    for j in range(1, len(data)+1):

        this_append = (this + j) % len(data)
        result.append(data[this_append])

    #print(f'#{test_case+1}', end=' ')
    #for k in range(len(data)):
    #    print(f'{result[k]}', end=' ')
    #print()

    print(f'#{test_case}', *result)