class UnionFound:
    def __init__(self,n):
        self.parent = list(range(n))
        self.rank = [0] * n
        self.count = n
    
    def find(self,x):
        if self.parent[x]!= x:
            self.parent[x] = self.find(self.parent[x])

        return self.parent[x]
    def union(self,x,y):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x == root_y:
            return
        if self.rank[root_x] > self.rank[root_y]:
            self.parent[root_y] = root_x
        elif self.rank[root_x] < self.rank[root_y]:
            self.parent[root_x] = root_y
        else:
            self.parent[root_x] = root_y
            self.rank[root_y] += 1
        self.count -= 1
    def connected(self,x,y):
        return self.find(x) == self.find(y)
    def getCount(self):
        return self.count

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        uf = UnionFound(n)
        for edge in edges:
            u = edge[0] - 1
            v = edge[1] - 1

            if uf.connected(u,v):
                return edge
            else:
                uf.union(u,v)

