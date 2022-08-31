import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for test_case in range(T):

    N = int(input())
    world = [list(map(int, input().split())) for _ in range(N)]




#▶ 최대한 많은 Core에 전원을 연결하였을 경우, 전선 길이 합을 구하고자 한다.
#
#  단, 여러 방법이 있을 경우, 전선 길이의 합이 최소가 되는 값을 구하라.
#Core와 전원을 연결하는 전선은 직선으로만 설치가 가능하며,
#전선은 절대로 교차해서는 안 된다.

