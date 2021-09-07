import sys
sys.setrecursionlimit(int(1e9))

n = int(sys.stdin.readline())
a = [[] for _ in range(n + 1)]
tin = [0] * (n + 1)
tout = [0] * (n + 1)
timer = 0
l = 0
while (1 << l) <= n:
    l += 1
l -= 1
p = [[0] * (l + 1) for _ in range(n + 1)]


def upper(u, v):
    return tin[u] <= tin[v] and tout[u] >= tout[v]


def lca(u, v):
    if upper(u, v):
        return u
    if upper(v, u):
        return v
    for i in range(l, -1, -1):
        if not upper(p[u][i], v):
            u = p[u][i]
    return p[u][0]


def dfs(v, parent):
    global timer
    timer += 1
    tin[v] = timer
    p[v][0] = parent
    for i in range(1, l+1):
        p[v][i] = p[p[v][i - 1]][i - 1]
    for to in a[v]:
        if to != parent:
            dfs(to, v)
    timer += 1
    tout[v] = timer


for i in range(n - 1):
    u, v = map(int, sys.stdin.readline().split())
    a[u].append(v)
    a[v].append(u)
dfs(1, 1)


t = int(sys.stdin.readline())
for _ in range(t):
    u, v = map(int, sys.stdin.readline().split())
    print(lca(u, v))
