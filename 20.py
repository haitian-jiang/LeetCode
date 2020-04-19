class Solution: # 题解抄来的，从最里面的括号对开始拆，如果合法最终所有的括号对都会被替换成空串。
    def isValid(self, s: str) -> bool:
        while("{}" in s or "[]" in s or "()" in s):
            s = s.replace("{}", "")
            s = s.replace("()", "")
            s = s.replace("[]", "")
        return s == ""