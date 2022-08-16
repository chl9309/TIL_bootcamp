import sys
sys.stdin = open('test_input.txt', encoding='utf-8')

def make_lps(p):
    # 중계 리스트
    lps = [0] * len(p)

    # lps를 위한 prefix의 index
    j = 0
    # 전체 순회는

    for i in range(1, len(p)):
        # prefix와 suffix가 같을때
        if p[j] == p[i]:
            lps[i] = j + 1
            j += 1

        #다르면, j를 0으로 초기화
        # pattern의 첫 글자와 다시 비교하도록 만들어야 한다.

        # 현재 순회중인 자리 (i)와 0번째로 돌아간 pattern이
        # 또 다시 일치하는지 확인

    return lps


def KMP(search, target):
    lps = make_lps(search)

    s_idx, t_idx = 0, 0
    count = 0

    while t_idx < len(target):
        if search[s_idx] == target[t_idx]:
            t_idx += 1
            s_idx += 1
        else:
            # s_idx가 0이 아니라면
            if s_idx != 0:
                # lps를 써서 다음 조사 대상 수색
                s_idx = lps[s_idx - 1]

            #p_idx == 0 이라면
            #t_idx를 한 칸 증가시켜서
            #search의 첫번째 글자와 다음 target 조사대상이랑 바꾼다
            else:
                t_idx += 1
    return count


for test_case in range(10):
    tc = int(input())
    search = input()
    target = input()

    result = KMP(search, target)
    #print(result)M,./
