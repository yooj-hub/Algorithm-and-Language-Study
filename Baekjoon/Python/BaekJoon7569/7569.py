import sys
from collections import deque

n, m, h = map(int, sys.stdin.readline().split())
check = [[[False] * n for _ in range(m)] for _ in range(h)]

dx = [0, 0, 1, -1, 0, 0]
dy = [1, -1, 0, 0, 0, 0]
dz = [0, 0, 0, 0, 1, -1]
data = [[] for _ in range(h)]
for i in range(h):
    for j in range(m):
        data[i].append(list(map(int, sys.stdin.readline().split())))

q = deque()
r = 0
for i in range(h):
    for j in range(m):
        for k in range(n):
            if data[i][j][k] == 1:
                q.append((i, j, k))
                check[i][j][k] = True
            elif data[i][j][k] == 0:
                r += 1
answer = 0

while q:
    x, y, z = q.popleft()
    for i in range(6):
        nx = x + dx[i]
        ny = y + dy[i]
        nz = z + dz[i]
        if nx < 0 or ny < 0 or nz < 0 or nx >= h or ny >= m or nz >= n:
            continue
        if check[nx][ny][nz]:
            continue
        if data[nx][ny][nz] != 0:
            continue
        q.append((nx, ny, nz))
        check[nx][ny][nz] = True
        data[nx][ny][nz] = data[x][y][z] + 1
        r -= 1
        if answer < (data[nx][ny][nz] - 1):
            answer = (data[nx][ny][nz] - 1)

if r == 0:
    print(answer)
else:
    print(-1)
