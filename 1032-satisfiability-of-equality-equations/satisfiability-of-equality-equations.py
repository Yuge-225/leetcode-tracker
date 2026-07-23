class UnionFound:
    def __init__(self,n):
        self.parent = {chr(i):chr(i) for i in range(ord('a'),ord('z')+1)}
        self.count = n
        self.rank = {chr(i):0 for i in range(ord('a'),ord('z')+1)}

    
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
        elif self.rank[root_x] < self.rank[root_y]:
            self.parent[root_x] = root_y
        else:
            self.parent[root_x] = root_y
            self.rank[root_y] += 1
        self.count -= 1
    def connected(self,x,y):
        return self.find(x) == self.find(y)
    def getcount(self):
        return self.count

class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        n = len(equations)
        uf = UnionFound(n)
        for equation in equations:
            x = equation[0]
            y = equation[3]
            if equation[1] == '!':
                continue
            if equation[1] == '=':
                uf.union(x,y)
        

        for equation in equations:
            x = equation[0]
            y = equation[3]
            if equation[1] == '!':
                if uf.connected(x,y):
                    return False
        return True