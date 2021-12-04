"""
BaekJoon 2580 스도쿠
Programmer: yooj
Date: 2021 12 04
Using: Python 3 & pycharm
Site: https://www.acmicpc.net/problem/2580
"""

import sys

# 입력 받기
data = []
for i in range(9):
    data.append(list(map(int, sys.stdin.readline().split())))
# 탐색해야할 리스트
checkList = []

# Row 에 대한 검사 Column 에 대한 검사 Square 에 대한 검사
checkRow = [[False] * 9 for _ in range(9)]
checkColumn = [[False] * 9 for _ in range(9)]
checkSquare = [[False] * 9 for _ in range(9)]


# row, column 바탕으로 몇번째 row, column 인지 확인
def getSquareNum(row, column):
    return row // 3 * 3 + column // 3


# check 를 바꾸는 함수
def changeCheck(row, column, val, flag):
    checkRow[row][val - 1] = flag
    checkColumn[column][val - 1] = flag
    checkSquare[getSquareNum(row, column)][val - 1] = flag


# 초기 설정
for i in range(9):
    for j in range(9):
        if data[i][j] == 0:
            checkList.append((i, j))
        else:
            changeCheck(i, j, data[i][j], True)


# backtracking 으로 답 구하기
def dfs(idx):
    if idx == len(checkList):
        return True
    x, y = checkList[idx][0], checkList[idx][1]
    for i in range(9):
        if not checkRow[x][i] and not checkColumn[y][i] and not checkSquare[getSquareNum(x, y)][i]:
            data[x][y] = i + 1
            changeCheck(x, y, i + 1, True)
            if dfs(idx + 1):
                return True
            changeCheck(x, y, i + 1, False)


dfs(0)

for i in range(9):
    print(' '.join(map(str, data[i])))
