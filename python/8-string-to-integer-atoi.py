# medium

'''2020-02-03'''
class Solution: # 面向测试编程
    def myAtoi(self, string):
        string = string.strip() # 去除空格
        ls = list(string)
        if ls == []:
            return 0

        is_neg = 0 # 判断符号
        if ls[0] == '-':
            is_neg = 1
            ls.pop(0)
        elif ls[0] == '+':
            ls.pop(0)

        if ls == []: # 原数仅有+/-号
            return 0

        if ls[0].isalpha(): # 原数首位或去除+/-号后首位仍为字母
            return 0

        integer = 0 # atoi
        while ls and ls[0].isdigit():
            integer = integer * 10 + int(ls[0])
            ls.pop(0)
        if is_neg:
            integer = -integer

        if integer > 2 ** 31 - 1: # 题目要求的防溢出
            return 2 ** 31 - 1
        if integer < -(2 ** 31):
            return -(2 ** 31)
        return integer