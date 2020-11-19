# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# ITERATIVE
# class Solution:
#     def searchBST(self, root: TreeNode, val: int) -> TreeNode:
#         current = root
#         while current:
#             if val == current.val:
#                 return current
#             elif val < current.val:
#                 current = current.left if current.left else None
#             elif val > current.val:
#                 current = current.right if current.right else None  
#         return
# Recursive
# class Solution:
#     def searchBST(self, root: TreeNode, val: int) -> TreeNode:
#         def helper(node):
#             if node == None:
#                 return
#             else:
#                 if val == node.val:
#                     return node
#                 elif val < node.val:
#                     return helper(node.left)
#                 elif val > node.val:
#                     return helper(node.right)
#         return helper(root)
        
        
