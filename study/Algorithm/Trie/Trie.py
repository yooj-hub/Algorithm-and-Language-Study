import sys


class Node(object):
    def __init__(self):
        self.valid = False
        self.children = [-1] * 26


class Trie:

    def __init__(self):
        self.trie = []
        self.root = self.init()

    def init(self):
        x = Node()
        self.trie.append(x)
        return len(self.trie) - 1

    def add(self, node, s, idx):
        if idx == len(s):
            self.trie[node].valid = True
            return
        c = ord(s[idx]) - ord('a')
        if self.trie[node].children[c] == -1:
            nx = self.init()
            self.trie[node].children[c] = nx
        child = self.trie[node].children[c]
        self.add(child, s, idx + 1)

    def addString(self, s):
        self.add(self.root, s, 0)

    def search(self, node, s, idx):
        if node == -1:
            return False
        if idx == len(s):
            return self.trie[node].valid
        c = ord(s[idx]) - ord('a')
        child = self.trie[node].children[c]
        return self.search(child, s, idx + 1)

    def searchString(self, s):
        return self.search(self.root, s, 0)


trie = Trie()
n, m = map(int, sys.stdin.readline().split())
ans = 0
for i in range(n):
    trie.addString(sys.stdin.readline().rstrip())
for j in range(m):
    if trie.searchString(sys.stdin.readline().rstrip()):
        ans += 1

print(ans)
