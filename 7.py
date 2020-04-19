class Solution:
    def reverse(self, x: int) -> int:
        minus = 0 # 标记输入数字是否为0
        if x < 0: # 如果为0，就去相反数，采用与正数相同的算法，最后再去相反数得到答案
            minus = 1
            x = -x
        reversed_x = 0 # 存放答案
        while(x > 0): # 核心算法(秦九韶算法)
            reversed_x *= 10
            reversed_x += (x % 10)
            x //= 10
        if minus:
            reversed_x = -reversed_x
        if reversed_x > 2**31-1 or reversed_x < -2**31: # 判断输出结果是否越界
            reversed_x = 0
        return reversed_x