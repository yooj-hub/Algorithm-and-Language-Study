import sys

d = [-1] * 5001
t = int(sys.stdin.readline())
mod = 1000000007
d[0] = 1


def dp(k):
    if d[k] != -1:
        return d[k]
    if d[k] >= 0:
        return d[k]
    d[k] = 0
    for i in range(2, k + 1):
        d[k] += dp(i - 2) * dp(k - i)
        d[k] %= mod
    return d[k] % mod


for _ in range(t):
    n = int(sys.stdin.readline())
    print(dp(n))
