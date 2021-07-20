# /*
#  * BaekJoon 14889 스타트와 링크
#  * programmer: yooj
#  * Date: 21.07.20
#  * using: Pycharm  & Python3
#  * Site: https://www.acmicpc.net/problem/14889
#  */


import sys
from itertools import permutations

n = int(sys.stdin.readline())

data = []
for _ in range(n):
    data.append(list(map(int, sys.stdin.readline().split())))

answer = int(1e9)


def dfs(idx, team, n): # 팀을 탐색하는 함수
    global answer
    if len(team) == n // 2:
        getAnswer(team, n)

    if idx >= n:
        return
    team.append(idx)
    dfs(idx + 1, team, n)
    team.pop()
    dfs(idx + 1, team, n)


def getAnswer(team, n): # 정답을 구하는 함수
    global answer
    opponent = []
    for i in range(n):
        if i in team:
            continue
        opponent.append(i)
    opponentList = list(permutations(opponent, 2))
    teamList = list(permutations(team, 2))
    m = 0
    for i in range(len(opponentList)):
        m += data[teamList[i][0]][teamList[i][1]] - data[opponentList[i][0]][opponentList[i][1]]
    answer = min(answer, abs(m))


dfs(0, [], n)
print(answer)
