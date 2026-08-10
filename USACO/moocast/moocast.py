import itertools

class DSU:
    def __init__(self, size) -> None:
        self.parents = list(range(size))
        self.weights = [1 for _ in range(size)]
    
    def find(self, x):
        if self.parents[x] == x:
            return x
        self.parents[x] = self.find(self.parents[x])
        return self.parents[x]
    
    def union (self, a, b):
        a_parent = self.find(a)
        b_parent = self.find(b)
        
        if a_parent == b_parent:
            return
        
        if self.weights[b_parent] > self.weights[a_parent]:
            a_parent, b_parent = b_parent, a_parent
            
        self.weights[a_parent] += self.weights[b_parent]
        self.parents[b_parent] = a_parent

with open("moocast.in", "r") as file:
    n = int(file.readline())

    points = []
    for i in range(n):
        point = tuple(map(int, file.readline().split()))
        points.append((i, point))

    combinations = list(itertools.combinations(points, 2))
    edges = []
    for comb in combinations:
        edge =((comb[0][1][0] - comb[1][1][0])**2) + ((comb[0][1][1] - comb[1][1][1])**2)
        edges.append((edge, comb[0][0], comb[1][0]))
    edges = sorted(edges, key=lambda x: x[0])
    
    low = 0
    high = len(edges) - 1    
    max_distance = 0
    while low <= high:
        mid = (low + high) // 2
        
        dsu = DSU(n)
        for edge in edges[:mid + 1]:
            dsu.union(edge[1], edge[2])
        
        if dsu.weights[dsu.find(0)] == n:
            max_distance = edges[mid][0]
            high = mid - 1   
        else:
            low = mid + 1

    with open("moocast.out", "w") as write_file:
        write_file.write(str(int(max_distance)))
        