# 第一步UnionFind骨架
class UnionFind:
    def __init__(self,n):
        self.parent = list(range(n))
        self.rank = [0] * n
        self.count = n

    def find(self,x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self,x,y):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x == root_y:
            return 

        if self.rank[root_x] > self.rank[root_y]:
            self.parent[root_y] = root_x
        elif self.rank[root_y] > self.rank[root_x]:
            self.parent[root_x] = root_y
        else:
            self.parent[root_x] = root_y
            self.rank[root_y] += 1

        self.count -= 1

    def connected(self,x,y):
        return self.find(x) == self.find(y)

    def getCount(self):
        return self.count

def kruskal(n,edges):

    uf = UnionFind(n)
    edges.sort(key = lambda x: x[2])
    total_cost = 0
    edges_used = 0

    for u,v,weight in edges:
        if uf.connected(u,v):
            continue
        else:
            uf.union(u,v)
            total_cost += weight
            edges_used += 1

    return total_cost if n-1 == edges_used else -1

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        edges = list() # (u,v,edges)
        for i in range(n):
            for j in range(i+1,n):
                distance = abs(points[i][0]-points[j][0]) + abs(points[i][1]-points[j][1])
                edges.append((i,j,distance))

        return kruskal(n,edges)


