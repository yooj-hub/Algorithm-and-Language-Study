import sys
from collections import deque


def lca(u, v):
    if depth[u] > depth[v]:
        u, v = v, u
    while depth[u] != depth[v]:
        v = parent[v]
    while u != v:
        u = parent[u]
        v = parent[v]
    return u


n = int(sys.stdin.readline())
a = [[] for _ in range(n + 1)]
depth = [-1] * (n + 1)
check = [False] * (n + 1)
parent = [-1] * (n + 1)

for i in range(n - 1):
    u, v = map(int, sys.stdin.readline().split())
    a[u].append(v)
    a[v].append(u)

q = deque()
q.append(1)
parent[1] = 0
check[1] = True
depth[1] = 0
while q:
    x = q.popleft()
    for i in a[x]:
        if not check[i]:
            check[i] = True
            depth[i] = depth[x] + 1
            parent[i] = x
            q.append(i)

t = int(sys.stdin.readline())

for _ in range(t):
    u, v = map(int, sys.stdin.readline().split())
    print(lca(u,v))