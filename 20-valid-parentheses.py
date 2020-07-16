# easy

'''2020-01-04'''
class Solution: # 题解抄来的，从最里面的括号对开始拆，如果合法最终所有的括号对都会被替换成空串。
    def isValid(self, s: str) -> bool:
        while("{}" in s or "[]" in s or "()" in s):
            s = s.replace("{}", "")
            s = s.replace("()", "")
            s = s.replace("[]", "")
        return s == ""

'''2020-07-16'''
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in s:
            if i in "([{":
                stack.append(i)
            else:
                if stack and "([{".find(stack[-1]) == ")]}".find(i):
                    stack.pop()
                else:
                    return False
        if stack:
            return False
        return True

