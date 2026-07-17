# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        

        if root is None:
            return

        left_res = root.left
        right_res = root.right
        root.left = right_res
        root.right = left_res
            
        self.invertTree(root.left)
        self.invertTree(root.right)

        return root







"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        def traverse(root):
            if root is None:
                return
            else:
                # 我们只处理当前节点的左右子节点交换
                temp = root.left
                root.left = root.right
                root.right = temp
                # 左右子树的交换去交给递归完成
                traverse(root.left)
                traverse(root.right)
        
        traverse(root)
        return root
                
"""