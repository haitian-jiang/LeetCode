# easy

'''2020-11-25'''
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        s = sum(map(ord, s))
        t = sum(map(ord, t))
        return chr(t-s)