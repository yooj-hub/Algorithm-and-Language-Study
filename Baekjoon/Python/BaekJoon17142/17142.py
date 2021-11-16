import itertools
import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())

board = []
c = []
z = 0
for i in range(n):
    board.append(list(map(int, sys.stdin.readline().split())))

for i in range(n):
    for j in range(n):
        if board[i][j] == 2:
            c.append((i, j, 0))
        elif board[i][j] == 0:
            z += 1

can = list(itertools.combinations(c, m))
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
answer = -1
if z == 0:
    print(0)
    sys.exit(0)
for i in can:
    visited = [[False] * n for _ in range(n)]
    q = deque()
    k = 0
    check = False
    for j in i:
        q.append(j)
        visited[j[0]][j[1]] = True

    while q:
        if check:
            break
        x, y, t = q.popleft()

        for j in range(4):
            nx = x + dx[j]
            ny = y + dy[j]
            if nx < 0 or ny < 0 or nx >= n or ny >= n:
                continue
            if visited[nx][ny]:
                continue
            if board[nx][ny] == 1:
                continue
            elif board[nx][ny] == 2:
                q.append((nx, ny, t + 1))
                visited[nx][ny] = True
            else:
                visited[nx][ny] = True
                q.append((nx, ny, t + 1))
                k += 1
                if k == z:
                    if answer == -1 or answer > t:
                        answer = t + 1
                        check = True
                        break

print(answer)
