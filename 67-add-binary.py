class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a,b = int(a,2), int(b,2) # 字符串转数字，按二进制，得到十进制数字
        return bin(a+b)[2:] # bin得到的结果形如'0b111'，需要去除左侧0b
        #https://blog.csdn.net/PanDD_0_1/article/details/86687140
        #string.atof