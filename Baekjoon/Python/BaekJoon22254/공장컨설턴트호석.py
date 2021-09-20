import heapq
import sys

n, x = map(int, sys.stdin.readline().split())
a = list(map(int, sys.stdin.readline().split()))
left = 0
right = x - 1


def getAns(cnt: int) -> int:
    q = []
    for i in range(cnt):
        heapq.heappush(q, 0)
    for i in a:
        cur = heapq.heappop(q)
        heapq.heappush(q, (cur + i))
    return max(q)


while left <= right:
    mid = (left + right) // 2
    if getAns(mid) > x:
        left = mid + 1
    else:
        right = mid - 1

print(left)
