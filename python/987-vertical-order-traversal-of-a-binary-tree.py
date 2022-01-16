# hard
'''2022-01-16'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict
class Solution:
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        vertnodes = defaultdict(list)
        traversal = [(root, 0, 0)]
        while traversal:
            node, row, col = traversal.pop()
            vertnodes[col].append((row, node.val))
            if node.left:
                traversal.append((node.left, row+1, col-1))
            if node.right:
                traversal.append((node.right, row+1, col+1))
        for col in vertnodes:
            vertnodes[col].sort()
        return [[i[1] for i in vertnodes[col]] for col in sorted(vertnodes)]
