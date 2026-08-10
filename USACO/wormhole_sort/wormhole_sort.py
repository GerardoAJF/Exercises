class DSU:
    def __init__(self, size) -> None:
        self.groups = size
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


with open("wormsort.in") as file:
    n, m = map(int, file.readline().split())

    cows = list(map(int, file.readline().split()))

    bad_cows = []
    for i in range(n):
        if cows[i] != i + 1:
            bad_cows.append(i)         

    ans = -1
    if bad_cows: 
        wormholes = []
        for _ in range(m- 1):
            wormholes.append(tuple(map(int, file.readline().split())))
        wormholes = sorted(wormholes, key=lambda x: x[2], reverse=True)        

        low = 0
        high = m - 1
        while low <= high:
            mid = (low + high) // 2
            dsu = DSU(n)
            for wormhole in wormholes[:mid + 1]:
                a, b, w = wormhole
                a, b = a - 1, b - 1
                dsu.union(a, b)

            for i in range(n):
                if dsu.find(i) != dsu.find(cows[i] - 1):
                    low = mid + 1
                    break
            else:
                ans = wormholes[mid][2]
                high = mid - 1
                
    with open("wormsort.out", "w") as write_file:
        write_file.write(str(ans))
