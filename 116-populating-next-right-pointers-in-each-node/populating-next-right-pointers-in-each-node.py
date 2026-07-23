"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
from collections import deque
class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        

        def level_order(root):
            if root is None:
                return
            queue = deque([root])
            depth = 1
            while queue:
                sz = len(queue)
                for i in range(sz):
                    curr = queue.popleft()
                    if i == sz -1:
                        curr.next = None
                    else:
                        curr.next = queue[0]
                    if curr.left:
                        queue.append(curr.left)

                    if curr.right:
                        queue.append(curr.right)

                    
                    
                depth += 1

            return root

        return level_order(root)




"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

from collections import deque
class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':

        if root is None:
            return root
        queue = deque([root])
        depth = 1
        while queue:
            sz = len(queue)
            for i in range(sz):
                cur = queue.popleft()
                if i < sz - 1:
                    cur.next = queue[0]
                else:
                    cur.next = None

                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)
                
            depth += 1
        return root

"""