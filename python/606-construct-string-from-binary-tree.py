# easy

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

'''2020-07-15'''
class Solution:
    def tree2str(self, t: TreeNode) -> str:
        output = ''
        if not t:
            return output
        output = str(t.val) + output  # 加入当前节点
        if not t.right:
            if t.left:  # 仅无右节点
                output = output + f'({self.tree2str(t.left)})'
            # 无子节点则无需添加
        else:
            if not t.left:  # 仅无左节点
                output = output + f'()({self.tree2str(t.right)})'  # 需要加空括号来指明右节点
            else:  # 有左右节点
                output = output + f'({self.tree2str(t.left)})({self.tree2str(t.right)})'
        return output

