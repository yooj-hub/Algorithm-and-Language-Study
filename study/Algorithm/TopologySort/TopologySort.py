from collections import deque

VERTEX = 200000
graph = [[] for _ in range(VERTEX)]
theNumberOfEdgesFromVertex = [0] * VERTEX
vertexes, edges = map(int, input().split())

for i in range(edges):
    f, t = map(int, input().split())
    graph[f].append(t)
    theNumberOfEdgesFromVertex[t] += 1
q = deque()
for i in range(1, vertexes + 1):
    if theNumberOfEdgesFromVertex[i] == 0:
        q.append(i)
        print(i, end =" ")

while q:
    cur = q.popleft()
    for c in graph[cur]:
        theNumberOfEdgesFromVertex[c] -= 1
        if theNumberOfEdgesFromVertex[c] == 0:
            q.append(c)
            print(c, end = " ")

