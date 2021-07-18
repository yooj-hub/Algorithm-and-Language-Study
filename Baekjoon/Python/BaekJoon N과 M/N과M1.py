# 순열

import sys

n, m = map(int, input().split())
ans = [0] * m
visited = [False] * (n + 1)


def dfs(idx):
    global m
    global n
    global ans
    if idx == m:
        sys.stdout.write(' '.join(map(str, ans)) + '\n')
        return
    for x in range(1, n + 1):
        if not visited[x]:
            visited[x] = True
            ans[idx] = x
            dfs(idx + 1)
            visited[x] = False


dfs(0)
