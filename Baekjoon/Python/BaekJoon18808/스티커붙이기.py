'''
BaekJoon 18808 스티커 붙이기
programmer: yooj
Date: 21.08.18
using: Pycharm  & Python3
Site: https://www.acmicpc.net/problem/18808
'''

import sys

r, c, k = map(int, sys.stdin.readline().split())
m = [[0] * c for _ in range(r)]


# 배열을 회전시키는 함수
def rotate(d):
    n = len(d)
    m = len(d[0])
    result = [[0] * n for _ in range(m)]
    for i in range(n):
        for j in range(m):
            result[j][n - i - 1] = d[i][j]
    return result


# k 개의 스티커를 붙이는 함수
for _ in range(k):
    a, b = map(int, sys.stdin.readline().split())
    sticker = []
    # 스티커를 입력 받아서 바로 바로 붙이는 식으로 구현
    for i in range(a):
        sticker.append(list(map(int, sys.stdin.readline().split())))
    check = True  # 스티커를 붙였으면 False 로 변경하여 해당 스티커에 대한 연산 종료
    for t in range(4):
        if check:  # 스티커를 안붙였을 때
            if t != 0:  # 처음을 제외하곤 회전을 함
                sticker = rotate(sticker)
            #  배열이 직사각형 일 경우 가로 세로가 변할 수 있으므로 다시 구한다.
            height = len(sticker)
            width = len(sticker[0])
            for i in range(r - height + 1):
                if not check:  # 붙였으면 종료
                    break
                else:
                    for j in range(c - width + 1):
                        flag = True  # 붙일수 있는지 확인하는 변수
                        if not check:
                            break
                        else:
                            for x in range(height):
                                if flag:
                                    for y in range(width):
                                        if sticker[x][y] == 0:
                                            continue

                                        if m[i + x][j + y] == 1:  # 이미 붙어있을 경우 종료
                                            flag = False
                                            break
                        if flag:  # 붙일 수 있을 경우
                            for x in range(height):
                                for y in range(width):
                                    if sticker[x][y] == 0:
                                        continue
                                    m[i + x][j + y] += 1  # 스티커를 붙임
                            check = False  # 붙인 것을 처리함

# 정답을 구함
ans = 0
for i in range(r):
    for j in range(c):
        if m[i][j] == 1:
            ans += 1
sys.stdout.write(str(ans))
