# 조합

import sys

n, m = map(int, input().split(" "))
ans = [0] * m
visited = [False] * (n + 1)


def dfs(idx, selected, n, m):
    if selected == m:
        sys.stdout.write(' '.join(map(str, ans)) + '\n')
        return
    if idx > n:
        return
    ans[selected] = idx
    dfs(idx + 1, selected + 1, n, m)
    ans[selected] = 0
    dfs(idx + 1, selected, n, m)


dfs(1, 0, n, m)
