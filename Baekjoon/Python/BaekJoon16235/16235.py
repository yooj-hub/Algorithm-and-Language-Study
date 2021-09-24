"""
BaekJoon 16235 나무 재태크
Programmer: yooj
Date: 2021 09 24
Using: Python 3 & pycharm
Site: https://www.acmicpc.net/problem/16235
"""
import heapq
import sys
from collections import deque

n, m, k = map(int, sys.stdin.readline().split())
# 겨울에 얻는 양분의 량
b = [[0] * n for _ in range(n)]
# 현재 양분의 상태
cur = [[5] * n for _ in range(n)]
# 나무가 심어지는 방향
dx = [-1, -1, -1, 0, 1, 1, 1, 0]
dy = [-1, 0, 1, 1, 1, 0, -1, -1]
q = []
for i in range(n):
    line = list(map(int, sys.stdin.readline().split()))
    for j in range(n):
        b[i][j] = line[j]
# 리스트에 양분, 현재 위치를 입력받음
for _ in range(m):
    x, y, z = map(int, sys.stdin.readline().split())
    q.append((z, x - 1, y - 1))
q.sort()
q = deque(q)
# k 시간 만큼 진행
for _ in range(k):
    # Spring & Summer
    # 번식하는 나무
    hatched_list = []
    # 죽어서 생기는 양분을 뜻함
    c = [[0] * n for _ in range(n)]
    # 모든 나무에 대하여 연산 해야한다.
    for v in range(len(q)):
        # 현재 나무의 나이, r , c
        current_tree, i, j = q.popleft()
        # 양분 보다 나이가 많을 경우 해당 나무를 죽이고 양분으로 만든다.
        if current_tree > cur[i][j]:
            c[i][j] += (current_tree // 2)
        # 그 외엔 양분을 나이만큼 빼고 다시 큐의 오른쪽에 추가한다.
        else:
            cur[i][j] -= current_tree
            q.append((current_tree + 1, i, j))
            if (current_tree + 1) % 5 == 0:
                hatched_list.append((i, j))
    # Fall
    for hatch in hatched_list:
        x, y = hatch[0], hatch[1]
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= n:
                continue
            # 나무의 나이가 1일 경우 제일 적으므로 큐의 왼쪽에 추가한다.
            q.appendleft((1, nx, ny))
    # Winter
    # 죽어서 생긴 양분과 겨울에 얻는 양분을 현재 상태에 더해준다.
    for i in range(n):
        for j in range(n):
            cur[i][j] += b[i][j] +c[i][j]

print(len(q))
