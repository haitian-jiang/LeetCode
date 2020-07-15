#medium

from typing import List
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

'''2020-07-15'''
class Solution:
    output = []
    def inorderTraversal(self, root: TreeNode, clear=True) -> List[int]:
        if not root:  # 空树
            return []
        if clear:  # 初始化
            self.output = []
        if root.left:
            self.inorderTraversal(root.left, False)
        self.output.append(root.val)
        if root.right:
            self.inorderTraversal(root.right, False)
        return self.output
