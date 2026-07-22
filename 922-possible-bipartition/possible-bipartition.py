class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        graph = [[] for _ in range(n)]
        for relation in dislikes:
            node1 = relation[0] - 1
            node2 = relation[1] - 1
            
            graph[node1].append(node2)
            graph[node2].append(node1)
        
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
                
