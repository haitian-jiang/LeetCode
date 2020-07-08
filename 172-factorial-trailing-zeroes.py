# easy

'''2020-02-13'''
class Solution: # LeetCode标程遇到大数会溢出
    def trailingZeroes(self, n: int) -> int:
        ans = 0
        while n:
            ans += n // 5
            n //= 5
        return ans