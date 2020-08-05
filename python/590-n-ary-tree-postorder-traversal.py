# easy

'''2020-07-08'''

# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

class Solution:
    def postorder(self, root: Node) -> List[int]:
        if not root:  # 空树
            return []
        if not root.children:
            return [root.val]
        ans_list = []
        for child in root.children:
            ans_list.extend(self.postorder(child))
        ans_list.append(root.val)
        return ans_list
