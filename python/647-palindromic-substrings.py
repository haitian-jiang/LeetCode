# medium

'''2020-07-22'''
class Solution:
    def countSubstrings(self, s: str) -> int:
        length = len(s)
        if length in (0, 1):
            return length
        amount = length
        for l in range(2, length + 1):
            for start in range(length - l + 1):
                obj = s[start : start+l]
                if obj == obj[::-1]:
                    amount += 1
        return amount

