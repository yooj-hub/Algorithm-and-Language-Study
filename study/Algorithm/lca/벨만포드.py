import sys
from collections import namedtuple

INF = int(1e9)
Edge = namedtuple('Edge', 'fr to cost')

n, m = map(int, sys.stdin.readline().split())
a = []
dist = [0] * 501
for i in range(m):
    f, t, c = map(int, sys.stdin.readline().split())
    a.append(Edge(f, t, c))

for i in range(1, n + 1):
    dist[i] = INF

dist[1] = 0
negative_cycle = False
for i in range(1, n + 1):
    for j in range(m):
        x, y, z = a[j].fr, a[j].to, a[j].cost
        if dist[x] != INF and dist[y] > dist[x] + z:
            dist[y] = dist[x] + z
            if i == n: # n 번 이동할 경우 음수 사이클 존재
                negative_cycle = True

if negative_cycle:
    print(-1)
else:
    for i in range(2, n + 1):
        if dist[i] == INF:
            dist[i] = - 1
        print(dist[i])
