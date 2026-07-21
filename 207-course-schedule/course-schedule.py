from collections import deque
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = [ [] for _ in range(numCourses)]
        indegree = [0] * numCourses

        for src, dest in prerequisites:
            graph[src].append(dest)
            indegree[dest] += 1
        
        queue = deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)
        
        res = []
        while queue:
            node = queue.popleft()
            res.append(node)

            for neighbor in graph[node]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)
        
        return True if len(res) == numCourses else False