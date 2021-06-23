'''
 * Programmers 연구소
 * programmer: yooj
 * using : pycharm & python 3.9.5
 * Date: 21.06.23
 * Site: https://www.acmicpc.net/problem/14502
'''

import copy
from itertools import combinations

n, m = map(int, input().split())
data = []
for i in range(n):
    data.append(list(map(int, input().split())))
#빈 곳 배열을 얻음
blank = []
for i in range(n):
    for j in range(m):
        if data[i][j] == 0:
            blank.append((i, j))
#combinations를 이용하여 벽을 칠 수 있는 모든 쌍을 구함
wall = list(combinations(blank, 3))

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
cnt = 0

#바이러스가 있는위치에서 dfs 실행
def dfs(x, y):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m:
            if d[nx][ny] == 0:
                d[nx][ny] = 2
                dfs(nx, ny)

result = -1

for z in wall:#모든 벽의 쌍 wall의 원소인 z에 대하여
    d = copy.deepcopy(data)#d는 data의 deepcopy
    for x in z:
        d[x[0]][x[1]] = 1

    for i in range(n):
        for j in range(m):
            if d[i][j] == 2:
                dfs(i, j)


    def check():#0의 개수를 체크함
        ans = 0
        for i in range(n):
            for j in range(m):
                if d[i][j] == 0:
                    ans += 1
        return ans

    result = max(check(), result)

print(result)
