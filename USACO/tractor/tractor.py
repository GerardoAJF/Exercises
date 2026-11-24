import itertools
import math

class DSU:
    def __init__(self, size) -> None:
        self.parents = list(range(size))
        self.weights = [1 for _ in range(size)]
        
    def find(self, x):
        if self.parents[x] == x:
            return x
        self.parents[x] = self.find(self.parents[x])
        return self.parents[x]
    
    def union(self, a, b):
        a_parent = self.find(a)
        b_parent = self.find(b)
        
        if a_parent == b_parent:
            return 0
        
        if self.weights[b_parent] > self.weights[a_parent]:
            a_parent, b_parent = b_parent, a_parent
            
        self.weights[a_parent] += self.weights[b_parent]
        self.parents[b_parent] = a_parent
        return self.weights[a_parent]


with open("tractor.in", "r") as file:
    n = int(file.readline())

    matrix = []
    for _ in range(n):
        matrix.append(tuple(map(int, file.readline().split())))

    edges = []
    for node in itertools.product(range(n), range(n)):
        # Bottom row
        if node[0] != n - 1:
            b_row = node[0] + 1

            a_high = matrix[node[0]][node[1]]
            b_high = matrix[b_row][node[1]]

            if a_high > b_high:
                a_high, b_high = b_high, a_high

            diff = b_high - a_high
            edges.append((diff, node, (b_row, node[1])))

        # Right column
        if node[1] != n - 1:
            r_column = node[1] + 1

            a_high = matrix[node[0]][node[1]]
            r_high = matrix[node[0]][r_column]

            if a_high > r_high:
                a_high, r_high = r_high, a_high

            diff = r_high - a_high
            edges.append((diff, node, (node[0], r_column)))
    edges = sorted(edges, key=lambda x: x[0])

    ans = 0        
    dsu = DSU(n * n)
    for edge in edges:
        weight = dsu.union((n * edge[1][0]) + edge[1][1], (n * edge[2][0]) + edge[2][1])

        if weight >= math.ceil((n * n) / 2):
            ans = edge[0]
            break

    with open("tractor.out", "w") as write_file:
        write_file.write(str(ans))