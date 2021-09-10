"""
Programmers 블록 이동하기
Programmer: yooj
Date: 2021 09 10
Using: Python 3 & pycharm
Site: https://programmers.co.kr/learn/courses/30/lessons/60063
"""

from collections import deque


def solution(board: [[int]]):
    q = deque()
    q.append([0, 0, 0, 1, 0])
    q.append([0, 1, 0, 0, 0])
    n = len(board)
    # 머리와 꼬리로 나누어 꼬리의 위치에 따라 방문 배열을 저장
    visited = [[[False] * 4 for _ in range(n)] for _ in range(n)]
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    # 처음 방향을 저장 ( 0, 2 가로 1, 3 세로)
    visited[0][0][0] = True
    visited[0][1][2] = True
    while q:
        cx, cy, tx, ty, time = q.popleft()
        # 도착할 경우
        if cx == n - 1 and cy == n - 1:
            return time
        if tx == n - 1 and ty == n - 1:
            return time
        # 도착이 아닐 경우
        # 4방향 이동
        for i in range(4):
            ncx = cx + dx[i]
            ncy = cy + dy[i]
            if not rangeOk(board, ncx, ncy, n):
                continue
            ntx = tx + dx[i]
            nty = ty + dy[i]
            if not rangeOk(board, ntx, nty, n):
                continue
            # 현재 방향에 따라 q에 삽입 하는 함수
            insert(q, ncx, ncy, ntx, nty, time, visited)
        # 오른쪽 회전 후 삽입
        rcx, rcy, rtx, rty = rightTurn(board, cx, cy, tx, ty, n)
        insert(q, rcx, rcy, rtx, rty, time, visited)
        # 왼쪽 회전 후 삽
        lcx, lcy, ltx, lty = leftTurn(board, cx, cy, tx, ty, n)
        insert(q, lcx, lcy, ltx, lty, time, visited)

    return -1


# 삽입하는 함수
def insert(q, cx, cy, tx, ty, time, visited):
    # cx cy 를 머리로 tx ty를 꼬리로
    dir1 = getDir(cx, cy, tx, ty)
    if not visited[cx][cy][dir1]:
        visited[cx][cy][dir1] = True
        q.append([cx, cy, tx, ty, time + 1])
    # 반대로
    dir2 = getDir(tx, ty, cx, cy)
    if not visited[cx][cy][dir2]:
        visited[cx][cy][dir2] = True
        q.append([tx, ty, cx, cy, time + 1])


# 외쪽으로 90도 회전하는 함수
def leftTurn(board, cx, cy, tx, ty, n):
    if ty - cy == 1:
        if rangeOk(board, cx - 1, cy + 1, n) and rangeOk(board, cx - 1, cy, n):
            tx, ty = cx - 1, cy
    elif ty - cy == -1:
        if rangeOk(board, cx + 1, cy, n) and rangeOk(board, cx + 1, cy - 1, n):
            tx, ty = cx + 1, cy
    elif tx - cx == -1:
        if rangeOk(board, cx, cy - 1, n) and rangeOk(board, cx - 1, cy - 1, n):
            tx, ty = cx, cy - 1
    elif tx - cx == 1:
        if rangeOk(board, cx + 1, cy + 1, n) and rangeOk(board, cx, cy + 1, n):
            tx, ty = cx, cy + 1
    return cx, cy, tx, ty


# 오른쪽으로 90도 회전하는 함수
def rightTurn(board, cx, cy, tx, ty, n):
    if ty - cy == 1:
        if rangeOk(board, cx + 1, cy + 1, n) and rangeOk(board, cx + 1, cy, n):
            tx, ty = cx + 1, cy
    elif ty - cy == -1:
        if rangeOk(board, cx - 1, cy - 1, n) and rangeOk(board, cx - 1, cy, n):
            tx, ty = cx - 1, cy
    elif tx - cx == -1:
        if rangeOk(board, cx - 1, cy + 1, n) and rangeOk(board, cx, cy + 1, n):
            tx, ty = cx, cy + 1
    elif tx - cx == 1:
        if rangeOk(board, cx, cy - 1, n) and rangeOk(board, cx + 1, cy - 1, n):
            tx, ty = cx, cy - 1
    return cx, cy, tx, ty


# 범위내에 있는지, 그 곳이 벽인지 확인하는 함수
def rangeOk(board, x, y, n):
    if x >= n or y >= n or x < 0 or y < 0:
        return False
    if board[x][y] == 1:
        return False
    return True


# 머리와 꼬리에따라 방향을 리턴하는 함수
def getDir(cx, cy, tx, ty):
    if ty - cy == 1:
        return 0
    elif tx - cx == -1:
        return 1
    elif ty - cy == -1:
        return 2
    else:
        return 3


print(solution([[0, 0, 0, 1, 1],
                [0, 0, 0, 1, 0],
                [0, 1, 0, 1, 1],
                [1, 1, 0, 0, 1],
                [0, 0, 0, 0, 0]
                ]))
