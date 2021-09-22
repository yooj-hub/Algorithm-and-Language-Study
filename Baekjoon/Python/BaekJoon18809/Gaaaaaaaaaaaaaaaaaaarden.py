"""
BaekJoon 18809 Gaaaaaaaaaarden
Programmer: yooj
Date: 2021 09 22
Using: Python 3 & pycharm
Site: https://www.acmicpc.net/problem/18809
"""


import itertools
import sys
from collections import deque

# n * m 의 지형, 녹색 배양액의 개수, 빨간색 배양액의 개수를 입력받음
n, m, g, r = map(int, sys.stdin.readline().split())
# 전체 지도를 입력 받음
a = []
for _ in range(n):
    a.append(list(map(int, sys.stdin.readline().split())))

able = []  # 배양액을 심을수 있는 토양의 리스트
for i in range(n):
    for j in range(m):
        if a[i][j] == 2:
            able.append((i, j))
# 배양액을 심을수 있는 토양의 인덱스
can = list(range(len(able)))
# itertools 의 combinations 를 이용하여 가능한 조합을 찾는다.
possible = list(itertools.combinations(can, g + r))
# 움직일 수 있는 방향
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
answer = 0
# 모든 조합에 대하여 확인한다.
for i in possible:
    # 비트 마스크를 이용한 모든 조합 확인
    for j in range(1 << (g + r)):
        g_list = []
        r_list = []
        for k in range(g + r):
            if j & (1 << k):
                g_list.append(k)
            else:
                r_list.append(k)
        # 조건에 맞을 경우 실행
        if len(g_list) == g and len(r_list) == r:
            # 빨간 배양액이 퍼진 시간을 기록
            r_visited = [[-1] * m for _ in range(n)]
            # 녹색 배양액이 퍼진 시간을 기록
            g_visited = [[-1] * m for _ in range(n)]
            # 꽃인지 아닌지 확인하는 배열
            is_flower = [[False] * m for _ in range(n)]
            q = deque()
            flower = 0
            # r -> 1
            # 빨간색 부터 삽입
            for l in r_list:
                q.append((able[i[l]][0], able[i[l]][1], 1))
                r_visited[able[i[l]][0]][able[i[l]][1]] = 0
            # g -> 2
            # 녹색 부터 삽입
            for l in g_list:
                q.append((able[i[l]][0], able[i[l]][1], 2))
                g_visited[able[i[l]][0]][able[i[l]][1]] = 0
            # BFS 를 이용하여 모든 배양액이 퍼질 시간을 구한다.
            while q:
                x, y, isRed = q.popleft()
                # 이미 꽃인 경우 생략
                if is_flower[x][y]:
                    continue
                # 모든 방향에 대하여 확인
                for z in range(4):
                    nx = x + dx[z]
                    ny = y + dy[z]
                    # 범위를 나갈경우 다음으로
                    if nx < 0 or ny < 0 or nx >= n or ny >= m:
                        continue
                    # 호수일 경우 다음으로
                    if a[nx][ny] == 0:
                        continue
                    # 이미 꽃인 경우 다음으로
                    if is_flower[nx][ny]:
                        continue
                    # 빨간색이 무조건 먼저 오므로 빨간색에서 꽃은 생기지 않는다. 양쪽다 방문하지 않았을 때 방문 처리
                    if isRed == 1 and g_visited[nx][ny] == -1 and r_visited[nx][ny] == -1:
                        r_visited[nx][ny] = r_visited[x][y] + 1
                        q.append((nx, ny, isRed))
                    # 녹색일 경우
                    if isRed == 2 and g_visited[nx][ny] == -1:
                        # 빨간색이 오지 않았을 경우 방문 처리
                        if r_visited[nx][ny] == -1:
                            g_visited[nx][ny] = g_visited[x][y] + 1
                            q.append((nx, ny, isRed))
                        # 빨간색이 방문한 시간과 녹색이 방문하려는 시간이 같으면 꽃을 추가해준다.
                        elif r_visited[nx][ny] == g_visited[x][y] + 1:
                            flower += 1
                            is_flower[nx][ny] = True
            answer = max(answer, flower)
print(answer)
