# /*
#  * BaekJoon 14501 퇴사
#  * programmer: yooj
#  * Date: 21.07.20
#  * using: Pycharm  & Python3
#  * Site: https://www.acmicpc.net/problem/14501
#  */


import sys

n = int(sys.stdin.readline()) # 일수를 입력 받음
data = []
for i in range(n): # 일수에 관한 가치를 설정함
    data.append(list(map(int, sys.stdin.readline().split())))
answer = 0


def dfs(idx, n, value): # idx 일때의 상담을 결정하는 함수
    if idx == n:  # idx == n 일 경우 모든 상담 종료
        global answer
        if answer < value: # 큰 값을 찾음
            answer = value
        return
    if idx > n:
        return
    dfs(idx + data[idx][0], n, value + data[idx][1]) # 상담 하는 경우
    dfs(idx + 1, n, value) # 상담을 하지 않는 경우


dfs(0, n, 0) # dfs
print(answer) # 정답 출력
