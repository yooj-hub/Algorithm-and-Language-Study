import sys

t = int(sys.stdin.readline())

for _ in range(t):
    kind = dict()
    n = int(sys.stdin.readline())
    for _ in range(n):
        name, k = map(str, sys.stdin.readline().split())
        if k not in kind.keys():
            kind[k] = 1
            continue
        kind[k] += 1
    answer = 1
    for i in kind.values():
        answer *= i + 1
    print(answer - 1)
