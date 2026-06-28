# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque
class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """

        res = []

        def traverse(root):
            if root is None:
                res.append('N')
                return 
            
            res.append(str(root.val))
            traverse(root.left)
            traverse(root.right)
        traverse(root)
        return ','.join(res)


        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        nodes = deque(data.split(','))

        def solve():
            val = nodes.popleft()
            if val == 'N':
                return None
            root = TreeNode(int(val))
            root.left = solve()
            root.right = solve()

            return root
        
        return solve()

        
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))