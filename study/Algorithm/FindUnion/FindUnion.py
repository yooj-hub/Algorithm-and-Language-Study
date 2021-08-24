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


