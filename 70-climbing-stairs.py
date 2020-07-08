# easy

'''2020-01-12'''
class Solution: # 动态规划
    def climbStairs(self, n: int) -> int:
        if n == 1 or n==2:
            return n
        dp_list = [1, 2]
        for i in range(2, n):
            dp_list.append(dp_list[i-1] + dp_list[i-2])
        return dp_list[-1]