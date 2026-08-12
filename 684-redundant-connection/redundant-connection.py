class UnionFound:
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
        if self.rank[root_x] < self.rank[root_y]:
            self.parent[root_x] = root_y
        elif self.rank[root_x] > self.rank[root_y]:
            self.parent[root_y] = root_x
        else:
            self.parent[root_x] = root_y
            self.rank[root_y] += 1
        self.count -= 1
    def connected(self,x,y):
        return self.find(x) == self.find(y)
    def get_count(self):
        return self.count

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        uf = UnionFound(n)

        for edge in edges:
            node1 = edge[0] - 1
            node2 = edge[1] - 1
            if uf.connected(node1,node2):
                return edge
            uf.union(node1,node2)
        







"""
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
        
        
        遍历每条边(u,v)：
            先检查u和v是否已经连通
            
            如果已经连通 → 说明这条边加进去会形成环 → 这就是答案，直接返回
            如果没有连通 → 正常合并，继续处理下一条边
        
        n = len(edges)
        uf = UnionFound(n)
        for edge in edges:
            # 一开始所有节点都是独立的，随着union操作逐渐连通，直到某条边的两端已经连通了，那条边就是多余的（会形成环）。
            u = edge[0] - 1 # 节点值转索引
            v = edge[1] - 1

            if uf.connected(u,v):
                return edge
            else: #随着遍历边，逐步产生连通关系
                uf.union(u,v)

"""