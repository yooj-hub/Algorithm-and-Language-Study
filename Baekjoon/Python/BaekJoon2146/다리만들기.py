'''
# /*
#  * BaekJoon 2146 다리만들기
#  * programmer: yooj
#  * Date: 21.07.27
#  * using: Pycharm  & Python3
#  * Site: https://www.acmicpc.net/problem/2146
#  */
'''

import sys
from collections import deque

# 움직일 방향 설정
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

# 지도의 크리를 입력 받음
n = int(sys.stdin.readline())

# 지도를 입력할 배열
data = []

# 방문했는지 확인하는 배열
visited = [[False] * n for _ in range(n)]

# 다리를 놓을 때 사용할 배열
graph = [[-1] * n for _ in range(n)]

# 지도를 입력받음
for _ in range(n):
    data.append(list(map(int, sys.stdin.readline().split())))
# 덱 2개를 선언함
q = deque()
q2 = deque()
cnt = 0
# 1번섬 2번섬을 bfs 탐색을 통하여 1번섬이면 1로 기록하고 2번섬이면 2로 기록함
for i in range(n):
    for j in range(n):
        if data[i][j] != 0 and not visited[i][j]:
            cnt += 1
            q.append((i, j))
            data[i][j] = cnt
            visited[i][j] = True
            while q:
                x, y = q.popleft()
                q2.append((x, y))  # 섬인 곳을 전부 q2에 저장함
                graph[x][y] = 0  # 섬인 곳은 0 으로 기록
                for s in range(4):
                    nx = x + dx[s]
                    ny = y + dy[s]
                    if nx < 0 or ny < 0 or nx >= n or ny >= n:
                        continue
                    if data[nx][ny] == 0:  # 바다일 경우 continue
                        continue
                    if not visited[nx][ny]:
                        visited[nx][ny] = True
                        q.append((nx, ny))
                        data[nx][ny] = cnt

ans = 10000  # 정답보다 충분히 큰수를 ans 로 설정
# bfs 를 활용한 풀이 섬의 외곽을 확장시켜 서로 만났을 때 확장 된 거리의 합이 다리의 길이임
while q2:
    x, y = q2.popleft()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or ny < 0 or nx >= n or ny >= n:
            continue
        if data[nx][ny] == data[x][y]:  # 같은 섬일 경우 continue
            continue
        # data[nx][ny]==0 이면 들리지 않은 섬임을 알 수 있음
        if data[nx][ny] == 0:
            graph[nx][ny] = graph[x][y] + 1
            data[nx][ny] = data[x][y]
            q2.append((nx, ny))
        # graph 의 값이 -1 이 아닐경우 이미 방문한 곳이고, data[nx][ny]!=data[nx][ny] 가 성립하면 같은 섬이아님
        elif graph[nx][ny] >= 0 and data[nx][ny] != data[x][y]:
            ans = min(ans, graph[nx][ny] + graph[x][y])  # 서로 만났음

sys.stdout.write(str(ans))
