VERTEX = 200000


def findDirectParent(parent: list, x: int):
    if parent[x] == x: return x
    return findDirectParent(parent, parent[x])


def findParent(parent: list, x: int):
    if parent[x] == x: return parent[x]
    return findParent(parent, parent[x])


def unionParent(parent: list, a: int, b: int):
    a = findParent(parent, a)
    b = findParent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


parent = [0] * VERTEX
# vertexes, edges = map(int, input().split())
vertexes = int(input())
edges = int(input())

graph = []
for i in range(1, vertexes + 1):
    parent[i] = i
for i in range(edges):
    f, t, cost = map(int, input().split())
    graph.append((cost, f, t))
graph.sort()

answer = 0
for i in range(edges):
    f = graph[i][1]
    t = graph[i][2]
    if findParent(parent, f) == findParent(parent, t):
        continue
    else:
        unionParent(parent, f, t)
        answer += graph[i][0]
print(answer)
