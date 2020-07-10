# hard

'''2020-07-10'''
class Solution:
    def lastSubstring(self, s: str) -> str:
        max_str = ''
        for i in range(len(s)):
            max_str = max(max_str, s[i:])
        return max_str
