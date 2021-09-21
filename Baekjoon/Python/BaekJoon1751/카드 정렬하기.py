"""
BaekJoon 1715 카드 정렬하기
Programmer: yooj
Date: 2021 09 19
Using: Python 3 & pycharm
Site: https://www.acmicpc.net/problem/1715
"""

import heapq

n = int(input())
pq = []
for _ in range(n):
    heapq.heappush(pq, int(input()))
ans = 0
while len(pq) != 1:
    a, b = heapq.heappop(pq), heapq.heappop(pq)
    ans += a + b
    heapq.heappush(pq, a + b)
print(ans)
