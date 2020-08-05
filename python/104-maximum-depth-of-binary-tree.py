# easy

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

'''2020-07-15'''
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:  # 空树
            return 0
        left = right = 0  # 如果为空，则深度为0
        if root.left:
            left = self.maxDepth(root.left)
        if root.right:
            right = self.maxDepth(root.right)
        return max(left, right) + 1
