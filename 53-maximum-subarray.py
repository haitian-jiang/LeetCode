# easy
from typing import List

'''
超时，复杂度O(n^3)
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ans = max(nums)
        for i in range(len(nums)):
            for j in range(i+2, len(nums)+1):
                ans = max(ans, sum(nums[i:j]))
        return ans

超时，复杂度O(n^2)，参考刘汝佳
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ans = nums[0]
        s = [0]
        for i in range(len(nums)):
            s.append(s[i]+nums[i])
        for i in range(len(s)-1):
            for j in range(i+1,len(s)):
                ans = max(ans, s[j]-s[i])
        return ans

'''

class Solution: # 动态规划解法，复杂度O(n)
    def maxSubArray(self, nums: List[int]) -> int:
        for i in range(1,len(nums)): # 更新过的num[i]表示以i结尾的子序列和的最大值，最终答案为更新后num中的最大值即可
            nums[i] = nums[i] + max(0,nums[i-1]) # 如果前面的最大和还比0小，就不取此数之前的
        return max(nums)