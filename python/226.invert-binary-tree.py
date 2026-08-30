#
# @lc app=leetcode id=226 lang=python3
#
# [226] Invert Binary Tree
#

# @lc code=start
# Definition for a binary tree node.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# @lc code=start
class Solution:
    def invertTree(self, root: TreeNode | None) -> TreeNode | None:
        # check if root is a leaf node
        if not root:
            return
        
        # swap child nodes recursively
        root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
        return root
# @lc code=end

