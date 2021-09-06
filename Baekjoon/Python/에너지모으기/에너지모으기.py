import sys

n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))


def go(arr):
    if len(arr) == 2:
        return 0
    ans = 0
    for i in range(1, len(arr) - 1):
        tmp = go(arr[:i] + arr[i + 1:]) + arr[i - 1] * arr[i + 1]
        if ans < tmp:
            ans = tmp
    return ans


print(go(a))
