# easy

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

'''2020-07-15'''
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if bool(p) ^ bool(q):  # 只有一个空树
            return False
        if not p and not q:  # 都是空树
            return True
        if p.val != q.val:  # 当前节点
            return False
        if bool(p.left) ^ bool(q.left) or bool(p.right) ^ bool(q.right):  # 一个有子树另一个没有
            return False
        if p.left and not self.isSameTree(p.left, q.left):  # 短路算法，有子树是两子树不同
            return False
        if p.right and not self.isSameTree(p.right, q.right):
            return False
        return True
