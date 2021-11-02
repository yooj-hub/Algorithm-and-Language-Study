import copy
import sys
import heapq

n, m, x = map(int, sys.stdin.readline().split())
INF = int(1e9)
VERTEX = n
vertex = [[] for _ in range(VERTEX + 1)]
for i in range(m):
    f, t, w = map(int, sys.stdin.readline().split())
    vertex[f].append((w, t))

# dijkstra 를 하기위한 배열
d = [INF] * (VERTEX + 1)
check = [False] * (VERTEX + 1)


# dijkstra
def dijkstra(start):
    d[start] = 0
    pq = []
    heapq.heappush(pq, (0, start))
    while pq:
        dist, cur = heapq.heappop(pq)
        if check[cur]:
            continue
        check[cur] = True
        for i in vertex[cur]:
            cost = dist + i[0]
            if cost < d[i[1]]:
                d[i[1]] = cost
                heapq.heappush(pq, (cost, i[1]))


dijkstra(x)
# 집을 가는 거리를 미리 구해둠
go_home = copy.deepcopy(d)
answer = -1
for i in range(1, n + 1):
    # 자기 집에서 파티하는 경우 생략
    if i == x:
        continue
    d = [INF] * (VERTEX + 1)
    check = [False] * (VERTEX + 1)
    dijkstra(i)
    answer = max(answer, d[x] + go_home[i])

print(answer)
