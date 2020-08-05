# easy

'''2020-01-06'''
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle == "":
            return 0
        if needle not in haystack:
            return -1
        length = len(needle)
        for i in range(len(haystack)-length+1):
            if(haystack[i:i+length] == needle):
                return i