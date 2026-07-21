class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        
        n = len(graph)
        color = [0] * n

        def dfs(node,c):
            color[node] = c

            for neighbor in graph[node]:
                if color[neighbor] == c:
                    return False
                if color[neighbor] == 0:
                    if not dfs(neighbor,3-c):
                        return False
            return True
        
        for i in range(n):
            if color[i] == 0:
                if not dfs(i,1):
                    return False
        return True