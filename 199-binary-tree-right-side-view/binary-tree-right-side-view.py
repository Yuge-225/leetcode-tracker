# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        def level_order(root):
            if root is None:
                return
            queue = deque([root])
            while queue:
                sz = len(queue)
                for i in range(sz):
                    cur = queue.popleft()
                    if i == sz - 1:
                        res.append(cur.val)
                    if cur.left:
                        queue.append(cur.left)
                    if cur.right:
                        queue.append(cur.right)
        
        level_order(root)
        return res
                    












"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        
        if root is None:
            return []

        queue = deque([root])
        depth = 1
        res = []

        while queue:
            sz = len(queue)
            for i in range(sz):
                cur = queue.popleft()

                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)
                
                if i == sz - 1:
                    res.append(cur.val)

                
            depth += 1
        return res
        
"""