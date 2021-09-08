import sys


def init(tree: [int], a: [int], node: int, start: int, end: int):  # 포스트 오더
    if start == end:
        tree[node] = a[start]
    else:
        init(tree, a, node * 2, start, (start + end) // 2)
        init(tree, a, node * 2 + 1, (start + end) // 2 + 1, end)
        tree[node] = min(tree[node * 2], tree[node * 2 + 1])


def query(tree: [int], node: int, start: int, end: int, i: int, j: int):
    if i > end or j < start:
        return -1
    if i <= start and end <= j:
        return tree[node]
    m1 = query(tree, 2 * node, start, (start + end) // 2, i, j)
    m2 = query(tree, 2 * node + 1, (start + end) // 2 + 1, end, i, j)
    if m1 == -1:
        return m2
    elif m2 == -1:
        return m1
    else:
        return min(m1, m2)


def update(tree: [int], node: int, start: int, end: int, index: int, value: int):
    if index < start or end < index:
        return
    if start == end:
        tree[node] = value
        return
    update(tree, node * 2, start, (start + end) // 2, index, value)
    update(tree, node * 2 + 1, (start + end) // 2 + 1, end, index, value)
    tree[node] = min(tree[node * 2], tree[node * 2 + 1])


def fenwickTreeSum(tree: [int], i: int):
    ans = 0
    while i > 0:
        ans += tree[i]
        i -= (i & -i)
    return ans


def fenwickTreeUpdate(tree: [int], i: int, num: int):
    while i <= n:
        tree[i] += num
        i += (i & -i)



n, m = map(int, sys.stdin.readline().split())
a = [0] * n
log = 0
while (1 << log) <= n:
    log += 1
tree_size = (1 << (log + 1))
tree = [0] * tree_size
for i in range(n):
    a[i] = int(sys.stdin.readline())

init(tree, a, 1, 0, n - 1)
for _ in range(m):
    start, end = map(int, sys.stdin.readline().split())
    print(query(tree, 1, 0, n - 1, start - 1, end - 1))
