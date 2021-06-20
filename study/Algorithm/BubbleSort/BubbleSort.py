import sys

a = list(map(int, sys.stdin.readline().split()))
pp = 0
for i in range(len(a)):
    for j in range(len(a) - 1, i, -1):
        if a[j - 1] > a[j]:
            a[j - 1], a[j] = a[j], a[j - 1]

print(a)
