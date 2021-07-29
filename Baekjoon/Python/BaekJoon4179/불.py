'''
# /*
#  * BaekJoon 4179 불!
#  * programmer: yooj
#  * Date: 21.07.29
#  * using: Pycharm  & Python3
#  * Site: https://www.acmicpc.net/problem/4179
#  */
'''
import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())
data = []
for i in range(n):
    data.append(sys.stdin.readline().rstrip())
a = [[0] * m for _ in range(n)]  # 맵 및 사람이 이동하는데 걸린 시간을 표시할 배열
f = [[1000] * m for _ in range(n)]  # 불의 이동시간을 표시할 배열
q = deque()  # 사람에 대한 bfs 를 시행할 배열
fire = deque()  # 불에대해 bfs 를 시행할 배열

for i in range(n):
    for j in range(m):
        if data[i][j] == '#':  # 벽일 경우 -1 로 저장
            a[i][j] = -1
        elif data[i][j] == '.':  # . 일경우 0 으로저장
            a[i][j] = 0
        elif data[i][j] == 'J':  # J 일 경우 J 의 위치를 0으로 저장하고 큐에 넣음
            q.append((i, j))
            a[i][j] = 1
        elif data[i][j] == 'F':  # F 일 경우 F의 위치를 -1 로저장하고 F에 넣음
            fire.append((i, j))
            a[i][j] = -1
            f[i][j] = 1  # 시작을 1초로 저장

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
while fire:  # 불의 BFS
    x, y = fire.popleft()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or ny < 0 or nx >= n or ny >= m:
            continue
        if a[nx][ny] == -1:
            continue
        if f[nx][ny] == 1000:
            f[nx][ny] = f[x][y] + 1
            fire.append((nx, ny))
while q:  # 사람의 BFS
    x, y = q.popleft()
    if x == n - 1 or y == m - 1 or x == 0 or y == 0:  # 외곽일 경우 정답
        sys.stdout.write(str(a[x][y]))
        exit(0)
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or ny < 0 or nx >= n or ny >= m:
            continue
        if a[nx][ny] == -1:
            continue
        if f[nx][ny] > a[x][y] + 1 and a[nx][ny] == 0:  # 사람의 시간 +1 보다 불의 시간이 적을경우갈 수 있음
            a[nx][ny] = a[x][y] + 1
            q.append((nx, ny))

sys.stdout.write("IMPOSSIBLE\n")
