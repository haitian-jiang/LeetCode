'''2020-07-06'''
class Solution:
    def reverseWords(self, s: str) -> str:
        return ' '.join(s.split()[::-1])
