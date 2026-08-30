#
# @lc app=leetcode id=543 lang=python3
#
# [543] Diameter of Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        d = self.height(root.left) + self.height(root.right)
        d_sub = max(self.diameterOfBinaryTree(root.left), self.diameterOfBinaryTree(root.right))
        return max(d, d_sub)
        
        
        
    def height(self, node):
        if not node:
            return 0
        else:
            return (max(self.height(node.left), self.height(node.right) ) + 1)
# @lc code=end

