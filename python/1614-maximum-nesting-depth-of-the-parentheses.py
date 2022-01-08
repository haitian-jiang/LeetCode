# easy
'''2022-01-07'''
class Solution:
    def maxDepth(self, s: str) -> int:
        s = "".join([c if c in "()" else "" for c in s])
        depth = 0
        stack = []
        for c in s:
            if c == "(":
                stack.append("(")
            else:
                stack.pop()
            depth = max(depth, len(stack))
        return depth
