"""
BaekJoon 10971 외판원 순회 2
Programmer: yooj
Date: 2021 11 15
Using: Python 3 & pycharm
Site: https://www.acmicpc.net/problem/10971
"""

import heapq
import sys

# init
n = int(sys.stdin.readline())
w = []
for i in range(n):
    w.append(list(map(int, sys.stdin.readline().split())))

'''
입력 형식
n = 노드수
w[i][j] 는 i 에서 j 로 가는 cost 를 뜻한다.
'''



for i in range(n):
    for j in range(n):
        if w[i][j] == 0:
            w[i][j] = int(1e9)


class Node:
    '''
    bound -> 현재 얻게 될 수 있는 최소 이동 거리
    level -> 트리의 깊이 처음 시작점에서 0 기준
    path -> 지금까지 진행한 경로
    check -> 갖고 있는 path 의 원소들의 2**i 의 합을 통하여 이미 지난 경로 확인
    '''

    def __init__(self):
        self.bound = 0
        self.level = 0
        self.path = ''
        self.check = 0

    '''
    heapq 연산을 위한 함수
    '''

    def __lt__(self, other):
        if self.bound < other.bound:
            return True
        else:
            return False

    def get_bound(self) -> int:
        # res 는 bound 값이다.
        res = 0
        self.check = 0
        # 진행한 path 의 이동 거리
        for i in range(1, len(self.path)):
            res += w[ord(self.path[i - 1]) - ord('a')][ord(self.path[i]) - ord('a')]

        # 마지막 path 에서 이동할 수 있는 경로중 최솟값
        k = ord(self.path[-1]) - ord('a')
        res += min(w[k])

        #  남은 노드에서 현재 진행한 경로를 제외하고, 갈수 있는 최솟값
        a = []
        # path 를 통하여 check 를 만들음
        for i in range(len(self.path)):
            self.check += 2 ** (ord(self.path[i]) - ord('a'))
        # path 에 포함되지 않는 원소들을 a 에 저장
        for i in range(n):
            if self.check & (2 ** i):
                continue
            a.append(i)
        # 남은 노드에서 처음으로 돌아가거나, path 에 없는 원소로 가는 길 중 최솟 값을 더한다.
        for i in range(len(a)):
            m = w[a[i]][0]
            for j in range(len(a)):
                if i == j:
                    continue
                m = min(m, w[a[i]][a[j]])
            res += m
        del a

        return res

    # 진행 거리를 구하는 함수
    def get_length(self) -> int:
        res = 0
        for i in range(1, len(self.path)):
            res += w[ord(self.path[i - 1]) - ord('a')][ord(self.path[i]) - ord('a')]
        return res


# travel n = 2 일 경우 바로 구할 수 있다.
if n == 2:
    print(w[0][1] + w[1][0])
    sys.exit(0)

# priority queue 이용
pq = []
v = Node()
v.level = 0
v.path = "a"
min_length = int(1e9)
heapq.heappush(pq, v)
# 이동 경로
# opt_tour = ""
v.bound = v.get_bound()
# pq 이용
while pq:
    # bound 기준으로 min heap 을 이용
    v = heapq.heappop(pq)
    # bound 가 현재 구한 length 보다 작을 떄만 연산
    if v.bound < min_length:

        for i in range(1, n):
            # 이미 간 적 있으면 다음으로
            if (2 ** i) & v.check:
                continue
            # 트리의 자식 노드를 생성
            u = Node()
            u.level = v.level + 1
            u.path = v.path
            u.path += chr(ord('a') + i)
            # level 이 n-2 일 경우 현재 n-1개의 노드를 지낫으므로 따로 탐색하지 않고 나머지 노드와 처음으로 가는 경로를 추가한다.
            if u.level == n - 2:
                for j in range(1, n):
                    if j != 0 and j != i and v.check & (2 ** j) == 0:
                        u.path += chr(ord('a') + j)
                        u.path += 'a'
                        length = u.get_length()
                        # min length 갱신
                        if length < min_length:
                            min_length = length
                            # opt_tour = u.path
            # level < n-2 일 경우 하한이 현재 구한 거리보다 작을 경우만 pq 에 삽입
            else:
                u.bound = u.get_bound()
                if u.bound < min_length:
                    heapq.heappush(pq, u)
    # 만약 하한이 클 경우 정지
    else:
        break

print(min_length)
# 이동 경로 출력
# print(opt_tour)
