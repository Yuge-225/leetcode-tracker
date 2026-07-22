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
    def isconnected(self,x,y):
        return self.find(x) == self.find(y)
    
    def get_count(self):
        return self.count

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        union_find = UnionFind(n)
        for i in range(n):
            for j in range(i+1,n):
                if isConnected[i][j] == 1:
                    union_find.union(i,j)
        return union_find.get_count()