class DSU:
    def __init__(self, size) -> None:
        self.groups = 0
        self.parents = list(range(size))
        self.sizes = [1] * size
        
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
            
        self.parents[b_parent] = a_parent
        self.sizes[a_parent] += self.sizes[b_parent]
        
        self.groups -= 1


with open("closing.in") as file:
    n, m = map(int, file.readline().split())

    adjacency_list = {i:[] for i in range(n)}
    for _ in range(m):
        a, b = [int(x) - 1 for x in file.readline().split()]
        adjacency_list[a].append(b)
        adjacency_list[b].append(a)

    actives = [False] * n

    dsu = DSU(n)

    response = []
    barns = [int(x) - 1 for x in file.readlines()]
    for barn in barns[::-1]:
        actives[barn] = True
        dsu.groups += 1

        for adjacent in adjacency_list[barn]:
            if actives[adjacent]:
                dsu.union(barn, adjacent)

        if dsu.groups == 1:
            response.append("YES")
        else:
            response.append("NO")

    with open("closing.out", "w") as write_file:
        write_file.write("\n".join(response[::-1]))