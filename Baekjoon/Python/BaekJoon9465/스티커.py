'''
BaekJoon 9465 스티커
programmer: yooj
Date: 21.08.06
using: Pycharm  & Python3
Site: https://www.acmicpc.net/problem/9465
'''

import sys


def solution():
    n = int(sys.stdin.readline())  # 테스트 케이스의 개수를 입력받음
    for _ in range(n):
        k = int(sys.stdin.readline())  # 스티커의 가로 개수
        a = []  # 스티커의 점수 목록을 저장할 배열
        d = [[0] * 3 for _ in range(k)]  # dynamic programming 을 할 배열
        for i in range(2):  # 입력 받음
            a.append(list(map(int, sys.stdin.readline().split())))
        ans = -1
        # dp 시작
        for i in range(k):
            if i == 0:
                d[i][0] = a[0][i]
                d[i][1] = a[1][i]
            else:
                d[i][2] = max(d[i - 1][0], d[i - 1][1])
                d[i][0] = max(d[i - 1][2], d[i - 1][1]) + a[0][i]
                d[i][1] = max(d[i - 1][2], d[i - 1][0]) + a[1][i]

        ans = max(*d[k-1], ans)
        sys.stdout.write(str(ans) + '\n')


if __name__ == '__main__':
    solution()
