import sys
from collections import deque

n, k = map(int, sys.stdin.readline().split())

q = deque()
q.append((n, 0))
answer = -1
anc = 0
visited = [0] * 200001
c = [0] * 200001
visited[n] = 1
while q:
    cur, cnt = q.popleft()
    if cur == k and answer == -1:
        answer = cnt
    if cur == k:
        anc += visited[cur]
        continue
    if answer != -1 and cnt > answer:
        break
    if cur + 1 <= 150000:
        if visited[cur + 1] == 0:
            c[cur + 1] = cnt
            q.append((cur + 1, cnt + 1))
        if c[cur + 1] == cnt:
            visited[cur + 1] += visited[cur]
    if 0 <= cur - 1:
        if visited[cur - 1] == 0:
            c[cur - 1] = cnt
            q.append((cur - 1, cnt + 1))
        if c[cur - 1] == cnt:
            visited[cur - 1] += visited[cur]

    if 0 <= cur * 2 <= 200000:
        if visited[cur * 2] == 0:
            q.append((cur * 2, cnt + 1))
            c[cur * 2] = cnt
        if c[cur * 2] == cnt:
            visited[cur * 2] += visited[cur]

sys.stdout.write(str(answer) + '\n' + str(anc))
