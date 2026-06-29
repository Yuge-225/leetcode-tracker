# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if root is None:
            return None
        if root.val == key:
            return self.handleDeletion(root)
        elif root.val < key:
            root.right = self.deleteNode(root.right,key)
        else:
            root.left = self.deleteNode(root.left,key)
        return root
    
    def handleDeletion(self, node):
        if node.left is None:
            return node.right
        
        if node.right is None:
            return node.left
        
        min_node = self.get_min(node.right)
        node.right = self.deleteNode(node.right,min_node.val)
        min_node.left = node.left
        min_node.right = node.right
        return min_node


    def get_min(self, node):
        while node.left:
            node = node.left
        return node