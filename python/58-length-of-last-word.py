# easy

'''2020-01-12'''
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        ls = s.split() # 转存为列表
        if ls == []: # s为空串或只有空格
            return 0
        if ls[-1].isalpha(): # 判断是否是单词
            return len(ls[-1])
        else: # 否则为符号或数字
            return 0