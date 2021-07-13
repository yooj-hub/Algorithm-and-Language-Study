import sys

n = int(sys.stdin.readline().rstrip())
data = []
for i in range(n):
    data.append(int(sys.stdin.readline().rstrip()))
ptr = data[-1]
ans = 0
for i in range(n - 2, -1, -1):
    if ptr <= data[i]:
        ans += data[i] - ptr + 1
        data[i] = ptr - 1
    ptr = data[i]

print(ans)
