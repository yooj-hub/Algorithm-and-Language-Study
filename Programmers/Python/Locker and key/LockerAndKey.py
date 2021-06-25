'''
 * Programmers 자물쇠와 열쇠
 * programmer: yooj
 * using : pycharm & python 3.9.5
 * Date: 21.06.25
 * Site: https://programmers.co.kr/learn/courses/30/lessons/60059
'''

import copy


def solution(key, lock):
    m = len(key)
    n = len(lock)
    turntime = 0
    while turntime != 4:
        for i in range(-m + 1, n):  # 4회 회전시 종료
            for j in range(-m + 1, n):
                temp = copy.deepcopy(lock)  # lock deep copy
                for k in range(m):
                    for x in range(m):
                        if 0 <= i + k < n and 0 <= j + x < n:  # 키의값을 자물쇠에 더하기
                            temp[i + k][j + x] += key[k][x]
                if (check(temp)):
                    return True
        key = turn(key)
        turntime += 1
    return False


def check(arr):  # 열리는지 확인
    n = len(arr)
    for i in range(n):
        for j in range(n):
            if (arr[i][j] != 1):
                return False
    return True


def turn(arr):  # 회전시키는 메소드
    n = len(arr)
    tmp = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            tmp[n - 1 - j][i] = arr[i][j]
    return tmp


key = [[0, 0], [0, 0]]
lock = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
print(solution(key, lock))
