import heapq
import sys

input = sys.stdin.readline

INF = int(1e9)
VERTEX = 20000

vertex = [[] for _ in range(VERTEX + 1)]
d = [INF] * (VERTEX + 1)


def dijkstra(start):
    d[start] = 0
    pq = []
    heapq.heappush(pq, (0, start))
    while pq:
        dist, cur = heapq.heappop(pq)
        for i in vertex[cur]:
            cost = dist + i[0]
            if cost < d[i[1]]:
                d[i[1]] = cost
                heapq.heappush(pq, (cost, i[1]))


v, e = map(int, input().split())
start = int(input())
for i in range(e):
    f, t, c = map(int, input().split())
    vertex[f].append((c, t))
dijkstra(start)

for i in range(1, v + 1):
    if d[i] == INF:
        print("INF")
    else:
        print(d[i])
