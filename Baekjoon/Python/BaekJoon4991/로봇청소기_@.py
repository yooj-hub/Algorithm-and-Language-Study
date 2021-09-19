"""
BaekJoon 4991 로봇 청소기
Programmer: yooj
Date: 2021 09 19
Using: Python 3 & pycharm
Site: https://www.acmicpc.net/problem/4991
"""

import itertools
import sys
from collections import deque

# 이동 방향
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

while True:
    # 크기를 입력 받음
    w, h = map(int, sys.stdin.readline().split())
    # 종료 조건 처리
    if w == 0 and h == 0:
        break
    board = []
    # 보드를 입력 받음
    for i in range(h):
        board.append(sys.stdin.readline().rstrip())
    # 시작 위치
    start = []
    # 쓰레기의 위치 저장
    target = []
    for i in range(h):
        for j in range(w):
            if board[i][j] == 'o':
                start = [(i, j)]
                continue
            if board[i][j] == '*':
                target.append((i, j))
    # 0 은 시작 위치에서 쓰레기 위치, 그외는 쓰레기 에서 쓰레기 위치
    target_dist = [[] for _ in range(len(start) + len(target))]
    q = deque()
    q.append(start[0])
    visited = [[-1] * w for _ in range(h)]
    visited[start[0][0]][start[0][1]] = 0
    # 못가는 곳이 있는지 확인하기 위한 변수
    ok = True
    # BFS 탐색
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= h or ny >= w:
                continue
            if visited[nx][ny] != -1:
                continue
            if board[nx][ny] == 'x':
                continue
            visited[nx][ny] = visited[x][y] + 1
            q.append((nx, ny))
    for i in target:
        if visited[i[0]][i[1]] == -1:
            # -1 일 경우 도달 불가능
            ok = False
            break
        else:
            target_dist[0].append(visited[i[0]][i[1]])
    if not ok:
        print(-1)
        continue
    # target_dist 의 인덱스로 사용
    pk = 0
    # 모든 쓰레기에서 쓰레기 위치 탐색을 위한 BFS
    for i in target:
        pk += 1
        q.append(i)
        visited = [[-1] * w for _ in range(h)]
        visited[i[0]][i[1]] = 0
        while q:
            x, y = q.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if nx < 0 or ny < 0 or nx >= h or ny >= w:
                    continue
                if visited[nx][ny] != -1:
                    continue
                if board[nx][ny] == 'x':
                    continue
                visited[nx][ny] = visited[x][y] + 1
                q.append((nx, ny))
        for i in target:
            target_dist[pk].append(visited[i[0]][i[1]])
    d = len(target)
    # 모든 경우의 수를 조사하기 위한 permutations
    can = list(itertools.permutations(list(range(1, d + 1)), d))
    ans = 2100000000
    for j in can:
        tmp = 0
        for i in range(d):
            if i == 0:
                # i = 0 일 경우 시작 위치에서 쓰레기의 위치까지
                tmp += target_dist[i][j[i] - 1]
            else:
                # i != 0 이면 전 위치에서 대상 위치까지
                tmp += target_dist[j[i - 1]][j[i] - 1]
        if ans > tmp:
            ans = tmp
    print(ans)
