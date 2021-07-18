# 조합

import sys

n, m = map(int, input().split(" "))
ans = [0] * m


def dfs(idx, start, n, m):
    if idx == m:
        sys.stdout.write(' '.join(map(str, ans)) + '\n')
        return
    for x in range(start, n + 1):
        ans[idx] = x
        dfs(idx + 1, x + 1, n, m)


dfs(0, 1, n, m)
