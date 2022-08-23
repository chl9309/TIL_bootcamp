def process_solution(arr, k, result):
    if result != 10:
        return

    for i in range(1, k+1):
        if arr[i]:
            print(data[i], end=' ')
    print()

# arr : 부분 집합을 구하기 위해 사용 하거나 하는 원소들
# k : 현재 조사 위치
# N : 최대 조사 위치
# result
def powershell(arr, k, n, result):
    pass

    c = [0] * MAXCANDIDATES

def construct_candidator(c):
    c

    # 언제까지 조사 할거냐
    if k == n:
        # 내가 원하는 수식이 만들어 졌는지 확인할 함수
        process_solution(arr, k, result)
    else:
        k += 1
        # 유망성 조사
        ncandidates = construct_candidator(c)
        for i in range(ncandidates):

            arr[k] = c[i]

            if arr[k]:
                powerset(arr, k, n, result + data[k])
            else:
                powerset(arr, k, n, result)
MAXCANDIDATES = 100
NMAX = 100

data = list(range(11))
