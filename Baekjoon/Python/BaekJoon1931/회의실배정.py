# /*
#  * BaekJoon 1931 회의실 배정
#  * programmer: yooj
#  * Date: 21.07.10
#  * using: Pycharm and python3
#  * Site: https://www.acmicpc.net/problem/1931
#  */

import sys

sys.setrecursionlimit(10 ** 9)  # 재귀 깊이 설정

n = int(sys.stdin.readline().rstrip())  # 받는 개수
data = []
for i in range(n):
    data.append(list(map(int, sys.stdin.readline().rstrip().split(" "))))
data.sort(key=lambda x: (x[1], x[0]))  # 끝나는 시간 기준으로 오름차순으로 정렬하고 만약 끝나는 시간이 같으면 시작하는 시간을 오름차 순으로 정렬


def searchNext(end, idx, ans):  # 재귀를 통해 끝나고 바로 시작할 회의를 선택함
    global data
    for i in range(idx + 1, len(data)):
        if end <= data[i][0]:  # 회의 탐색
            return searchNext(data[i][1], i, ans + 1)  # 찾으면 다시 탐색
    return ans


print(searchNext(data[0][1], 0, 1))  # 시작을 정해줌
