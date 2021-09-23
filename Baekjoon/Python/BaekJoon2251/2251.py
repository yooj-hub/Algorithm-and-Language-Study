"""
BaekJoon 2251 물통
Programmer: yooj
Date: 2021 09 23
Using: Python 3 & pycharm
Site: https://www.acmicpc.net/problem/2251
"""

import sys
from collections import deque

a, b, c = map(int, sys.stdin.readline().split())
all = c
visited = [[False] * (all + 1) for _ in range(all + 1)]
# 중복 처리를 위한 set 사용
possible = set()
q = deque()
q.append((0, 0))
visited[0][0] = True
while q:
    x, y = q.popleft()
    z = all - x - y
    # 문제에 제시한 조건
    if x == 0:
        possible.add(z)
    # x 를 다른 물통에 넣는 경우
    if x != 0:
        # 물통2 에 넣는 경우
        # 가득 찰 경우 물통2 에 b 만큼 넣고 나머지를 물통1 에 넣음
        # 아래도 다 동일한 과정
        if x + y >= b:
            if not visited[x + y - b][b]:
                visited[x + y - b][b] = True
                q.append((x + y - b, b))
        else:
            if not visited[0][x + y]:
                visited[0][x + y] = True
                q.append((0, x + y))
        if x + z >= c:
            if not visited[x + z - c][y]:
                visited[x + z - c][y] = True
                q.append((x + z - c, y))
        else:
            if not visited[0][y]:
                q.append((0, y))
    # y 를 다른 물통에 넣는 경우
    if y != 0:
        if x + y >= a:
            if not visited[a][x + y - a]:
                visited[a][x + y - a] = True
                q.append((a, x + y - a))
        else:
            if not visited[x + y][0]:
                visited[x + y][0] = True
                q.append((x + y, 0))
        if y + z >= c:
            if not visited[x][z + y - c]:
                visited[x][z + y - c] = True
                q.append((x, z + y - c))
        else:
            if not visited[x][0]:
                visited[x][0] = True
                q.append((x, 0))
    # z 를 다른 물통에 넣는 경우
    if z != 0:
        if x + z >= a:
            if not visited[a][y]:
                visited[a][y] = True
                q.append((a, y))
        else:
            if not visited[x + z][y]:
                visited[x + z][y] = True
                q.append((x + z, y))
        if y + z >= b:
            if not visited[x][b]:
                visited[x][b] = True
                q.append((x, b))
        else:
            if not visited[x][y + z]:
                visited[x][y + z] = True
                q.append((x, y + z))

possible = list(possible)
possible.sort()
print(' '.join(map(str, possible)))
