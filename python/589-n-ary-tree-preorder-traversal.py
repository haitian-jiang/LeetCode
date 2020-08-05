# easy

# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

'''2020-07-15'''
class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        if not root:  # 空树
            return []
        if not root.children:
            return [root.val]
        ans_list = []
        ans_list.append(root.val)
        for child in root.children:
            ans_list.extend(self.preorder(child))
        return ans_list
