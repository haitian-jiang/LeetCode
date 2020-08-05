# easy

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

'''2020-07-15'''
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:  # 空树
            return 0
        left = right = 0  # 如果为空，则深度为0
        if root.left:
            left = self.minDepth(root.left)
        if root.right:
            right = self.minDepth(root.right)
        if (left, right) == (0, 0):  # 只有根节点
            return 1
        if left and not right:  # 右子树为空
            return left + 1
        if not left and right:  # 左子树为空
            return right + 1
        return min(left, right) + 1
