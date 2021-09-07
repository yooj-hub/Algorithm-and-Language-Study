import sys
from collections import deque


def lca(u, v):
    if depth[u] < depth[v]:
        u, v = v, u
    log = 1
    while (1 << log) <= depth[u]:
        log += 1
    log -= 1
    for i in range(log, -1, -1):
        if depth[u] - (1 << i) >= depth[v]:
            u = p[u][i]
    if u == v:
        return u
    for i in range(log, -1, -1):
        if p[u][i] != 0 and p[u][i] != p[v][i]:
            u = p[u][i]
            v = p[v][i]
    return parent[u]


n = int(sys.stdin.readline())
a = [[] for _ in range(n + 1)]
depth = [0] * (n + 1)
check = [False] * (n + 1)
parent = [0] * (n + 1)

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
log = 1
while (1 << log) <= n:
    log += 1
log -= 1

p = [[0] * (log + 1) for _ in range(n + 1)]
for i in range(1, n + 1):
    p[i][0] = parent[i]

j = 1
while (1 << j) < n:
    for i in range(1, n + 1):
        if p[i][j - 1] != 0:
            p[i][j] = p[p[i][j - 1]][j - 1]
    j += 1

t = int(sys.stdin.readline())

for _ in range(t):
    u, v = map(int, sys.stdin.readline().split())
    print(lca(u, v))
