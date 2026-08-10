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
            return

        if self.weights[b_parent] > self.weights[a_parent]:
            a_parent, b_parent = b_parent, a_parent

        self.weights[a_parent] += self.weights[b_parent]
        self.parents[b_parent] = a_parent

    def __str__(self) -> str:
        return f"Parents: {self.parents}, Weights {self.weights}"

with open("mootube.in", "r") as file:
    n, q = map(int, file.readline().split())
    dsu = DSU(n)

    relations = []
    for _ in range(n - 1):
        p, p2, r = map(int, file.readline().split())
        relations.append((p, p2, r))
    relations = sorted(relations, key=lambda x: x[2], reverse=True)

    questions = []
    for i in range(q):
        k, v = map(int, file.readline().split())
        questions.append((k, v, i))
    questions = sorted(questions, key=lambda x: x[0], reverse=True)

    ans = [""] * q
    relation_id = 0
    for k, v, real_pos in questions:
        while relation_id < n - 1 and relations[relation_id][2] >= k:
            
            p, p2, _ = relations[relation_id]
            dsu.union(p - 1, p2 - 1)
            relation_id += 1
        
        root = dsu.find(v - 1)
        ans[real_pos] = str(dsu.weights[root] - 1)

    with open("mootube.out", "w") as write_file:
        write_file.write("\n".join(ans))