# medium
from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

'''2020-11-16'''
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if not preorder:
            return None
        if len(preorder) == 1:
            return TreeNode(preorder[0])
        root = TreeNode(preorder[0])
        len_left = inorder.index(root.val) + 1
        root.left = self.buildTree(preorder[1:len_left], inorder[:len_left])
        root.right = self.buildTree(preorder[len_left:], inorder[len_left:])
        return root