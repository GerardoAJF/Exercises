class DSU:
    def __init__(self, size) -> None:
        self.parents = list(range(size))
        self.sizes = [1 for _ in range(size)]

    def find(self, x) -> int:
        if self.parents[x] == x:
            return x

        self.parents[x] = self.find(self.parents[x])
        return self.parents[x]

    def unite(self, a, b):
        a_parent = self.find(a)
        b_parent = self.find(b)

        if a_parent == b_parent:
            return

        if self.sizes[b_parent] > self.sizes[a_parent]:
            a_parent, b_parent = b_parent, a_parent

        self.sizes[a_parent] += self.sizes[b_parent]
        self.parents[b_parent] = a_parent

    def connected(self, a, b):
        return 1 if self.find(a) == self.find(b) else 0

n, q = map(int, input().split())

dsu = DSU(n)
for _ in range(q):
    t, u, v = map(int, input().split())
    
    if t == 0:
        dsu.unite(u, v)
    else:
        print(dsu.connected(u, v))
