import heapq
import sys
from collections import namedtuple


class Edge:
    def __init__(self, to, cost):
        self.to = to
        self.cost = cost

    def __lt__(self, other):
        return self.cost < other.cost

    def __str__(self):
        return "to: " + str(self.to) + " cost: " + str(self.cost)


def greater(a: Edge, b: Edge):
    return a.cost < b.cost


n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
a = [[] for _ in range(1001)]
c = [False] * 1001

for i in range(m):
    fr, t, co = map(int, sys.stdin.readline().split())
    a[fr].append(Edge(t, co))
    a[t].append(Edge(fr, co))

c[1] = True

pq = []
for e in a[1]:
    heapq.heappush(pq, e)

ans = 0
while pq:
    e = heapq.heappop(pq)
    if c[e.to]:
        continue
    c[e.to] = True
    ans += e.cost
    x = e.to
    for ee in a[x]:
        heapq.heappush(pq, ee)
print(ans)
