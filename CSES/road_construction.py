class DSU:
    def __init__(self, size):
        self.max = None
        self.n_groups = size
        self.parents = list(range(size))
        self.sizes = [1 for _ in range(size)]

    def find(self, x):
        if self.parents[x] == x:
            return x

        self.parents[x] = self.find(self.parents[x])
        return self.parents[x]    

    def union(self, a, b):
        a_parent = self.find(a)
        b_parent = self.find(b)

        if a_parent == b_parent:
            return

        if self.sizes[b_parent] > self.sizes[a_parent]:
            a_parent, b_parent = b_parent, a_parent

        self.sizes[a_parent] += self.sizes[b_parent]
        self.parents[b_parent] = a_parent

        if not self.max:
            self.max = self.sizes[a_parent]

        if self.sizes[a_parent] > self.max:
            self.max = self.sizes[a_parent]

        self.n_groups -= 1

n, m = map(int, input().split())
dsu = DSU(n)
for _ in range(m):
    a, b = map(int, input().split())
    
    dsu.union(a - 1, b - 1)
    print(dsu.n_groups, dsu.max)
